import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib.animation import FuncAnimation

# 1. Define signals
def x_func(tau):
    """Periodic square wave: period 2, alternating between +1 and -1."""
    return np.where(np.mod(tau + 0.5, 2.0) < 1.0, 1.0, -1.0)

def h_sliding(tau, t):
    """h(t - tau) = 1 - (t - tau) for t - 1 <= tau <= t, else 0."""
    tau = np.asarray(tau)
    val = 1.0 - (t - tau)
    return np.where((tau >= t - 1.0) & (tau <= t), val, 0.0)

def y_analytical(t):
    """Analytical periodic output for y(t) = x(t) * h(t)."""
    t = np.asarray(t)
    t_mod = np.mod(t + 0.5, 2.0) - 0.5  # maps to [-0.5, 1.5)
    return np.where(
        t_mod < 0.5,
        -t_mod**2 + t_mod + 0.25,
        t_mod**2 - 3.0 * t_mod + 1.75
    )

# 2. Setup Canvas
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 7), sharex=False)
plt.subplots_adjust(left=0.1, bottom=0.25, right=0.9, top=0.93, hspace=0.35)

tau = np.linspace(-3.5, 4.5, 1600)
t_range = np.linspace(-2.5, 3.5, 1200)

# Top Subplot: Overlap of x(tau) and h(t - tau)
ax1.set_xlim(-3.5, 4.5)
ax1.set_ylim(-1.5, 1.6)
ax1.set_ylabel(r"$x(\tau),\; h(t - \tau)$", fontsize=11)
ax1.set_title(r"Que. 2: Moving Window $h(t - \tau)$ over Periodic Square Wave $x(\tau)$", fontsize=12)
ax1.grid(True, linestyle="--", alpha=0.5)

ax1.plot(tau, x_func(tau), 'b-', lw=2, label=r"$x(\tau)$ (Square Wave)")
line_h, = ax1.plot([], [], 'r-', lw=2.2, label=r"$h(t - \tau)$ (Reversed Ramp)")
fill_poly = [ax1.fill_between([], [], color='orange', alpha=0.5, label="Integrand Area")]
ax1.legend(loc="upper right", framealpha=0.9)

# Bottom Subplot: Resulting output y(t)
ax2.set_xlim(-2.5, 3.5)
ax2.set_ylim(-0.8, 0.8)
ax2.set_xlabel(r"$t$", fontsize=11)
ax2.set_ylabel(r"$y(t) = x(t) * h(t)$", fontsize=11)
ax2.set_title(r"Convolution Output $y(t)$ (Periodic)", fontsize=12)
ax2.grid(True, linestyle="--", alpha=0.5)

ax2.plot(t_range, y_analytical(t_range), 'gray', linestyle=":", lw=1.8, label="Full Waveform")
line_trace, = ax2.plot([], [], 'g-', lw=2.2, label=r"$y(t)$ Traced")
point_y, = ax2.plot([], [], 'go', markersize=8)
text_val = ax2.text(0.02, 0.82, '', transform=ax2.transAxes, fontsize=10, weight="bold")
ax2.legend(loc="upper right", framealpha=0.9)

# 3. Add Slider and Play/Pause Button
ax_slider = plt.axes([0.15, 0.12, 0.7, 0.03])
slider_t = Slider(ax_slider, "Time (t)", -2.0, 3.0, valinit=-1.0, valstep=0.02)

ax_btn = plt.axes([0.15, 0.04, 0.12, 0.04])
btn_play = Button(ax_btn, "Pause")

# 4. Update Function
is_playing = [True]

def update_plot(t):
    h_vals = h_sliding(tau, t)
    line_h.set_data(tau, h_vals)
    
    # Overlap shaded region: integrand = x(tau) * h(t - tau)
    fill_poly[0].remove()
    overlap = x_func(tau) * h_vals
    fill_poly[0] = ax1.fill_between(tau, 0, overlap, color='orange', alpha=0.5)
    
    # Traced curve up to current t
    t_history = t_range[t_range <= t]
    line_trace.set_data(t_history, y_analytical(t_history))
    
    y_curr = float(y_analytical(t))
    point_y.set_data([t], [y_curr])
    text_val.set_text(f"t = {t:.2f}\ny(t) = {y_curr:.3f}")
    fig.canvas.draw_idle()

def on_slider_change(val):
    update_plot(val)

slider_t.on_changed(on_slider_change)

def toggle_play(event):
    is_playing[0] = not is_playing[0]
    btn_play.label.set_text("Play" if not is_playing[0] else "Pause")

btn_play.on_clicked(toggle_play)

def animate(frame):
    if is_playing[0]:
        new_t = slider_t.val + 0.03
        if new_t > 3.0:
            new_t = -2.0
        slider_t.set_val(new_t)
    return line_h, line_trace, point_y

anim = FuncAnimation(fig, animate, interval=30, blit=False)
update_plot(slider_t.val)

plt.show()
import random

bot = random.choice(["r", "p", "s"])

player_input = input("You have options: \nRock (r)\nPaper (p)\nScissor (s)\nEnter your Choice: ")

player = player_input.lower()

mapping = {
    "r" : "Rock",
    "p" : "Paper",
    "s" : "Scissor",
}

print(f"Bot chose {mapping[bot]}\nYou chose {mapping[player]}")

if(bot == player):
    print("it's a Draw !")

else:
    if((bot == "r" and player == "p") or (bot == "p" and player == "s") or (bot == "s" and player == "r")):
        print("you Won !")

    else:
        print("Bot Won !")

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if a > b:
    if a > c:
        g = a
    else:
        g = c
elif b > c:
    g = b
else:
    g = c

print("Greatest number is ", g)

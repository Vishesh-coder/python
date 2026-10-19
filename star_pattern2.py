n = int(input("Enter a number: "))

print(n*"* ")
for j in range(1,n-1):
    print("* ", end="")
    print((n-2)*"  ", end="")
    print("* ")
    
print(n*"* ")
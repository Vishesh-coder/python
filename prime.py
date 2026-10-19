n = int(input("Enter any number: "))
x = 0

if(n<=1):
    print("Not prime")

else:
    for i in range(2,n):
        if(n%i == 0):
            print("Number is not prime")
            break
    
        else:
            print("Number is prime")
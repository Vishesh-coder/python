n=int(input("Enter a number: "))
c=0
if n==1:
    print(n,"is Not Prime")
else:
    for i in range(2,n):
        if i<n:
            if n%i==0:
                c=1
                break

    if c==0:
        print(n,"is Prime")
    else:
        print(n,"is Not Prime")

n = int(input("Enter your Number: "))

for i in range(2,n):
    if(n%i == 0):
        print("This is not a Prime")
        break
else:
    print("This is prime")
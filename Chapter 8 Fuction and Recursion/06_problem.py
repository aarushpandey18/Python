#Multiplication of a Number using function
def multiple(n):
    for i in range(1,11):
        print (f"{n} X {i} = {n*i}")

n=int(input("Enter your Number: "))
print(f"Multiplication is: {multiple(n)}")
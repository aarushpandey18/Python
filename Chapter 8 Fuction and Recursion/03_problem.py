#Sum of n natural Number using Fucntion

def sumof(n):
    if(n==1):
        return 1
    return sumof(n-1) + n

n=int(input("Enter Your Number: "))
print(f"The Sum of n is: {sumof(n)}") 
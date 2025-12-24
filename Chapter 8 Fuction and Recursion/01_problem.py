def greater(a,b,c):
    if(a>b and a>c):
       return a
    elif(b>a and b>c):
      return b
    elif(c>a and c>b):
        return c

a=int(input("Enter Number a: "))
b=int(input("Enter Number b: "))
c=int(input("Enter Number c: "))

print(greater(a, b, c))

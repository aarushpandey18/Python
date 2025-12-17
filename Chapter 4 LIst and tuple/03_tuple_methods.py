#tuple.count() tuple me 1 number kitni bar ata hn
a=(1, 2, 3, 45,45, 6)
b=a.count(45)
print(b)

#tuple.index() return the index value of number jo phele ayega  
a=(10, 10, 12, 20, 100,500)
no=a.index(10)
print(no)

#concatennation Add two tuple 
tuple1=("Aarush")
tuple2=("Pandey")
concatenated= tuple1  +  tuple2
print(concatenated)

#repetation
a=("Aarushpandey")
repeted = a*3
print(repeted)

#membership "in" check itmes present in list and give true or false
my_tuple = (1,2,5,4)
print(2 in my_tuple)
print(5 in my_tuple)
print(100 in  my_tuple)

#length 
name=("Aarush")
print(len(name))

#min and max 
num=(45,1,100,10)
print(min(num))
print(max(num))

#slicing
my_tuple=(1,2,3,4,5,6)
sliced = my_tuple[1:4]
print(sliced)

#unpacking
kuchbhi=(1, 2, 5)
a, b, c = kuchbhi
print(kuchbhi)
print(a,b,c)
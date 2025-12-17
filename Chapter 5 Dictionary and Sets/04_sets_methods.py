s = {1, 2, 3, 5, 5, 6, 6, 70, "Aarush"}
print(s,type(s))

#set.add 
s = {1, 2, 3, 5, 5, 6, 6, 70, "Aarush"}
s.add("Dubey")
print(s)

#set.update([])
s = {1, 2, 3, 5, 5, 6, 6, 70, "Aarush"}
s.update(["Pandey"])
print(s)

#remove()
s = {1, 2, 3, 5, 5, 6, 6, 70, "Aarush"} 
s.remove('Aarush') #agr set me element nhi ho or tum remove kr rhe toh error show krega 
print(s)

#discard()
s = {1, 2, 3, 5, 5, 6, 6, 70, "Aarush"}
s.discard(0) #agr set me element nhi hoga toh koi error nhi show karega 
print(s)

#set.pop
s = {1, 2, 3, 5, 5, 6, 6, 70, "Aarush"}
s.pop() #one one by one element ko remove krta hn
print(s)

#set.clear()
s={1, 2, 3, 4,"Aarush"}
s.clear()
print(s)












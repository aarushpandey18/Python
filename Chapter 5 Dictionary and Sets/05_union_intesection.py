#set1.union(s2)merge s1 and s2
s1 = {1,2, 45, 6}
s2 = {7, 1, 75, 81, 91}
print(s1.union(s2))

#set1.intersection(s2) take common value from set1 and set2
s1 = {1,2, 45, 6}
s2 = {7, 1, 2 ,75, 81, 91}
print(s1.intersection(s2))

#set1.difference(set2)
s1 = {1, 2, 3}
s2 = {3, 4, 2, 1}
print(s2.difference(s1))

#set.symmetric_difference(set2) eleminate the common value 
s1 = {1, 2, 3}
s2 = {4}
print(s1.symmetric_difference(s2))

#set1.issubset(set2) set 1 or set 2 me same number hoge toh true warna false
s1 = {4}
s2 = {1, 2, 3}
print(s1.issubset(s2))

#set1.issuperset(set2) dono set pura same hona chaiye
s1 = {1, 2, 3, 4}
s2 = {1, 2, 3}
print(s2.issuperset(s1))

#set1.isdisjoint(set2)  dono set me kuch bhi same nhi hona chaiye
s1 = {1, 2, 3, }
s2 = {4,5,6}
print(s1.isdisjoint(s2))

#set1.copy()
s1 = {1, 2, 3, 4, 5}
s2 = s1.copy()
print(s2) 

#set.Pop first element eliminate 
s1 = {1, 2, 3, 4, 5}
s1.pop()
print(s1)





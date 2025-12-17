marks = {
    "Aarush" : 100,
    "Dubey" : 75,
    "Dhruv" : 35
 }
print(marks) 
 
#dict.items() give a list of(key,value) in tuples
marks = {
    "Aarush" : 100,
    "Dubey" : 75,
    "Dhruv" : 35
}

print(marks.items())

#dict.keys
marks = {
    "Aarush" : 100,
    "Dubey" : 75,
    "Dhruv" : 35
 }
print(marks.keys())

#dict.values
marks = {
    "Aarush" : 100,
    "Dubey" : 75,
    "Dhruv" : 35
 }
print(marks.values())

#dict.update()
marks = {
    "Aarush" : 100,
    "Dubey" : 75,
    "Dhruv" : 35
 }
marks.update({"Dhruv" : 99})
print(marks)

#dict.gets()
marks = {
    "Aarush" : 100,
    "Dubey" : 75,
    "Dhruv" : 35
 }
print(marks.get("Harry2")) #prints none
print(marks["Aarush"])     # prints an error
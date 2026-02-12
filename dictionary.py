#dictionary-stores data in key value pairs
student={
    "name":"mike",
    "age":17,
    "city":"mombasa"
}
print(student)
print(type(student))
#accessing the values
print(student.get("name"))
print(student["city"])
#change value
student["city"]="nairobi"
print(student)
#adding key:value
student["course"]="fullstack"
print(student)
#print all keys
print(student.keys())
#print all values
print(student.values())
#print all items
print(student.items())
#loop through:
#keys
for a in student.keys():
    print(a)
#values
for a in student.values():
    print(a)
#keys and values
for x,y in student.items():
    print(x,":",y)















#list-a collection of items stored in one variable
#list are ordered,changeable and allow duplicates
from operator import index

students=["john","mary","lewis","lucy","jackson"]
mynum=[39,89,76,78,45,67]
print(mynum)
print(type(mynum))
#list constructor lis()
mycourses =list(("html","css","java","bootstrap","python"))
print(mycourses)
print(type(mycourses))
#access list item
print(students[1])
print(mycourses[2])
print(mycourses[-1])
#list methods len(),insert(),remove()
#len
print(len(students))
print(len(mycourses))
#append()-add an item at the end
students.append("james")
print(students)
#remove()-removes an item
students.remove("lewis")
print(students)
#insert()-adds item at given index
students.insert(1,"anna")
print(students)
students.pop()
print(students)
print(students)
#pop(),sort()
students.pop()
print(students)
students.sort()
print(students)
#loop
for a in students:
    print(a)
for x in mycourses:
    print(x)


























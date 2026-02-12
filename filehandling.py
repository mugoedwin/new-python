#open(filename,mode)
#mode-w-write,r-read a-append x-create
x=open('example.txt', "r")
print(x.read())
x.close()
#write
y=open('demo.txt','w')
y.write("This is python")
y.close()
#append
z=open('example.txt','a')
z.write('\nThis is some appended text')
z.close()
#read
x=open('example.txt','r')
print(x.read())
x.close()















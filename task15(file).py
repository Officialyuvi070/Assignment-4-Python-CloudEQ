# Files Input/Output Function
# read, write, append, open

# Use write() the File
f = open("yuvi.txt",'w')
data = f.write("Hello! I am Yuvraj")
print(data)
f.close()

# Use append() function in file
f = open("yuvi.txt",'a')
f.write(" from CloudEQ")
f.close()

# Use read() function in file
f = open("yuvi.txt")
data = f.read()
print(data)
f.close()
# Reading a file 

# open
file = open("file.txt")

# read
content = file.read(22)
print(content, end='')

more_content = file.read(35)
print(more_content)

# close
file.close()
# Reading a file

# open
file = open("file.txt", "r")


# read
content = file.readline()
print(content, end='')

more_content = file.readline()
print(more_content)

# close
file.close()

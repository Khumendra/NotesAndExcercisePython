# Reading a file

# open
file = open('file.txt', "r")

# read
content = file.readlines()
print(*content, sep='\n')

# more_content = file.readlines()
# print(more_content)


# close
file.close()

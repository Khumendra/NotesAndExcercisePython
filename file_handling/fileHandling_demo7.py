# If a file doesn't exist, a new file will be created.
# If the file already exists, It's overwritten
# Write a file which doesn't exist


with open("file_write.txt", "w") as file:
    file.write("\n")
    
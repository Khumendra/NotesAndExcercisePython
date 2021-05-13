# readlines()

with open("file.txt","r") as file:
    lines = file.readlines()
    print(*lines, sep='')
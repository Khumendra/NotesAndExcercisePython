# file = open("file.txt")


with open('file.txt', 'r') as file:
    content = file.read(10)
    print(content)

    more_content = file.readline()
    print(more_content)

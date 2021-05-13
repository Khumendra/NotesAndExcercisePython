# Reading a file

file = open('file.txt', 'r')

print(
    file.read(),
    # file.read(6),
    # file.readable(),
    # file.readline(),
)

file.close()
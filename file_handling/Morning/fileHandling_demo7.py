# Appending a file
with open("file.txt", "a") as file:
    lines = ["\n",
             "Python is my fav lang", "\n",
             "\t Python is amazing",
             ]
    file.writelines(lines)

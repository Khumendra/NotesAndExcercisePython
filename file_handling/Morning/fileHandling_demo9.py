# Delete the file

import os

file = "file.txt"

print('##########', os.path.exists(file))
if os.path.exists(file):
    os.remove(file)
else:
    print(f"{file} doesn't exists")

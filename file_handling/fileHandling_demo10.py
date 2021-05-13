# writelines()

with open("js.txt", "w") as file:
    lines = [
        "Js is Awesome", "\nJs is my 2nd favorite prg lang"
    ]

    file.writelines(lines)
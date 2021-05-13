for _ in range(int(input())):
    s = input()
    for i in range(len(s)-1):
        if (s(i) != s(i+1)):
            print(s(i), end='')
        else:
            continue
        print(s[len(s)-1], end='')
    print()
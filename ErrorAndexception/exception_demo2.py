a = 10
b = 0

try:
    print(a/b)
except ZeroDivisionError as zde:
    print("You can't divide by 0")
    print(zde)

print('Done!')
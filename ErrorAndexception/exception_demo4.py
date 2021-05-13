a = 5
b = 10


try:
    print('Open')
    print(a/b)
except Exception as e:
    print("You can't divide by 0",e)
finally:
    print("Closed")

print('Done')
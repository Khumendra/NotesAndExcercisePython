a = 5
b = 5

try:
    print('Open')
    print(a/b)

    n = int(input('number: '))
    print(n)
except ZeroDivisionError as e:
    print("You can't divide num by 0 ")
    print('Error:', e)

except ValueError as e:
    print('Invalid Input: ')
    print("Error:", e)
except Exception as e:
    print('Somthing went wrong...')
    print(e)
finally:
    print('Closed')

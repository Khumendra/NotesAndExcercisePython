print('Resource Open')

try:
    num1 = int(input('number1: '))
    num2 = int(input('number2: '))

    division = num1/num2
    print(division)

except Exception as e:
    print('Error:', e)

else:
    print('All Good!')

finally:
    print('Finally Done!')


print('File Closed')
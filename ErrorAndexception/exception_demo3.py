
try:
    a = int(input('number: '))
    b = int(input('denominator: '))

    print('Open')
    print(a/b)
    print('Closed')

except ValueError as ve:
    print('Please Enter the Number value')

except Exception as e:
    print('Error:', e)

try:
    numerator = int(input('Enter numerator: '))
    denominator = int(input('Enter denominator: '))
    result = numerator / denominator
    print(result)
except ZeroDivisionError as zd:
    print('Denominator cannot be 0. Please try again.')
    print("Error:", zd)
print('Programs ends')

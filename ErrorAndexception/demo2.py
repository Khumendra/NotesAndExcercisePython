try:
    numerator = int(input('Enter numerator: '))
    denominator = int(input('Enter denominator: '))
    result = numerator / denominator
    print(result)

    my_list = [1,2,3]
    i = int(input("Enter index: "))
    print(my_list[i])

except ZeroDivisionError as zd:
    print('Denominator cannot be 0. Please try again.')
    print("Error:", zd)

except IndexError:
    print('Index cannot be greater than size of list.')
print('Programs ends')


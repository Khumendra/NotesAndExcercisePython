try:
    # risky code goes here...

    numerator = int(input('Numerator: '))
    denominator = int(input('Denominator: '))

    result = numerator / denominator
    print(result)

except ZeroDivisionError as zde:
    print("You can't divide number by 0.")
    print("Error:", zde)

except ValueError as ve:
    print("Please Enter the int value..")
    print("Error:",ve)

else:
    print('All Good!')


print('Done.')
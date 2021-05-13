user_input = input('Do you want to print numbers y/n: ').lower()
user_input_result = {'y': True, 'n': False}

if user_input not in user_input_result:
    print('Unrecoginzed user entry!')

else:
    successful = user_input_result[user_input]
    
    if successful:
        numbers = [ x for x in range(1, 11)]
        print(*numbers, sep='  ')
    else:
        print("Thanks for response!")
    
    

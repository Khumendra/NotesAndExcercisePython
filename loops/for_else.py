# successful = False
successful = True


for number in range(3):
    print(number+1, "Attempt")
    if successful:
        print("successful")
        break
else:
    print('Attempted 3 Times and failed')

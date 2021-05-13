# and, or, not

high_income = False
good_credit = True
student = True


# if not student:
#     print('Eligible')

# if high_income or good_credit:
#     print('Eligible')

if (high_income or good_credit) and not student:
    print('Eligible')
else:
    print('Not Eligible')

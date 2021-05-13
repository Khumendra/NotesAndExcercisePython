# *args = tuple()


name = "Makku"
email = "xyz@gmail.com"
phone = 7879921319
extras = {'value': "Some Values", 'isstudent': True, 'flag': False, }


def info(name, email, phone, *extras):
    # print(name, email, phone)
    print(extras)
    print(type(extras))


info(name, email, phone, extras)

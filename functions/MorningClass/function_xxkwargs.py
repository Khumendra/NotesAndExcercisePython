#  **kwargs ----> dict() {"key":"value"}


def bio(**bio):
    print(bio)
    print(type(bio))


bio(
    name='Vishal',
    age=21,
    address='Hyderabad',
    phone=7879921319

)

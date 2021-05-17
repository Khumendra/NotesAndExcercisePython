li = [1, 2, 3]

iter_obj = iter(li)

while True:
    try:
        print(next(iter_obj))

    except StopIteration:
        break


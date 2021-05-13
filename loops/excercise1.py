# Print all the even number

count = 0
# for x in range(1, 10):
    
#     if x % 2 == 0:
#         count += 1
#         print(x)
# print(f'We have count {count} even numbers')

# list comprehension

numbers = [x for x in range(1, 10) if x % 2 == 0]

print(
    *numbers, sep='\n', 
)

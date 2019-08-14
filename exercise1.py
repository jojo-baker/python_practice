# Lists

name = 'jo'
level = 5
awesomeness = 95.9
is_raining = True

# backpack = []
# print()

backpack = [
    'drink bottle',
    'yoghurt',
    'headphones',
    'laptop',
]

# print(backpack)

backpack.append('blueberries')
backpack.append('book')
backpack.append('pythons')
# print(backpack)

# print(backpack[0])
# print(backpack[1])

# can change parts of a list
backpack[0] ='lunchbox'
# print(backpack)

# print(name[0])
# can't change parts of a string
# name[0] = 'c'
# print(name)

# for index, item in enumerate(backpack): # item can be anything, it represents something within the variable
#     print(index, item)

# print()




num = 1
for num in range(1, 11):
    print(num)

print()

num = 1
while num <= 10:
    print(num)
    num += 1
## TASK 1

# given a 5x5 grid, add the last column and row, then flip the card at the
# coordinate specified by the user

five_by_five_grid = [
    ['X','0','X','X','X'],
    ['X','X','0','0','0'],
    ['X','0','X','0','X'],
    ['0','X','X','X','X'],
    ['X','0','0','X','X'],
]

# first step is to add colum 6 and row 6

# count how many X values in row 1
#   if x = odd then appeand X
#   if x = even then append with 0
# repeat for all rows

five_by_five_grid = [ int(items) for items in five_by_five_grid]


list_1_total = sum(five_by_five_grid[0])
print(list_1_total)

# output the grid to the user
for item in five_by_five_grid:
    print(item)
# ask the user for the coordinate of the card to flip
# e.g. input could be: (0,2)
coordinate = input('Enter a coordinate ')
# coordinate_items = coordinate.split(", ")
# print (coordinate_items)

coordinate_items = [x.strip('()') for x in coordinate.split(',')]
print (coordinate_items)

# output the grid with the flipped card


## TASK 2

# given a six by six grid, work out what card was flipped

# your program should output the coordinate of the flipped card
# in this case it would be: (x,y)
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

# Count number of x's in each row and if even, append with a 0 otherwise append with an X
for row in five_by_five_grid:
    x_count = row.count('X')
    if x_count % 2 == 0:
        row.append ('0')
    else:
        row.append ('X')

# Count the number of x's in first value of each list, if even, append with a 0 otherwise append with an X
# Another for loop to check item 0 in each row - define each col and then figure out how to simplify the code

sum1 = 0
for row in five_by_five_grid:
   xcol1 = row[0].count('X')
   sum1 = sum1 + xcol1
if sum1 % 2 == 0:
        col1 = '0'
else:
        col1 = 'X'

sum2 = 0
for row in five_by_five_grid:
   xcol2 = row[1].count('X')
   sum2 = sum2 + xcol2
if sum2 % 2 == 0:
        col2 = '0'
else:
        col2 = 'X'

sum3 = 0
for row in five_by_five_grid:
   xcol3 = row[2].count('X')
   sum3 = sum3 + xcol3
if sum3 % 2 == 0:
        col3 = '0'
else:
        col3 = 'X'

sum4 = 0
for row in five_by_five_grid:
   xcol4 = row[3].count('X')
   sum4 = sum4 + xcol4
if sum4 % 2 == 0:
        col4 = '0'
else:
        col4 = 'X'

sum5 = 0
for row in five_by_five_grid:
   xcol5 = row[4].count('X')
   sum5 = sum5 + xcol5
if sum5 % 2 == 0:
        col5 = '0'
else:
        col5 = 'X'

sum6 = 0
for row in five_by_five_grid:
   xcol6 = row[5].count('X')
   sum6 = sum6 + xcol6
if sum6 % 2 == 0:
        col6 = '0'
else:
        col6 = 'X'

five_by_five_grid.append ([col1, col2, col3, col4, col5, col6])

# output the grid to the user
for row in five_by_five_grid:
    print(row)

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
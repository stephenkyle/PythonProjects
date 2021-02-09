# This program displays a pattern in the shape of a triangle
# starting with 7 * and ending with one *
size = 7
for rows in range(size, 0, -1):
    for columns in range (rows):
        print('*',end='')
    print()

print('Stephen Oakford')

rows = 5
for i in range(1, rows + 1):
    if i == 1:
        print(' ' * (rows - i) + '*')
    elif i == rows:
        print('* ' + ' ' * (2 * (rows - 2)) + '*')
    else:
        print(' ' * (rows - i) + '*' + ' ' * (2 * i - 3) + '*')

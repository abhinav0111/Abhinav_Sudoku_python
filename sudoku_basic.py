import tkinter as tk
table = [
    [4, 0, 6, 5, 0, 2, 8, 0, 9],
    [0, 0, 0, 0, 4, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 5],
    [6, 0, 0, 8, 0, 0, 1, 0, 0],
    [5, 0, 0, 0, 7, 0, 0, 8, 0],
    [3, 0, 2, 9, 0, 4, 0, 6, 0],
    [0, 2, 0, 6, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 5, 3, 9, 4, 0],
    [8, 3, 0, 0, 9, 0, 0, 0, 2],

]


# Now we have to recuerssively check the values
def solve(table):

    # For finding the table completly filled or not
    k = find_empty(table)
    if k == None:
        return True
# If it is not filled now take the values and chack one by one
    else:
        row = k[0]
        col = k[1]
    for i in range(1, 10):
        if valid(table, i, k) == True:
            table[row][col] = i
    # If the perviouse recursed values returned true then it is valid if not
    # we have to back track as it returns false
            if solve(table) == True:
                return True
            table[row][col] = 0

    return False

    # If table not filled now we have to.........


# To check the value is valid to put in or not
def valid(table, num, pos):

    # checking rows
    for i in range(len(table)):
        if table[pos[0]][i] == num and pos[1] != i:
            return False

    # checking coloumns
    for i in range(len(table)):
        if table[i][pos[1]] == num and pos[0] != i:
            return False

    # checking the values in that table
    row = pos[0]//3
    col = pos[1]//3

    for i in range(row*3, row*3 + 3):
        for j in range(col*3, col*3 + 3):
            if table[i][j] == num and pos[0] != i and pos[1] != j:
                return False
    return True

# For printing the values


def print_table(table):
    for i in range(0, len(table)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(table[i])):
            if j % 3 == 0:
                print(" | ", end="")
            print(table[i][j], end=" ")
        print("")


# to find next x,y values that the value should be placed
def find_empty(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == 0:
                l = [i, j]
                return l
    return None


print_table(table)
print(find_empty(table))
print(valid(table, 3, [0, 4]))
solve(table)
print_table(table)

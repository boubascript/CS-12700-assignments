gridTest = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def printGrid(grid):
    for col in range(len(grid[0])):
        line = ""
        for row in range(len(grid)):
            line += grid[row][col]
        print(line)
        
printGrid(gridTest)

#Attempt to print jagged arrays

jaggedTest = [['.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O'],
        ['O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def printJaggedGrid(grid):
    for col in range(len(grid[0])):
        line = ""
        for row in range(len(grid)):
            line += grid[row][col]
        print(line)

print("\n\n")
printJaggedGrid(jaggedTest)
    
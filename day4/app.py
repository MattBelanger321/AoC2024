count = 0
grid = []

def search(grid, r, c):
    try:
        if grid[r-1][c-1] == "M" and grid[r+1][c+1] == "S": # M top left
            if grid[r+1][c-1] == "M" and grid[r-1][c+1] == "S": # M Bottom left
                return 1
            elif  grid[r+1][c-1] == "S" and grid[r-1][c+1] == "M": # S Bottom left
                return 1
            else:
                return 0
        elif grid[r-1][c-1] == "S" and grid[r+1][c+1] == "M": # S Top left
            if grid[r+1][c-1] == "M" and grid[r-1][c+1] == "S": # M Bottom left
                return 1
            elif  grid[r+1][c-1] == "S" and grid[r-1][c+1] == "M": # S Bottom left
                return 1
            else:
                return 0
        else:
            return 0
    except:
        return 0

with open("input.txt") as f:
    for line in f:
        grid.append(line.strip())

grid = grid

for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == 'A':
            count += search(grid,r,c)

print(count)

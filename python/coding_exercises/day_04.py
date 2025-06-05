"""
grid = ['uxf', 'vof', 'hmp']


def gridChallenge(grid):
    def is_sorted(string: str):
        return string == "".join(sorted(string))  

    sorted_grid =[]
    for row in grid:
        sorted_row = "".join(sorted(row))
        sorted_grid.append(sorted_row)

    for i in range(len(grid[0])):
        if is_sorted("".join([item[i] for item in sorted_grid])):
            continue
        else:
            return "NO"
    return "YES"

print(gridChallenge(grid))
"""

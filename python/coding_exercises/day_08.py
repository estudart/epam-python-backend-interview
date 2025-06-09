"""
petrolpumps = [[1, 5], [10, 3], [3, 4], [2, 5], [5, 1]]

def truckTour(petrolpumps):
    smallest_index = 0
    current_fuel = 0
    total_fuel = 0
    total_distance = 0
    
    for i in range(len(petrolpumps)):
        fuel, distance = petrolpumps[i]
        total_fuel += fuel
        total_distance+=distance
        current_fuel+=fuel - distance
        
        if current_fuel < 0:
            smallest_index = i + 1
            current_fuel = 0

    if total_fuel < total_distance:
        return -1
    else:
        return smallest_index

print(truckTour(petrolpumps))
"""


"""
s = "{)[](}]}]}))}(())("
def isBalanced(s):
    if len(s) % 2 != 0:
        return "NO"

    opening_order = []

    opening_brackets = ["{", "(", "["]

    mapping_brackets = {
        "}": "{",
        ")": "(",
        "]": "["
    }

    for i in range(len(s)):
        if s[i] in opening_brackets:
            opening_order.append(s[i])
        else:
            if len(opening_order) < 1:
                return "NO"
            elif opening_order[-1] == mapping_brackets[s[i]]:
                opening_order.pop(-1)
            else:
                return "NO"

    return "YES" if len(opening_order) == 0 else "NO"

print(isBalanced(s))
"""


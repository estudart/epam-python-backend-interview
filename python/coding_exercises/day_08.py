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
    
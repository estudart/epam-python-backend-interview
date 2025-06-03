"""
a = [1, 2, 3, 4, 3, 2, 1]
def lonelyinteger(a):
    checking_list = []
    duplicated_numbers_list = []
    non_duplicated_numbers_list = []
    for number in a:
        if number not in checking_list:
            checking_list.append(number)
        else:
            duplicated_numbers_list.append(number)

    for number in checking_list:
        if number not in duplicated_numbers_list:
            non_duplicated_numbers_list.append(number)

    return non_duplicated_numbers_list[0]
lonelyinteger(a)
"""

"""
arr = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]
def diagonalDifference(arr):
    number_of_rows = len(arr)
    left_diagonal_sum = 0
    right_diagonal_sum = 0

    for i in range(number_of_rows):
        left_diagonal_sum+=arr[i][i]
        right_diagonal_sum+=arr[i][-1-i]

    result = left_diagonal_sum - right_diagonal_sum
    if result < 0:
        result = result * (-1)

    print(result)

    return result
diagonalDifference(arr)
"""

"""
arr = [
    63, 54, 17, 78, 43, 70, 32, 97, 16, 94,
    74, 18, 60, 61, 35, 83, 13, 56, 75, 52,
    70, 12, 24, 37, 17, 0, 16, 64, 34, 81,
    82, 24, 69, 2, 30, 61, 83, 37, 97, 16,
    70, 53, 0, 61, 12, 17, 97, 67, 33, 30,
    49, 70, 11, 40, 67, 94, 84, 60, 35, 58,
    19, 81, 16, 14, 68, 46, 42, 81, 75, 87,
    13, 84, 33, 34, 14, 96, 7, 59, 17, 98,
    79, 47, 71, 75, 8, 27, 73, 66, 64, 12,
    29, 35, 80, 78, 80, 6, 5, 24, 49, 82
]

def countingSort(arr: list):
    print(len(arr))
    frequency_list = [0 for i in range(100)]

    for number in arr:
        frequency_list[number]+=1

    print(frequency_list)

    return frequency_list

countingSort(arr)
"""

"""
matrix = [
    [1, 2, 4, 4],
    [4, 2, 4, 4],
    [4, 2, 4, 4],
    [4, 2, 4, 4]
]

def flippingMatrix(matrix):
    total = 0
    n = len(matrix) // 2
    print(n)
    for i in range(n):
        for j in range(n):
            total += max(
                matrix[i][j],
                matrix[i][2*n - 1 - j],
                matrix[2*n - 1 - i][j],
                matrix[2*n - 1 - i][2*n - 1- j]
            )
    return total

flippingMatrix(matrix)
"""

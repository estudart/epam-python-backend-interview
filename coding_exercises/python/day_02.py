"""
arr = [1, 1, 0, -1, -1]
def plusMinus(arr):
    counts_list = [0, 0, 0]
    arr_lenght = len(arr)

    for n in arr:
        if n > 0:
            counts_list[0]+=1
        elif n < 0:
            counts_list[1]+=1
        else:
            counts_list[2]+=1

    for count in counts_list:
        print(f"{count/arr_lenght:.6f}")

plusMinus(arr)
"""

"""
arr = [1, 3, 5, 7, 9]
def miniMaxSum(arr: list):
    min_val = min(arr)
    max_val = max(arr)
    total_val = sum(arr)

    print(f"{total_val - max_val} {total_val - min_val}")

miniMaxSum(arr)
"""

"""
s = "01:45:00AM"
def timeConversion(s):
    if s[-2:] == "PM":
        if s[:2] == "12":
            new_time = f"{s[:-2]}"
        else:
            new_time = f"{int(s[0:2])+12}{s[2:-2]}"

    elif s[-2:] == "AM":
        if s[:2] == "12":
            new_time = f"00{s[2:-2]}"
        else:
            new_time = f"{s[:-2]}"
    print(new_time)
    return new_time

timeConversion(s)
"""
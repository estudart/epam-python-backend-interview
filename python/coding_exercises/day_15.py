"""
Find the longest substring within a string
Sliding window algorithm

test_string = "ericostudartabcdefghijklmnopqericostudagt"

def find_longest_unique_substring(string: str):
    start = 0
    seen = {}
    max_lenght = 0

    for i in range(len(string)):
        if string[i] in seen and seen[string[i]] >= start:
            start = seen[string[i]] + 1
        seen[string[i]] = i
        max_lenght = max(max_lenght, i - start + 1)

    return max_lenght, string[start:start+max_lenght]   

find_longest_unique_substring(test_string)
"""



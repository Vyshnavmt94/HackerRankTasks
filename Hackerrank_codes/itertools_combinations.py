"""
itertools.combinations(iterable, r)
This tool returns the  length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

Sample Code

>>> from itertools import combinations
>>>
>>> print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
>>>
>>> A = [1,1,3,3,3]
>>> print list(combinations(A,4))
[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]
Task

You are given a string .
Your task is to print all possible combinations, up to size , of the string in lexicographic sorted order.

Input Format

A single line containing the string  and integer value  separated by a space.

Constraints


The string contains only UPPERCASE characters.

Output Format

Print the different combinations of string  on separate lines.

Sample Input

HACK 2
Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK

"""

import itertools

if __name__ == "__main__":
    string, N = input().split()
    assert 0 < int(N) <= len(string), f"k != length of string"
    assert string.isupper() == True, f"String is not uppercase"
    for i in range(1, int(N)+1):
        for j in itertools.combinations(sorted(string), i):
            print("".join(j))
    # perms = list(itertools.combinations(string, int(N)))
    # perms = sorted([''.join(val) for val in perms])
    # string.extend(perms)
    # for val in string:
    #     print(val)

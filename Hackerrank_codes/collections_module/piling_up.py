"""
There is a horizontal row of  cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if  is on top of  then .

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print Yes if it is possible to stack the cubes. Otherwise, print No.

Example

Result: No

After choosing the rightmost element, , choose the leftmost element, . After than, the choices are  and . These are both larger than the top block of size .


Result: Yes

Choose blocks from right to left in order to successfully stack the blocks.

Input Format

The first line contains a single integer , the number of test cases.
For each test case, there are  lines.
The first line of each test case contains , the number of cubes.
The second line contains  space separated integers, denoting the sideLengths of each cube in that order.

Constraints




Output Format

For each test case, output a single line containing either Yes or No.

Sample Input

STDIN        Function
-----        --------
2            T = 2
6            blocks[] size n = 6
4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
3            blocks[] size n = 3
1 3 2        blocks = [1, 3, 2]
Sample Output

Yes
No
Explanation

In the first test case, pick in this order: left - , right - , left - , right - , left - , right - .
In the second test case, no order gives an appropriate arrangement of vertical cubes.  will always come after either  or .
"""

import collections


def pile_up_cubes(cubes):
    while cubes:
        big = cubes.popleft() if cubes[0] > cubes[-1] else cubes.pop()
        if not cubes:
            return "Yes"
        elif cubes[0] > big or cubes[-1] > big:
            return "No"


if __name__ == "__main__":
    T = int(input())
    assert 1 <= T <= 5
    d = collections.deque()
    for _ in range(T):
        d.clear()
        n = int(input())
        assert 1 <= n <= 10 ** 5
        d.extend(list(map(int, input().split())))
        print(pile_up_cubes(d))

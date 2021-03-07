"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.
"""


def check_number(num):
    if num >= 2 and num <= 10:
        return True

def check_array(arr):
    if not False in [True if a >= -100 and a <= 100 else False for a in arr]:
        return True

#k = kth largest number to be found
def runner_up(arr,k):
    for i in range(k):
        m = max(arr)
        arr = [a for a in arr if a != m]
    return m
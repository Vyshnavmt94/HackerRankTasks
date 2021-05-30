"""
There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. You like all the integers in set  and dislike all the integers in set . Your initial happiness is . For each  integer in the array, if , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.

Constraints



Input Format

The first line contains integers  and  separated by a space.
The second line contains  integers, the elements of the array.
The third and fourth lines contain  integers,  and , respectively.

Output Format

Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1
Explanation

You gain  unit of happiness for elements  and  in set . You lose  unit for  in set . The element  in set  does not exist in the array so it is not included in the calculation.

Hence, the total happiness is .
"""

if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    assert 1 <= n,m <= 10**5
    a = list(map(int, input().split()))
    like = set(map(int, input().split()))
    dislike = set(map(int, input().split()))
    assert all(1 <= i <= 10**9 for i in a) == True
    assert all(1 <= i <= 10 ** 9 for i in like) == True
    assert all(1 <= i <= 10 ** 9 for i in dislike) == True
    happiness = 0

    print(sum([(i in like) - (i in dislike) for i in a]))

    # for i in a:
    #     if i in like:
    #         happiness += 1
    #     elif i in dislike:
    #         happiness -= 1
    #     else:
    #         pass
    # print(happiness)
"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Sample Designs

    Size: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
Input Format

A single line containing the space separated values of  and .

Constraints

Output Format

Output the design pattern.

Sample Input

9 27
Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""


# N, M = map(int,input().split())
N = 7
M = N * 3
text = 'WELCOME'
pattern = '.|.'

#Top Cone
for i in range(int(N/2)):
    print((pattern*i).rjust(M-int(((N+1)/2)*3), '-') + pattern + (pattern*i).ljust(M-int(((N+1)/2)*3), '-'))

#Middle Belt
print(text.center(M, '-'))

#Bottom Cone
for i in range(int(N/2)-1,-1,-1):
    print(((pattern*i).rjust(M-int(((N+1)/2)*3), '-') + pattern + (pattern*i).ljust(M-int(((N+1)/2)*3), '-')))
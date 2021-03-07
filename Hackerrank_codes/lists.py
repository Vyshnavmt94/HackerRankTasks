"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Example





: Append  to the list, .
: Append  to the list, .
: Insert  at index , .
: Print the array.
Output:
[1, 3, 2]
Input Format

The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""


def insert(l, line):
    pos, e = line
    l.insert(pos, e)
    return l


def remove(l, line):
    e = line[0]
    l.remove(e)
    return l


def append(l, line):
    e = line[0]
    l.append(e)
    return l


def pop(l):
    l.pop()
    return l


def sort(l):
    l = sorted(l)
    return l


def reverse(l):
    l.reverse()
    return l


if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N):
        query, *line = input().split()
        line = list(map(int, line))
        if len(line) > 0:
            if query == 'insert':
                lst = insert(lst, line)
            elif query == 'append':
                lst = append(lst, line)
            elif query == 'remove':
                lst = remove(lst, line)
            else:
                raise ValueError(f"{query} not avaliable")
        else:
            if query == 'sort':
                lst = sort(lst)
            elif query == 'pop':
                lst = pop(lst)
            elif query == 'reverse':
                lst = reverse(lst)
            elif query == 'print':
                print(lst)
            else:
                raise ValueError(f"{query} not avaliable")

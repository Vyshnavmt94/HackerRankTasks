"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

Your task is to determine the winner of the game and their score.

Input Format

A single line of input containing the string .
Note: The string  will contain only uppercase letters: .

Constraints



Output Format

Print one line: the name of the winner and their score separated by a space.

If the game is a draw, print Draw.

Sample Input

BANANA
Sample Output

Stuart 12
"""

# def minion_game(string):
#     assert 0 < len(string) <= 10 ** 6
#     if any(w.islower() for w in string):
#         raise Exception
#     vowels = ["A", "E", "I", "O", "U"]
#     kevin_words = []
#     stuart_words = []
#     kevin_points = 0
#     stuart_points = 0
#     i = 0
#     while i < len(string):
#         for j in range(i+1, len(string)+1):
#             sub_string = string[i:j]
#             if sub_string[0] in vowels:
#                 # if sub_string not in kevin_words:
#                 kevin_words.append(sub_string)
#                 kevin_points += 1
#             else:
#                 # if sub_string not in stuart_words:
#                 stuart_words.append(sub_string)
#                 stuart_points += 1
#         i += 1
#     if kevin_points > stuart_points:
#         print(f"Kevin {kevin_points}")
#     elif kevin_points < stuart_points:
#         print(f"Stuart {stuart_points}")
#     else:
#         print("Draw")


def minion_game(string):
    assert 0 < len(string) <= 10 ** 6

    vowels = 'AEIOU'
    Stuart_score = 0
    Kevin_score = 0
    for i in range(len(string)):
        if string[i] in vowels:
            Kevin_score += len(string) - i
        else:
            Stuart_score += len(string) - i
    if Stuart_score == Kevin_score:
        print('Draw')
    if Stuart_score > Kevin_score:
        print('Stuart {}'.format(Stuart_score))
    if Stuart_score < Kevin_score:
        print('Kevin {}'.format(Kevin_score))


if __name__ == '__main__':
    s = "BANANA"
    minion_game(s)

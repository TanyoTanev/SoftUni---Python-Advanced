'''7. Balanced Parentheses
Given a sequence consisting of parentheses, determine whether the expression is balanced. A sequence of parentheses is balanced if every open
parenthesis can be paired uniquely with a closed parenthesis that occurs after the former. Also, the interval between them must be balanced.
You will be given three types of parentheses: (, {, and [.

{[()]} - This is a balanced parenthesis.

{[(])} - This is not a balanced parenthesis.

Input
Each input consists of a single line, the sequence of parentheses.
Output

For each test case, print on a new line "YES" if the parentheses are balanced.
Otherwise, print "NO". Do not print the quotes.

Constraints

1 ≤ lens ≤ 1000, where lens is the length of the sequence.
Each character of the sequence will be one of {, }, (, ), [, ].

Examples
Input
Output

{[()]}
YES

{[(])}
NO

{{[[(())]]}}
YES'''

from collections import deque
#string = input()

line =  deque(input())
check_line = deque()

i = 1

while line:
    symbol = line.popleft()
    if symbol == '{' or symbol == '(' or symbol == '[':
        check_line.append(symbol)
    elif symbol == '}' or symbol == ')' or symbol == ']':
        if check_line:
            check = check_line[-1]
        else:
            print('NO')
            i = 0
            break

        if  (symbol == '}' and check == '{') or (symbol == ')' and check == '(') or (symbol == ']' and check == '['):

             check_line.pop()
        else:
            print('NO')
            i = 0
            break



if i == 1:
    print('YES')




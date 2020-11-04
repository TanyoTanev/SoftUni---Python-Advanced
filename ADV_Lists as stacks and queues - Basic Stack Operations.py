'''1. Basic Stack Operations

Play around with a stack. You will be given an integer N representing the number of elements to push into the stack,
an integer S representing the number of elements to pop from the stack and finally an integer X, an element that you should look for in the stack.
If it's found, print "True" on the console. If it isn't, print the smallest element currently present in the stak.

Input
On the first line you will be given N, S and X, separated by a single space
On the next line you will be given N number of integers

Output
On a single line print either "True" if X is present in the stack, otherwise print the smallest element in the stack.
If the stack is empty, print "0".

Examples
Input
Output
Comments

5 2 13
1 13 45 32 4
True

We have to push 5 elements. Then we pop 2 of them. Finally, we have to check whether 13 is present in the stack. Since it is we print True.

4 1 666
420 69 13 666
13
'''


stack = []

commands = [int(i) for i in input().split(' ')]
push,  s_pop , x = commands

push = int(push)
s_pop = int(s_pop)
x = int(x)


numbers = [int(i) for i in input().split(' ')]

[ stack.append(i) for i in numbers ]
#print(stack)

[ stack.pop() for i in range(s_pop) ]
#print(stack)

if [i for i in stack if i == x ]:
     print(True)

elif stack:
    print(min(stack))
else:
    print(0)
'''3. Maximum and Minimum Element

You have an empty sequence, and you will be given N queries. Each query is one of these three types:
1 – Push the element x into the stack.
2 – Delete the element present at the top of the stack.
3 – Print the maximum element in the stack.
4 – Print the minimum element in the stack.

After you go through all the queries, print the stack in the following format:
"{n}, {n1}, {n2} …, {nn}"

Input
The first line of input contains an integer, N
The next N lines each contain an above-mentioned query. (It is guaranteed that each query is valid.)

Output
For each type 3 or 4 query, print the maximum/minimum element in the stack on a new line
Constraints
1 ≤ N ≤ 105
1 ≤ x ≤ 109
1 ≤ type ≤ 4

Examples
Input
Output

9
1 97
2
1 20
2
1 26
1 20
3
1 91
4
26
20
91, 20, 26

10
2
1 47
1 66
1 32
4
3
1 25
1 16
1 8
4
32
66
8
8, 16, 25, 32, 66, 47
'''

N = int(input())
stack =[]

for i in range(1, N+1):
    command = input().split(' ')

    if int(command[0]) == 1:
        stack.append(int(command[1]))
    elif int(command[0]) == 2 and stack:
        stack.pop()
    elif int(command[0]) == 3 and stack:
        print(max(stack))
    elif int(command[0]) == 4 and stack:
       print(min(stack))


#print(len(stack))

#list = []
#[list.append(str(stack.pop())) for i in range(len(stack))]
#print(list)
print(', '.join([str(x) for x in reversed(stack)]))


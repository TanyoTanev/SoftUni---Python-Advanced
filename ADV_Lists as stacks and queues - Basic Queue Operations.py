'''2. Basic Queue Operations

Play around with a queue. You will be given an integer N representing the number of elements to enqueue (add), an integer
S representing the number of elements to dequeue (remove) from the queue and finally an integer X, an element that you should look for in the queue.
If it is, print "True" on the console. If it's not print the smallest element currently present in the queue.
If there are no elements in the sequence, print 0 on the console.

Examples
Input
Output
Comments

5 2 32
1 13 45 32 4
True

We have to enqueue 5 elements. Then we dequeue 2 of them. Finally, we have to check whether 13 is present in the queue. Since it is we print True.

4 1 666
666 69 13 420
13

3 3 90
90 0 90
0'''

import collections
queue = collections.deque()

commands = input().split(' ')
push, pop, x = [int(i) for i in commands]

numbers = [int(i) for i in input().split(' ')]
#print(numbers)

[queue.append(i) for i in numbers]
#print(queue)
[queue.popleft() for i in range(pop)]
#print(queue)

if queue:
    if x in queue:
        print(True)
    else:
        print(min(queue))
else:
    print(0)
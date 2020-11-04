'''2.
Write a program that prints a set of elements. On the first line you will receive two numbers - n and m, which represent the lengths of
two separate sets. On the next n + m lines you will receive n numbers, which are the numbers in the first set, and m numbers,
which are in the second set. Find all the unique elements that appear in both of them and print them on separate lines (the order does not matter).
For example:
Set with length n = 4: {1, 3, 5, 7}
Set with length m = 3: {3, 4, 5}
Set that contains all the elements that repeat in both sets -> {3, 5}
'''

lenghts = input().split(' ')
len_first = int(lenghts[0])
len_second = int(lenghts[1])


set1 = list()
set2 = list()

for i in range(len_first+len_second):
    if i < len_first:
        set1.append(input())
    else:
        set2.append(input())

set1 = set(set1)
set2 = set(set2)

set3 = set1.intersection(set2)
for number in (set3):
    print(number)
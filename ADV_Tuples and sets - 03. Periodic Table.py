'''3. 3.	Periodic Table
Write a program that keeps all the unique chemical elements. On the first line you will be given a number n - the count of input lines
that you are going to receive. On the next n lines, you will be receiving chemical compounds, separated by a single space.
Your task is to print all the unique ones on a separate lines (order does not matter):
'''
count = int(input())
l1 = list()

for i in range(count):
   string = input().split(' ')
   for j in range(len(string)):
       l1.append(string[j])

set1 = set(l1)
#print(l1)

for element in set1:
    print(element)
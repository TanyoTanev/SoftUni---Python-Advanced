'''1.Unique usernames
Write a program that reads from the console a sequence of N usernames and keeps a collection only of the unique ones.
On the first line you will be given an integer N. On the next N lines, you will receive one username per line. Print the collection on the console
(the order does not matter):
'''

number = int(input())
names = list()

for i in range(number):
    names.append(input())

names=set(names)

for name in names:
    print(name)


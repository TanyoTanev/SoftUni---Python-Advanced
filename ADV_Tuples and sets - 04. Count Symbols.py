'''04. Count Symbols

4.	Count Symbols
Write a program that reads some text from the console and counts the occurrences of each character in it. Print the results in alphabetical
(lexicographical) order.
'''

string = input()

d1 = dict()

for i in range(len(string)):

    if string[i] not in d1:
        d1[string[i]] = []
        d1[string[i]] = 1
    else:
        d1[string[i]]+=1
#
sorted_d1 = dict(sorted(d1.items(), key=lambda x: x[0], reverse=False ))
#print(sorted_d1)
#print(d1['f'])

for key, value in sorted_d1.items():
    print(f"{key}: {value} time/s")

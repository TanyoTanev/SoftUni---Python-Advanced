'''2. Number Classification
Using list comprehension write a program that receives numbers separated by comma and space &quot;, &quot; and prints
all the positive, negative, even and odd numbers on separate lines as shown below.
Note: Zero is counted for a positive number
'''


'''numbers_list = list(map(int, input().split(', ')))
#print(numbers_list)
positive = []
negative = []
even = []
odd = []

for i in numbers_list:
    if i >= 0:
        positive.append(str(i))
    else :
        negative.append(str(i))
    if i % 2 == 0:
        odd.append(str(i))
    else: #i // 2 > 0:
        even.append(str(i))
print(f"Positive: {', '.join(positive)}"'\n'f"Negative: {', '.join(negative)}"'\n'f"Even: {', '.join(even)}"'\n'f"Odd: {', '.join(odd)}")'''

positive = []
negative = []
even = []
odd = []

def check_number(i,positive, negative, even, odd):

    if i >= 0:
        positive.append(str(i))
    else:
        negative.append(str(i))
    if i % 2 == 0:
        even.append(str(i))
    else:  # i // 2 > 0:
        odd.append(str(i))
    return positive, negative, even, odd


def print_lists_of_numbers(positive, negative, even, odd):

 print(f"Positive: {', '.join(positive)}"'\n'f"Negative: {', '.join(negative)}"'\n'f"Even: {', '.join(even)}"'\n'f"Odd: {', '.join(odd)}")

positive1 = [check_number(i,positive, negative, even, odd) for i in (list(map(int, input().split(', '))))]
#print(positive1)
positive, negative, even, odd = positive1[0]
print_lists_of_numbers(positive, negative, even, odd)
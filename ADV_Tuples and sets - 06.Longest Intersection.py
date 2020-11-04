'''6.
Write a program that finds the longest intersection. You will be given a number N. On the next N lines you will be given two ranges in the format:
"{first_start},{first_end}-{second_start},{second_end}". Find the intersection of these two ranges and save the longest one of all N intersections.
At the end print the numbers that are included in the longest intersection and its length in the format:
"Longest intersection is {longest_intersection} with length {length_longest_intersection}"
Note: in each 2 ranges there will always be intersection. If there are two equal intersections, print the first one.
'''

count = int(input())
set_4 = set()

for i in range(count):
    command = input().split('-')
    first_beg, first_end = command[0].split(',')
    second_beg, second_end = command[1].split(',')
    set_1 = set(range(int(first_beg), int(first_end)+1))
    set_2 = set(range(int(second_beg), int(second_end) + 1))
    set_3 = set_1.intersection(set_2)
    longest = len(set_3)
    if len(set_3) > len(set_4):
        set_4 = set_3


#print(set_1)
#print(set_4)

print(f"Longest intersection is {list(set_4)} with length {len(set_4)}")
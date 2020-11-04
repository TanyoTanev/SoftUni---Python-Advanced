'''
6. Bunker
Using comprehension write a program that finds all the amount of all items in a bunker and their average quantity.
On the first line you will be given all the categories of items in the bunker, then you will be given a number (n). On
the next &quot;n&quot; lines you will be given items in the following format: &quot;{category} - {item_name} -
quantity:{item_quantity};quality:{item_quality}&quot;. Store that information, you will need it later. After
you received all the inputs, print the total amount of items (sum the quantities) in the format: &quot;Count of
items: {count}&quot;. After that print the average quality of all items in the format: &quot;Average quality:
{quality - formatted to the second digit}&quot;. Finally, print all of the categories with the items on
separate lines in it in the format: &quot;{category} -&gt; {item1}, {item2}…&quot;. For more clarification, see the
example below.
'''

categories = input().split(', ')
N = int(input())
bunker = {category: {} for category in categories}

for _ in range(N):
    command = input().split(' - ')

    items_info = command[2].split(';')
    quantity = int(items_info[0].split(':')[1])
    quality = int(items_info[1].split(':')[1])

    category = command [0]
    item = command[1]

    if command[0] in bunker:

        bunker[category][item] = {'quantity': quantity, 'quality': quality}

#print(bunker)

count_quantity = [ bunker[key][y]['quantity'] for key in bunker for y in bunker[key] ]
count_quality = [ bunker[key][y]['quality'] for key in bunker for y in bunker[key] ]

print( f"Count of items: {sum(count_quantity)}")
print(f"Average quality: {sum(count_quality)/len(bunker):.2f}")
[print(f"{key} -> {', '.join(bunker[key].keys())}") for key in bunker.keys()]
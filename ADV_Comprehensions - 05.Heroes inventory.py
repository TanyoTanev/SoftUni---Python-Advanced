'''
5. Heroes Inventory
Using comprehension write a program that receives some hero names, items that need to be added in their
inventory (item name and item cost) and then prints for each hero the total amount of items and the total cost of
them.
Input
 On the first line you will receive the names of the heroes separated by comma and space &quot;, &quot;
 On the next lines until the command &quot;End&quot;, you will be given items with their cost in the format &quot;{name}-
{item}-{cost}&quot;. If an item repeats in a hero inventory, ignore it
Output
 For each hero print his name, the total items and the total cost of the items in the format: &quot;{name} -&gt;
Items: {items_count}, Cost: {items_cost}&quot;
'''

command = input().split(', ')
inventory = { key:{'items':[], 'cost':[]} for key in command }
#print(inventory)
#print(inventory[command[0]]['items'])


while True:
    command = input().split('-')
    if command[0] == 'End':
        break



    if len(inventory[command[0]]['items']) and command[1] not in inventory[command[0]]['items']:
      inventory[command[0]]['items'].append(command[1])
      inventory[command[0]]['cost'].append(int(command[2]))
      #print(inventory[command[0]]['items'])

    elif len(inventory[command[0]]['items']) < 1:
      inventory[command[0]]['items'] = [command[1]]
      inventory[command[0]]['cost']= [int(command[2])]

#print(inventory)


[print(f" {key} -> Items: {len(inventory[key]['items'])}, Cost: {sum(inventory[key]['cost'])}") for key in inventory.keys()   ]


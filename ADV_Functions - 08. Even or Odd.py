'''Even or Odd
Create a function called even_odd that can receive different amount of numbers and a command at the end. The command can be "even" or "odd".
Filter the numbers depending on the command and return them in a list. Submit only the function in the judge system.

Examples
Test Code
Output

print(even_odd(1, 2, 3, 4, 5, 6, "even"))

[2, 4, 6]

print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

[1, 3, 5, 7, 9]
'''

def even_odd( *args ):
    '''command = args[-1]
    list_1 = list(args[:-1])
    list_2 = []
    if command == "even":
        for i in list_1:
            if i%2==0:
                list_2.append(i)
    elif command == "odd":
        for i in list_1:
            if i % 2 == 1:
                list_2.append(i)'''

    command = args[-1]
    x = 0 if command == "even" else 1
    return [num for num in args[:-1] if num%2 ==x]

    #return list_2


#print(even_odd( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,"odd"))
print(even_odd( 1, 2, 3, 4, 5, 6, "even"))
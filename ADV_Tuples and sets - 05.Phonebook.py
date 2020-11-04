'''5. Phonebook
Write a program that receives some info from the console about people and their phone numbers.
You are free to choose the way the data is entered; each entry should have just one name and one number (both strings).
If you receive a name that already exists in the phonebook, simply update its number.
After filling this simple phonebook, upon receiving the command "search", your program should be able to perform a search of a contact by name and
print her details in format "{name} -> {number}". In case the contact isn't found, print "Contact {name} does not exist." Examples:
'''

phonebook = dict()
check = 0

while True:



    if check == 1:
        break

    command = input().split('-')

    if command[0].isdigit():

       count = int(command[0])
       for i in range(count):
           search_name = input()
           #if search_name == 'stop':
             #  break
           if search_name in phonebook:
                print(f"{search_name} -> {phonebook[search_name]}")
           else:
                print(f"Contact {search_name} does not exist.")
           if count - 1 == i:
               check = 1


    elif command[0] not in phonebook: #and not command[0].isdigit():
        phonebook[command[0]] = []
        phonebook[command[0]] = command[1]


#print(phonebook)



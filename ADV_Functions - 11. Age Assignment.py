'''11.Age Assignment
Create a function called age_assignment that receives different amount of names and then different amount of key-value pairs. The key will
be a single letter (first letter of a name), and the value a number (age). For each name, find its first letter in the key-value pairs and
assign the age to the persons name. At the end return a dictionary with all the names and ages as shown in the example. Submit only the
function in the judge system.

Examples
Test Code
Output

	print(age_assignment("Peter", "George", G=26, P=19))
{'Peter': 19, 'George': 26}

	print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
{'Amy': 22, 'Bill': 61, 'Willy': 36}
'''

def age_assignment(*args,**kwargs):
    result = {}
    for person in args:
        result[person] = kwargs[person[0]]

    return result

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
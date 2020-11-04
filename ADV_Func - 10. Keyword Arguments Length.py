'''10.Keyword Arguments Length

Create a function called kwargs_length which can receive different amount of keyword arguments and returns their length. Submit only the
function in the judge system.

Examples
Test Code
Output
	dictionary = {'name': 'Peter', 'age': 25}

	print(kwargs_length(**dictionary))
2
'''

def kwargs_length(**kwargs):
    return len(kwargs)


dictionary = {'name': 'Peter', 'age': 25, 'height':180}

print(kwargs_length(**dictionary))
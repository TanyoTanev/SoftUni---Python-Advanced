'''4. Capitals
Using dictionary comprehension write a program that receives countries on the first line separated by comma and
space &quot;, &quot; and their corresponding capital cities on the second line (again separated by comma and space &quot;, &quot;)
and prints each country with their capital on a separate line in the format: &quot;{country} -&gt; {capital}&quot;
'''
#countries = input().split(', ')
#capitals = input().split(', ')

dictionary = {key:value for key, value in zip(list(input().split(', ')), list(input().split(', '))) }
#print(dictionary)
#print('\n'.join([(f"{key} -> {value}") for key, value in dictionary]))

print('\n'.join([(f"{key} -> {value}") for key,value in dictionary.items()]))
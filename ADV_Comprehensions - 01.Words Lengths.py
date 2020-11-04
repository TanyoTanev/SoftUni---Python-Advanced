'''
Using list comprehension, write a program that receives some strings separated by comma and space &quot;, &quot; and
prints on the console each string with its length in the format: &quot;{first_str} -&gt; {first_str_len},
{second_str} -&gt; {second_str_len}…&quot;

'''

#string_list = input().split(', ')
#list1 = []
#for i in range(len(string_list)):

  #  list1.append(f"{string_list[i]} -> {len(string_list[i])}")
#print(', '.join(list1))
#print([(f"{i} -> {len(i)}") for i in (input().split(', '))])

print(', '.join([(f"{i} -> {len(i)}") for i in (input().split(', '))]))
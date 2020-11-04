'''12.Recursion Palindrome
Write a recursive function called palindrome which will receive a word and an index (always 0). Implement the function, so it returns "{word}
 is a palindrome" if the word is a palindrome and "{word} is not a palindrome" if the word is not a palindrome using recursion. Submit only
 the function in the judge system.

Examples
Test Code
Output

	print(palindrome("abcba", 0))
abcba is a palindrome

	print(palindrome("peter", 0))
peter is not a palindrome
'''

def palindrome(word, idx):
    second_idx = len(word) - 1 - idx

    if idx == len(word)//2 :
        return f"{word} is a palindrome"

    if word[idx] == word[second_idx]:
         return palindrome(word, idx+1)
    else:
        return f"{word} is not a palindrome"
    
print(palindrome("peter", 0))
print(palindrome("abcba", 0))
#write a function remove vowel (text) that remove all vowel from a given string
def remove_vowel(text):
    vowels="aeiouAEIOU"
    return ''.join(char for char in text if char not in vowels)

text=input("enter a string:")
print("string without vowels is ")
removed = remove_vowel(text)
print(removed)
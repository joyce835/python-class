#write a function count_upper(text)
# that count the number of uppercase letter in a string.

def count_uppercase_letters(text):
    return sum ( 1 for word in text if word.isupper())
text=input("enter your text:")
print(count_uppercase_letters(text))
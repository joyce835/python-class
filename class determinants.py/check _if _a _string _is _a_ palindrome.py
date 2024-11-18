#check if a word reads the same back word as forward
def is_palindrome(word):
    word =input("enter your word:")
    if word == word:
        print(True)
    else:
        print(False)
print(is_palindrome("radar"))
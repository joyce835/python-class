#write a function is_strong_password(password) that check if a password is strong
#at least 8 characters ,including letters,numbers and special characters

def is_strong_password(password):
    for i in range(len(password)):
        if password[i].isupper():
            has_upper=True
        elif password[i].islower():
            has_lower=False
        elif password[i].isdigit():
            has_special=True
        elif not password[i].digit():
            has_digit=True
            if len(password)>= 8 and has_upper and has_lower and has_digit and has_special:
                print(True)
            else:
                print(False)
password=input("enter your password:")
print(f"is strong password?{password}")
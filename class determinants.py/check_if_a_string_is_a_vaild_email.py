# write a function is_vaild_email(email) that checks if a string is a vaild email address

def is_vaild_email(email):
    if "@" in email and "." in email:
        return "True"
    else:
        return "False"

email=input("enter your email address:")
valid = is_vaild_email(email)
print(f"is your email vaild? {valid}")
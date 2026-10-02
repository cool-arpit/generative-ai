# WAP to check whether the entered password is strong or weak.
def password_strength_checker(password):

    if len(password) < 8:
        print(f"The entered password {password} is weak")

    elif not any (char.islower() for char in password):
        print(f"The entered password {password} is weak")

    elif not any (char.isupper() for char in password):  
        print(f"The entered password {password} is weak")

    elif not any (char.isdigit() for char in password):  
        print(f"The entered password {password} is weak")

    elif not any(char in "!@#$%&*()" for char in password):
        print(f"The entered password {password} is weak")

    else:
        print(f"The entered password {password} is strong")

password = input("ENTER PASSWORD :")
password_strength_checker(password)







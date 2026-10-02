# WAP to check whether the given string is palindrome or not 
# Palindrome = same from both the direction , example : mom , dad , wow
def palindrome (string):
    string_value = string.lower().replace(" " , "")
    
    if string_value == string_value[::-1]:
        print("THE GIVEN STRING IS A PALINDROME")
    else:
        print("THE GIVEN STRING IS NOT THE PALINDROME ")

value = input("ENTER THE STRING: ")
palindrome(value)
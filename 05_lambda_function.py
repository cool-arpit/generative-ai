#LAMBDA : These are one liner functions defined by lambda keyword.
'''THEY CAN HAVE ANY NUMBER OF ARGUMENTS BUT ONLY ONE EXPRESSION OR ONLY ONE LOGIC
THEY ARE USED FOR SHORT OPERATIONS OR AS ARGUMENTS TO HIGHER ORDER FUNCTION
IT CAN BE TREATED AS A FUNCTION WITHOUT A NAME AND THEY DON'T EVEN REQUIRE A RETURN STATEMENT
'''

# WAP to calculate square of a given number
function_square = lambda x : x**2
num = int(input("ENTER THE NUMBER : "))
print(f"The square of given number is : " , function_square(num))
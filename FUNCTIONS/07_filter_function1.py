# Filter function is going to retrieve only those items which are meeting a certain condition in an iterable.
#Filter function constructs an iterator from elements of an iterable for which a condition remains true or for which a function returns true.

# syntax for filter function :
#     list(filter(function, iterable))

# WAP to retrieve only even numbers from list
def even_function(value):
    if value %2 == 0:
        return True

lists = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list(filter(even_function,lists)))
 

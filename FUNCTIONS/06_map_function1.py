# WAP TO SQUARE ALL ELEMENTS OF A LIST 
# list = [1 ,2 , 3 , 4, 5, 6, 7, 8, 9, 10]
# result =[]
# def square(list):
#     for item in list:
#         square_item = item**2
#         result.append(square_item)
#     print(result)
# square(list)

#USING MAP AND LAMBA FUNCTION

print(list(map(lambda x : x**2 , [1,2,3,4,5,6,7,8,9,10])))
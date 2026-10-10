# open() --> opening your file 
# First parameter --> file Name 
# Second parameter --> Mode 
# Mode --> it decides the way in which we are working with this file 
# Mode : r= reading the content from file 
#        w= writing the content into the File 
#        r+ = read the content first and then writing the content into the file 
#        w+ = writing the content first and then reading it 
#        a = append mode

f = open("FILE HANDLING/example.txt" , "r")
content = f.read()
print(content)
f.close()
print("\n\n")
#FOR WRITING THE CONTENT INTO THE FILE 
# w mode = it overwrites the content into the text file 
# append mode  = it adds the data from the end of the file 

f = open("FILE HANDLING/example.txt" , "a")
f.write("Hello , we are now writing the content into the file after end")
f.close()



#with command : It will be used for first of all opening the file as a object and there is no requirement for closing the file as well 

with open("FILE HANDLING/example.txt" , "r") as f:
    content = f.read()
    print(content)

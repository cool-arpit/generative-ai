# Read the content from the example.txt file and then writing that content into another file

with open("FILE HANDLING/example.txt" , "r") as source:
    content = source.read()
with open("FILE HANDLING/destination.txt" , "w") as destination:
    destination.write(content)
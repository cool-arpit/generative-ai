# Write the content into our file line by line --> writelines()
        # lines = ["First line\n" , "Second line\n" , "Third line\n"]
        # with open("FILE HANDLING/example.txt" , "w") as data:
        #     data.writelines(lines)

# Mode --> write the content into the binary file --> wb
# Mode --> read the content from the binary file --> rb

data = b"\x00\x01\x02\x03\x04"
with open("FILE HANDLING/example.txt" , "wb") as binary_data :
    binary_data.write(data)

with open("FILE HANDLING/example.txt" , "rb") as binary_read :
    binary_content = binary_read.read()
    print(binary_content)
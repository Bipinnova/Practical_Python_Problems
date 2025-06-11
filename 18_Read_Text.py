#  Write a Python program to read an entire text file.

# Ask the user for the file name
file_name = input("Enter the file name: ")

# Open the file in read mode
file = open(file_name, 'r')

# Read the entire content
content = file.read()

# Print the content
print("File Content:\n")
print(content)

# Close the file
file.close()

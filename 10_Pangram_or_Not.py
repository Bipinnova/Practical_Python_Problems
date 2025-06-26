# Write the program for the following: ( by using list) 
# A. A pangram is a sentence that contains all the letters of the English alphabet at least once,
# for example: The quick brown fox jumps over the lazy dog. 
# Your task here is to write a function to check a sentence to see if it is a pangram or not.

def pangram(str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in alphabet:
        if i not in str.lower():
            return False
        return True

str = 'The quick brown fox jumps over the lazy dog. '
if pangram(str) == True:
    print("It a pangram")
else:
    print("not pangram")


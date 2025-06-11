# A. Write a function that takes a character (i.e. a string of length 1) and 
# # returns True if it is a vowel, False otherwise.

char = input("Please enter the character: ")

def vowel(char):
    vowel_lst = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in char:
        if i in vowel_lst:
            print('True')
        else:
            print('False')
            
vowel(char)
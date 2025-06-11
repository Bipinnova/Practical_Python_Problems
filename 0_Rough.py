
# Write the program for the following: ( by using list) 
# A. A pangram is a sentence that contains all the letters of the English alphabet 
# at least once, for example: The quick brown fox jumps over the lazy dog. 
# Your task here is to write a function to check a sentence to see if it is a 
# pangram or not.


def pangram(sentence):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for i in alphabets:
        if i not in sentence.lower():
            return False
        return True

sentence = 'The quick brown fox jumps over the lazy dog. '
if pangram(sentence) == True:
    print('pangram')
else:
    print('Not pangram')
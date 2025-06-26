# # A. Write a function that takes a character (i.e. a string of length 1) and 
# # # returns True if it is a vowel, False otherwise.
# 
char = input("Please enter the character: ")

def vowel(char):
    vowel_lst = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in char:
        if i in vowel_lst:
            print('True')
        else:
            print('False')
            
vowel(char)
# 
# def is_vowel(char):
#     vowels = "aeiouAEIOU"
#     return char in vowels
# 
# def get_valid_string():
#     while True:
#         user_input = input("Please enter one or more alphabet characters: ").strip()
#         if user_input.isalpha():
#             return user_input
#         else:
#             print("❌ Invalid input. Please enter only alphabetic characters (a-z or A-Z).")
# 
# # Main program
# user_string = get_valid_string()
# 
# for ch in user_string:
#     if is_vowel(ch):
#         print(f"✅ '{ch}' is a vowel.")
#     else:
#         print(f"❌ '{ch}' is not a vowel.")

# Write a function that reverses the user defined value. 

def reverse(value):
    return str(value)[::-1]

# users = int(input("Enter the number or string which you want to reverse: "))

users = input("Enter the number or string which you want to reverse: ").strip()


reverse_result = reverse(users)
print("Here the reverse Value is: ",reverse_result)


# 
# # user defined value ko reverse karne ke liye function bana rahe hain
# def reverse(value):  # reverse naam ka function define kiya gaya hai jo ek value lega
#     return str(value)[::-1]  # value ko pehle string me convert kar ke slicing se reverse kar rahe hain
# 
# # user se input le rahe hain jo reverse karna hai
# users = input("Enter the number or string which you want to reverse: ").strip()  # user se koi string ya number le rahe hain aur strip() se extra spaces hata rahe hain
# 
# # function ko call karke reverse value nikal rahe hain
# reverse_result = reverse(users)  # reverse function ko call kar ke result ko reverse_result variable me store kar rahe hain
# 
# # reversed value ko print kar rahe hain
# print("Here the reverse Value is: ", reverse_result)  # final reversed value ko print kar rahe hain

# Write the program for the following: ( by using list) 
# A. Write a program that takes two lists and returns True if they have at least 
# one common member.


#method 1 - ---  O(n) O(n)
# def lst(lst_1, lst_2):
#     set_1 = set(lst_1)
#     for i in lst_2:
#         if i in set_1:
#             return True
#     return False


# Method --- 2       ----------     time O(n * m) space O(1)
# def lst(lst_1, lst_2):
#     for i in lst_1:
#         for j in lst_2:
#             if i == j:
#                 return True
#     return False
    


lst_1 = [1,2,3,4,6,6,7]
lst_2 = [5,6,7,8,9,6,7]
result = lst(lst_1, lst_2)
print(result)
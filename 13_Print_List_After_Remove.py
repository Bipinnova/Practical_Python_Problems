# Write a Python program to print a specified list after removing the 0th, 2nd, 4th 
# and 5th elements.



#Method - 1 ---- hard code for data input

def Specified_lst(data):
    remove_lst = {0,2,4,5}
    checkList = [
        value for index,value in enumerate(data)
        if index not in remove_lst
        ]
    return checkList
 
#this is hard code

data_1 = [3,'d','sdsa','sdfcsadfe',23,54,'f','re','sfg',45,67,87]

result = Specified_lst(data_1)
print(result)
    
    
#Method - 2 ---- taking list input also from user


def specidied_lst(data):
    remove_lst = {0,2,4,5}
    checklist = [
        value for index,value in enumerate(data)
        if index not in remove_lst
        ]
    return checklist

user_input = input("ENter the data in commas separated: ")
original_lst = [item.strip() for item in user_input.split(',')]    # this both are the user inpur convert in list

result = specidied_lst(original_lst)
print("Original List:", original_lst)
print("Modified List:", result)



        
        
        
        
        

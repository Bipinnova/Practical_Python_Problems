# Take a list, say for example this one: 
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
# and write a program that prints out all the elements of the list that are less than 5.


# method : 1
def want_element(a):
    for i in a:
        if i <= 5:
            print(i)



# # method: 2
# def want_element(a):
#     b = []
#     for i in a:
#         if i <= 5:
#             b.append(i)
#     return b


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
want_element(a)
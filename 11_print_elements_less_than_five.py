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

# Both methods are O(n) in time complexity  where n is the length of the list.
# Method 1 is space-efficient (O(1) extra space).
# Method 2 uses O(k) extra space (where k is the number of elements ≤ 5).

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
want_element(a)
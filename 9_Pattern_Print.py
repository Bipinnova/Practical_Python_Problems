#  Define a procedure histogram() that takes a list of integers and prints a 
# histogram to the screen. For example, histogram([4, 9, 7]) should print the 
# following: 
# **** 
# ********* 
# *******

def pattern(n):
    for i in n:
        print("* " * i )        


n = [4,9,7]
dsa = pattern(n)
# f.  Write a recursive function to print the factorial for a given number. 
#

def recur(n):
    if n == 0:
        return 1
    return n * recur(n-1)


n = int(input("Enter the number: "))
fac_recur = recur(n)
print(fac_recur)
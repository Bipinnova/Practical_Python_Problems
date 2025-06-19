# # f.  Write a recursive function to print the factorial for a given number. 
# #
# 
# def recur(n):
#     if n == 0:
#         return 1
#     return n * recur(n-1)
# 
# 
# n = int(input("Enter the number: "))
# fac_recur = recur(n)
# print(fac_recur)


def recur(n):
    if n == 0:
        return 1
    return n * recur(n - 1)

def get_valid_number():
    while True:
        user_input = input("Enter a non-negative integer: ").strip()
        if user_input.isdigit():
            return int(user_input)
        else:
            print("❌ Invalid input. Please enter a non-negative integer.")

if __name__ == "__main__":
    n = get_valid_number()
    factorial = recur(n)
    print(f"✅ Factorial of {n} is: {factorial}")

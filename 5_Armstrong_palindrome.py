# Armstrong number check karne ke liye function define kiya gaya hai
def armstrong(num): 
    total = 0  # sum store karne ke liye variable
    temp = num  # original number ko ek temporary variable me store kiya
    ORDER = len(str(temp))
    
    while temp > 0:  # jab tak number 0 se bada hai loop chalega
        digit = temp % 10  # last digit nikal rahe hain
        total += digit ** ORDER  # digit ka cube karke total me jod rahe hain (3-digit ke liye). Agar n-digit ho to digit ** len(str(num)) use karte
        temp //= 10  # last digit hata rahe hain number se (integer division)

    if num == total:  # agar original number aur calculated total barabar hain to Armstrong hai
        print(num, "is an Armstrong number") 
    else: 
        print(num, "is not an Armstrong number")
        
# User se input le rahe hain Armstrong check ke liye
num = int(input("Enter a number to check if it is an Armstrong number: ")) 
armstrong(num)  # Armstrong function call kar rahe hain





# Palindrome number check karne ke liye function define kiya gaya hai
def palindrome(num): 
    original = num  # original number ko store kar rahe hain
    reverse = 0  # reverse number banane ke liye variable

    while num != 0:  # jab tak number 0 nahi ho jaata loop chalega or num >0:
        reverse = reverse * 10 + num % 10  # reverse number banana: har digit ko reverse me jodte ja rahe hain
        num //= 10  # last digit hata rahe hain number se

    if original == reverse:  # agar original aur reverse barabar hain to palindrome hai
        print(original, "is a Palindrome number") 
    else: 
        print(original, "is not a Palindrome number") 


# User se input le rahe hain Palindrome check ke liye
num = int(input("Enter a number to check if it is a Palindrome: ")) 
palindrome(num)  # Palindrome function call kar rahe hain

# 2.Enter the number from the user and depending on whether the number is
# even or odd, print out an appropriate message to the user.

# user se number input lene ke liye
num = int(input("Koi bhi number daaliye: "))  # input se value le rahe hain aur int() se number me badal rahe hain

# even ya odd check karne ke liye condition laga rahe hain
if num % 2 == 0:  # agar number ko 2 se divide karne par remainder 0 aaye to woh even number hota hai
    print("Yeh ek even (samaan) number hai.")  # agar condition true hai to even number ka message print karte hain
else:  # agar upar wali condition false ho jaaye
    print("Yeh ek odd (visam) number hai.")  # odd number hone par yeh message print hota hai

# 1. Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will
# turn 100 years old.

# from datetime import datetime
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# cur_year = datetime.now().year
# ave = int(100 - age)
# print(ave)
# add_to_cur_year = cur_year + ave
# print(add_to_cur_year)
# 
#

from datetime import datetime  # datetime module se datetime class import kar rahe hain taaki current year le saken

def main():  # main function define kar rahe hain jahan se program start hoga

    name = input("Enter your name: ").strip()  # user se naam le rahe hain aur strip() se extra spaces hata rahe hain

    while True:  # infinite loop laga rahe hain taaki valid age milne tak input le sakein

        try:  # try block use kar rahe hain taaki agar user galat input de to program crash na ho

            age = int(input("Enter your age: ").strip())  # user se age le rahe hain aur usse int me convert kar rahe hain

            if age < 0 or age > 150:  # age ko valid range me check kar rahe hain (0 se 150 ke beech)

                print("Please enter a valid age between 0 and 150.")  # agar age galat ho to user ko bataya ja raha hai

                continue  # galat age milne par loop ko dobara start karne ke liye continue use kar rahe hain

            break  # jab age valid ho jaye to loop se bahar nikalne ke liye break use kar rahe hain

        except ValueError:  # agar user number ke alawa kuch aur de de to us error ko handle karne ke liye

            print("Invalid input. Please enter a number for your age.")  # user ko galat input dene par message dikhate hain

    current_year = datetime.now().year  # datetime class ka use karke current year nikal rahe hain

    year_when_100 = current_year + (100 - age)  # user 100 saal ka kab hoga us year ka calculation kar rahe hain

    print(f"\nHello {name}, you will turn 100 years old in the year {year_when_100}.")  # final message user ko print kar rahe hain

if __name__ == "__main__":  # yeh check karta hai ki file directly run ho rahi hai ya import ki gayi hai

    main()  # agar file directly run ho rahi hai to main function call hota hai


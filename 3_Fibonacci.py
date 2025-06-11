# # # 3. Write a program to generate the Fibonacci series.
# 
# # def fib(n):
# #     serious = []
# #     a, b = 0,1
# #     for i in range(n):
# #         serious.append(a)
# #         a, b = b, a + b
# #     return serious
# # 
# # n = int(input("Enter the number of fibonacci series you want: ").strip())
# # febo = fib(n)
# # print("Fibonacci series: ",*febo)
# 
# 
# Fibonacci series generate karne ke liye function bana rahe hain
def fib(n):  # fib naam ka function define kiya gaya hai jo n terms ki series return karega
    serious = []  # ek khaali list banayi gayi hai jisme Fibonacci numbers store kiye jaayenge
    a, b = 0, 1  # pehle do numbers initialize kiye jaate hain Fibonacci ke (0 aur 1)
    
    for i in range(n):  # loop chalate hain n baar tak jahan har baar ek naya number add hoga
        serious.append(a)  # current number ko list me add karte hain
        a, b = b, a + b  # agla number banane ke liye values ko update karte hain (swapping)
    
    return serious  # final list return karte hain jisme puri Fibonacci series hoti hai

# user se number le rahe hain ki kitne terms chahiye
n = int(input("Enter the number of fibonacci series you want: ").strip())  # input le rahe hain aur usse number me badal rahe hain

# function call karke series generate kar rahe hain
febo = fib(n)  # fib function ko call karke result ko febo naam ke variable me store kar rahe hain

# series ko print kar rahe hain
print("Fibonacci series: ", *febo)  # series ko print kar rahe hain using unpacking (*febo) taki list ke numbers space se print ho

#
from datetime import date
print("welcome to my python GUI calculator".title())
name = input("Enter Your Name: ")
print(f"welcome {name} which operation do you want perform".title())
print("[1]add\n[2]subtract\n[3]multiply\n[4]divide\n[5]reminder".upper())
def add_function(first_number,second_number):
    add = first_number + second_number
    return add


choice = input()
if choice == 1 :
    print("welcome to add wizard",name)
    first_num = input("Enter first num ".title())
    to_int = int(first_num)
    # print("enter second num".title())
    

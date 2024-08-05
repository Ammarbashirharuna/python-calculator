from datetime import date
print("welcome to my python GUI calculator".title())
name = input("Enter Your Name: ")
print(f"welcome {name} which operation do you want perform".title())
print("[1]add\n[2]subtract\n[3]multiply\n[4]divide\n[5]reminder".upper())
##functions to handle mathmatic operation
def add_function(first_number,second_number):
    add = first_number + second_number
    return add
def subtract_function(first_num,second_num):
    subtract = first_num - second_num
    return subtract
def multiply_function(first_num,second_num):
    multiply = first_num * second_num
    return multiply
def divide_function(first_num,second_num):
    devide = first_num / second_num
    return devide
def reminder_function(first_num,second_num):
    reminder = first_num % second_num
    return reminder
#giving choice to a user
choice = input()
to_num = int(choice)
if to_num == 1 :
    print("welcome to add wizard",name)
    first_num = input("Enter first num ".title())
    to_int = int(first_num)
    second_num = input("enter second num ".title())
    to_integer = int(second_num)
    print(f"the sum of your numbers is {add_function(to_int,to_integer)}")
elif to_num == 2:
    print("welcome to subtract wizard".title())
    first_num  = input("enter first num ".title())
    to_int = int(first_num)
    second_num = input("enter second num ".title())
    to_integer = int(second_num)
    print(f"the subtract of your numbers is {subtract_function(to_int,to_integer)}")
elif to_num == 3:
    print("welcome to divide wizard".title())
    first_num = input("enter first num")
    to_int = int(first_num)
    second_num = input("enter second num")
    to_integer = int(second_num)




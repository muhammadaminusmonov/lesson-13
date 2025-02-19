# debugging ~~~~~~~~~~~~~~

# Describe Problem
# in giving the end of number in range it won't include the that number itself.
# I changed 20 => 21 so the print will work
# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")
#
#
# my_function()

# Reproduce the Bug
# randint function includes both, start and ending number. I changed them to 1 => 0 and 6 => 5
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if 1980 < year < 1994:
#     print("You are a millennial.")
# else:
#     print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")

# # Print is Your Friend
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# Use a Debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)
#
#
# mutate([1, 2, 3, 5, 8, 13])

# # checks number for even or odd
# number = input("Enter the number that want to check: ")
# if number % 2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")

# leap year or not
# year = int(input("Enter the year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("It is a leap year")
#         else:
#             print("It is not a leap year")
#     else:
#         print("It is a leap year")
# else:
#     print("It is not a leap year")


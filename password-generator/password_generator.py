import random

upper_case_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case_letters = "abcdefghijklmnopqrstuvwxyz"
symbols = "!@#$%&()+-/*"
numbers = "0123456789"

print("Welcome to Password Generator")
print("-----------------------------")
upper_case_letters_count = int(input("Upper case (A-Z): "))
lower_case__letters_count = int(input("Lower case (a-z): "))
symbols_count = int(input("Special characters: "))
numbers_count = int(input("Numbers (0-9): "))

password_list = []

for i in range(upper_case_letters_count):
    password_list.append(random.choice(upper_case_letters))

for i in range(lower_case__letters_count):
    password_list.append(random.choice(lower_case_letters))

for i in range(symbols_count):
    password_list.append(random.choice(symbols))

for i in range(numbers_count):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for character in password_list:
    password += character

print("-----------------------------")
print("New Password =  " + password)

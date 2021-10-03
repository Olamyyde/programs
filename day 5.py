# student_heights = input("Input a list of student heights ").split()

# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])

# print(student_heights)

# # total height = sum(student_heights)
# total_height = 0
# for height in student_heights:
#     total_height += height
# print(total_height)

# # no_of_students = len(student_heights)
# no_of_students = 0
# for student in student_heights:
#     no_of_students += 1
# print(no_of_students)


# avg_height = round(total_height/no_of_students)
# print(avg_height)


# # max_value = max(student_heights)
# max_value = 0
# for score in student_heights:
#     if score > max_value:
#         max_value = score
# print(f'The highest score is {max_value}')


# # Even numbers from 1 to 100
# even = []
# for x in range(0, 101):
#     if x % 2 == 0:
#         even.append(x)
# print(even)

# # sum of Even numbers from 1 to 100
# even = []
# for x in range(0, 101):
#     if x % 2 == 0:
#         even.append(x)
# print(sum(even))

# even1 = 0
# for i in range(0, 101, 2):
#     even1 += i
# print(even1)



# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz") 
#     elif i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)


# Pypassword generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
 
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print('Welcome to the Password Generator')
no_L = int(input('How many letters would you like? \n'))
no_N = int(input('How many numbers would you like? \n'))
no_S = int(input('How many symbols would you like? \n'))


password = ""
for char in range(1, no_L + 1): 
    password += random.choice(letters)
for char in range(1, no_N + 1):
    password += random.choice(numbers)
for char in range(1, no_S + 1):
    password += random.choice(symbols)
print(f'Your easy level password is {password}') 


# Hard level
password = []
for char in range(1, no_L + 1): 
    password.append(random.choice(letters))
for char in range(1, no_N + 1):
    password.append(random.choice(numbers))
for char in range(1, no_S + 1):
    password.append(random.choice(symbols))

x = random.shuffle(password)
#Hard level
r = ""
for i in password:
    r += i
print(f'Your strong password is {r}')







    
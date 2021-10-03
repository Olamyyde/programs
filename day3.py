# h = int(input("what is your height? "))

# if (h > 120):
#     print("you can ride bruh")
# else:
#     print("sai baba")

print("\n\n")


# no = int(input("enter a no: "))

# x = no % 2

# if x == 0:
#     print("This is an even no")
# else:
#     print("This is an odd no")


# BMI calculator
# w = int(input("enter weight in kg: "))
# h = float(input("enter height in m: "))

# bmi = round(w/(h ** 2))

# print(f'Your bmi is {bmi}')

# if bmi  < 18.5:
#     print("u underweight brah")

# elif bmi > 18.5 and bmi < 25:
#     print("u normal weight brah")

# elif bmi > 25 and bmi < 30:
#     print("u overweight bruh")

# elif bmi > 30 and bmi < 35:
#     print("obesere")

# else:
#     print("clinically obese")


# Leap Year calculator
# yr = int(input("enter the year: "))


# if yr % 4 == 0:
#     if yr % 100 == 0:
#         if yr % 400 == 0:
#             print("This is a leap year")
#         else:
#             print("not a leap year")  
#     else:
#         print("leap year") 
    
# else:
#     print("Not a  leap year")
    


# Love Calculator
print('Welcome')
name1 = input('What is your name? \n')
name2 = input('What is their name? \n')

combo =  name1 + name2
lower_combo = combo.lower()

t = lower_combo.count("t")
r = lower_combo.count("r")
u = lower_combo.count("u")
e = lower_combo.count("e")

true = t + r + u + e

l = lower_combo.count("l")
o = lower_combo.count("o")
v = lower_combo.count("v")
e = lower_combo.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

# print(f'Your score is {love_score}')

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and akara")

elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, y'all tight")

else:
    print(f"Your Score is {love_score}")



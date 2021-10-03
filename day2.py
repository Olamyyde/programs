# x = input("Enter two digit number: ")

# print(int(x[0]) + int(x[1]))

#BMI calculator
# w = int(input("enter weight in kg: "))
# h = float(input("enter height in m: "))

# bmi = w/(h ** 2)

# print(f"Your BMI is {int(bmi)}")

# a = int(input("Enter your age: "))
# days = (90-a) * 365
# weeks = (90-a) * 52
# years =(90-a)

# print(f"you have {days} days, {weeks} weeks, {years} years left")


print("welcome")

tot = float(input("what was total bill? $ "))
percent = int(input("what percentage would you like? 10, 12 or 15? "))
people = int(input("how many poeple? "))

tip_percent = percent/100
tot_bill = tot * tip_percent
bill_per_person = tot_bill/people
final = round(bill_per_person, 2)
print(f"Each person should pay ${final}")



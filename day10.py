#fxns with outputs

# title() returns the lower case of the mixed string but the first letters
# retain their case 

def format_name(f_name, l_name):
    """Take a first and last name and format it to return the
    title case version of the name. """
    format1 = f_name.title()
    format2 = l_name.title()

    return f'{format1} {format2}' # Return tells the pc that that's the end of the fxn

final_form = format_name("MyYdE", "JOHN")
print(final_form) 






# leap year

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid Input"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29

    return month_days[month - 1]



  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)



# Calculator

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
    
# fam = multiply(2, 3)
# print(fam)


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


num1 = int(input("enter 1st no: "))
num2 = int(input("enter 2nd no: "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation below: ")
calc_func = operations[operation_symbol]
answer = calc_func(num1, num2)

print(f'{num1} {operation_symbol} {num2} = {answer}')
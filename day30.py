# Exceptions

# try:
#     file = open("a.txt")
# except:
#     print("Error Occurred")


# try:
#     file = open("a.txt")
#     dicted = {"key": "value"}
#     # print(dicted["sdsd"])
#     print(dicted["key"])
# except FileNotFoundError:
#     file = open("a.txt", "w")
#     file.write("sth")
# except KeyError:
#     print("Key doesn't exist")
# else: 
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("file was closed")
#     # raise KeyError
#     raise TypeError("This is an Error")



# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Height should be above 3 meters")

# bmi = weight/height ** 2
# print(bmi)


fruits = ["orange", "apple", "mango"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print('fruit pie')
    else:
        print(fruit + " pie")

make_pie(5)


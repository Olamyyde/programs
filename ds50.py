print(type("Hey".replace("ey","i")[-1]))


d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"},                
                ],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

# print(d["employees"][1]["lastName"])

d["employees"][1]["lastName"] = "Mide"
print(d["employees"][1]["lastName"])


import json

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

with open("company.json", "w") as file:
	json.dump(d, file, indent = 4)


from pprint import pprint

with open("company.json", "r") as file:
	d = json.loads(file.read())

pprint(d)

# add a new employee to the json file
import json

with open("company.json", "r+") as file:
	d = json.loads(file.read())
	d["employees"].append(dict(firstName = "Albert", lastName = "Einstein" ))
	file.seek(0)
	json.dump(d, file, indent=4, sort_keys=True)
	file.truncate()


# enumerate(a)  creates an enumerate object which yields pairs of indexes and items.
a = [1, 2, 3] 

for i, index in enumerate(a):
	print(f'Item {i} has index {index}')



# import time

# while True:
# 	print("Hello")
# 	time.sleep(2)


# Create a program that once executed the programs prints Hello  instantly first,
# then it prints it after 1 second, then after 2, 3, and 
# then the program prints out the message "End of the Loop" and stops.

# import time

# i = 0
# while True:
# 	i += 1
# 	print("Hello")

# 	if i > 3:
# 		print("end of loop")
# 		break
# 	time.sleep(i)


# while True:
# 	print("Hello")
# 	if 2>1:
# 		pass
# 	print("Hi")


# The program takes a word from the user as input and
# translates it using the following dictionary as a vocabulary source.

d = dict(weather = "clima", earth = "terra", rain = "chuva") 

# def vocab(word):
# 	return d[word]

# word = input("Enter word: ")
# print(vocab(word))


# def vocab(word):
# 	try:
# 		return d[word]
# 	except KeyError:
# 		return "this word does not exist"

# word = input("Enter word: ")
# print(vocab(word))

# case In-sensitive
def vocab(word):
	try:
		return d[word]
	except KeyError:
		return "we couldn't find this word"

word = input("Enter word: ").lower()
print(vocab(word))
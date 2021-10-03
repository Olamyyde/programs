# for i in range(1,11):
# 	print(i)



# def acceleration(v1,v2,t1,t2):
# 	a = (v2 - v1)/(t2 - t1)
# 	return a

# print(acceleration(0, 10, 0, 20))


from math import pi

def volume(h, r = 10):
	v = ((1/3)*pi*(4*r**3 - (h**2 * (3*r - h)))) 
	return v

print(volume(2))



#Create a function that takes any string as input and returns the number of words for that string.
def count_words(Strng):
	splited = Strng.split()
	return len(splited)

print(count_words("I am a man"))


# Create a function that takes a text file as input and 
# returns the number of words contained in the text file.

def counter(filepath):
	with open(filepath, 'r') as file:
		Sttrng = file.read()
		Sttrng_list = Sttrng.split(" ")
		return len(Sttrng_list)

print(counter('words1.txt'))



def counter_words(filepath):
	with open(filepath, 'r') as file1:
		Sttrng1 = file1.read()
	Sttrng1 = Sttrng1.replace(",", " ")
	Sttrng_list1 = Sttrng1.split(" ")
	return len(Sttrng_list1)
		
print(counter_words('words1.txt'))


import math
print(math.cos(1))


print(math.pow(2,3))


import string


# with open('letter.text', 'w+') as file:
# 	for letter in string.ascii_lowercase:
# 		file.write(letter + '\n')
		

a = [1, 2, 3]
b = (4, 5, 6)

for i,j in zip(a, b):
	print(i+j)



# Create a script that generates a file 
# where all letters of English alphabet are listed two in each line. 

with open('letters.text', 'w') as file:
	for letter1, letter2 in zip(string.ascii_lowercase[0::2], string.ascii_lowercase[1::2]):
		file.write(letter1 + letter2 + '\n')
		


letters = string.ascii_lowercase + " "

slice1 = letters[0::3]
slice2 = letters[1::3]
slice3 = letters[2::3]



with open('lettery.text', 'w') as file:
	for letter1, letter2, letter3 in zip(slice1, slice2, slice3):
		file.write(letter1 + letter2 + letter3 + '\n')


# Please create a script that generates 26 text files named a.txt, b.txt, and so on up to z.txt. 
# Each file should contain a letter reflecting its filename.
# So, a.txt will contain letter a, b.txt will contain letter b and so on.

import string, os

if not os.path.exists("letters"):
	os.makedirs("letters")

for xter in string.ascii_lowercase:
	with open("letters/" + xter + ".txt", "w") as file:
		file.write(xter + "\n")



# Write a script that extracts letters from the 26 text files 
# and put the letters in a list 

# import glob

# letters = []
# file_list = glob.glob('letters\*.txt')

# for filename in file_list:
# 	with open(filename, "r") as file:
# 		letters.append(file.read().strip('\n'))

# print(letters)

# Create a script that iterates through text files and checks if strings p, y, t, h, o, or n are found in the content of the text file.
# If any of those strings is found, append that string to a list.

import glob

letters = []
file_list = glob.iglob('letters\*.txt')
check = "python"

for filename in file_list:
	with open(filename, "r") as file:
		letter = file.read().strip("\n")
	if letter in check:
		letters.append(letter)


print(letters)


for letter in "Hello":
    if letter == "e":
    	print(letter)




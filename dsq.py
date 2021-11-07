# import csv
# from IPython.display import clear_output



# # handle user registration and writing to csv

# def registerUser():
# 	with open('users.csv', 'a', newline='') as f:
# 		writer = csv.writer(f, delimiter = ',')
# 		print("To register, please enter your info: ")
# 		email = input("E-mail: ")
# 		password = input("Password: ")
# 		password2 = input("re-type password: ")
# 		clear_output()
# 		if password == password2:
# 			writer.writerow( [email, password] )
# 			print('You are now registered!')
# 		else:
# 			print('Something went wrong. Try again')

# def loginUser():
# 	print("To login, please enter your info: ")
	
# 	email = input('E-mail: ')
# 	password = input("password: ")
	
# 	clear_output()
	
# 	with open('users.csv', 'r') as f:
# 		reader = csv.reader(f, delimiter=',')
# 		for row in reader:
# 			if row == [email, password]:
# 				print('You are logged in now!')
# 				return True
# 	print('Something went wrong, try again.')
# 	return False



phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

for i in range(4):
	plist.pop()
plist.pop(0)
plist.remove("'")
plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))


new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

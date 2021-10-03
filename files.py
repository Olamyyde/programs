text = 'dkjnladlkn adlnlnamdmn;da k;dam;m;dam;;admjmneq'

s = open('rsa.txt', 'w')

s.write(text)
s.close()

smh = open('rsa.txt', 'r')

z = smh.read()
print(z)


# w means writing to a file, a means appending, r is reading


t=66
while True:
	value = input('Enter an integer btw 1 and 100: ')
	try:
		value=int(value)
	except ValueError:
		print("I said Enter an integer")

if value > t:
	print(value, 'is too high')
elif int(value < target):
	print('too low')
else:
	print('perfect')
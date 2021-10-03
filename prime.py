E = int(input('Enter number: '))

if E > 1:
	for i in range(2 , E):
		if E % i == 0:
			print(E, ' is not a Prime number')
			print(f'{i} times {E//i} is {E}')
			break
		else:
			print('This is a prime number')
			break

# if number is less or equal to 1
else:
	print('Not a prime number')




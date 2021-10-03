import random

def guess(x):
	rand_no = random.randint(1,x)
	guess = 0

	while guess != rand_no:
		guess = int(input('guess a number between 1 and {}: '.format(x)))
		print(guess)
		if guess < rand_no:
			print('sorry, guess again. Too low')
		elif guess > rand_no:
			print('too high')
	
	print(f'Yay, congrats. You have guessed the number {rand_no}')


def pc_guess(x):
	low = 1
	high = x
	feedback = ''
	while feedback != 'c':
		guess = random.randint(low, high)
		feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
		if feedback == 'h':
			high = guess - 1
		elif feedback == 'l':
			low = guess + 1

	print(f'The pc guessed your number, {guess} correctly!')

pc_guess(1000)
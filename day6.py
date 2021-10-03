# x = 4
# while x > 0:
#     print("shii")
#     x -= 1



# picking random words and checking answers
import random

import matplotlib


word_list = ['advark', 'baboon', 'camel']

#randomly choose a word from the list
chosen_word = random.choice(word_list)
# print(chosen_word)


guess = input('Guess a letter: ').lower()

# if guess == chosen_word:
#     print('You guessed right dude')
# else:
#     print(f'You guessed wrong, the right answer is {chosen_word}')

print(f'The right answer is {chosen_word}')

display = []
word_length = len(chosen_word)

# for letter in chosen_word:
#     if letter == guess:
#         print('right')
#     else:
#         print('wrong')

for letter in range(word_length):
    display += "_"
print(display)


end_of_game = False

while not end_of_game:
    for position in range(word_length):
        letter = chosen_word[position]
        print(f'Current position: {position}')
        print(f'Current letter: {letter}')
        print(f'Guessed letter: {guess}')    
        if letter == guess:
            display[position] = letter

    print(display)

    if '_' not in display:
        end_of_game = True
        print('You win')



    





    

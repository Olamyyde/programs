import random

# r = random.randint(1, 29)
# print(r)

# random_float = random.random()
#  print(random_float)


# test_seed = int(input("create a seed no: "))
# random.seed(test_seed)

# randoma = random.randint(0,1)

# if randoma == 1:
#     print('Heads')
# else:
#     print('Tails')


# Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

# x = random.randint(0, len(names)-1)
# l = random.choice(names)
# print(names[x], " is going to buy it")
# print(l)



# Treasure Map

# row1 = ['#', '#', '#']
# row2 = ['#', '#', '#']
# row3 = ['#', '#', '#']

# map = [row1, row2, row3]
# print(f'{row1}\n{row2}\n{row3}')

# position = input("Where do u want to put the treasure? ")

# hori = int(position[0])
# verti = int(position[1])

# selected_row = map[verti-1]
# selected_row[hori - 1] = "X"

# print(f'{row1}\n{row2}\n{row3}')


# Rock, paper, scissors

# Rock = 'rock'
# paper = 'paper'
# scissors = 'scissors'



# game_img = [Rock, paper, scissors] 
# user_choice = int(input("what do you choose? Type 0 for Rock, 1 for paper or 2 for scissors. \n"))
# print(game_img[user_choice])

# pc_choice = random.randint(0, 2)
# print(f'Computer chose: {game_img[pc_choice]} ')

# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid no. You lose!")
# elif user_choice == 0 and pc_choice == 2:
#     print("you win!")
# elif pc_choice == 0 and user_choice == 2:
#     print("you lose!")
# elif pc_choice > user_choice:
#     print("You lose")
# elif user_choice > pc_choice:
#     print("You win")
# elif user_choice == pc_choice:
#     print("Draw!")








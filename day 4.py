import random

# r = random.randint(1, 29)
# print(r)

# random_float = random.random()
# print(random_float)


test_seed = int(input("create a seed no: "))
random.seed(test_seed)

randoma = random.randint(0,1)

if randoma == 1:
    print('Heads')
else:
    print('Tails')

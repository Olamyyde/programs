
def greet():
    print('dss')
    print('adfd')
    print('saddfs')


# greet()

def greet_name(name, city):
    print(f'Hello {name}, you from {city}?')

# greet_name(city='lag', name='lola')


# import math
# from typing import Text

# print(round(23.212, 2))


# Prime Number Checker
# n = int(input('Enter number to be checked: '))

# def prime_checker(number):
#     if number > 1:
#         for i in range(2, number):
#             if number % i == 0:
#                 print('Not prime number')
#                 break
#             else:
#                 print('prime')
#             break
#     else:
#         print('prime number')


def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Na prime Number")
    else:
        print("No be prime number")


# prime_checker(number = n)



# Caeser Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
 'y', 'z']


def caesar(start_text, shift_amt, cipher_direction):
    end_text=""
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            if cipher_direction == 'decode':
                shift_amt *= -1
            new_position = position + shift_amt
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f'The {cipher_direction}d text is {end_text}')

should_continue = True
while should_continue:
    direction = input('Type "encode" to encrypt, type "decode" to decrypt:\n')

    text = input('Type your message:\n').lower()

    shift = int(input('Type the shift number:\n'))

    shift = shift % 25

    caesar(start_text=text, shift_amt=shift, cipher_direction=direction)

    end_program = input('Do you want to end the program? Type "yes" to end, "no" to continue: ').lower()
    if end_program == 'yes':
        should_continue = False
        print('Sayonara')
    

# def encrypt(plain_text, shift_amt):
#     cipher_text = ""
#     for letter in plain_text:
#         # Index of the letter that we are looping through
#         position = alphabet.index(letter)
#         new_position = position + shift_amt
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f'The encoded text is {cipher_text}')

# def decrypt(cipher_text, shift_amt):
#     plain_text = ""
#     for letter in cipher_text:
#         # Index of the letter that we are looping through
#         position = alphabet.index(letter)
#         new_position = position - shift_amt
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     print(f'The decoded text is {plain_text}')

# if direction == 'encode':
#     encrypt(plain_text=text, shift_amt=shift)
# elif direction == 'decode':
#     decrypt(cipher_text=text, shift_amt=shift)







        







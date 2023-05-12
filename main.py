# functions with parameters
from alphabet import alphabet
from art import logo
def ceasar(shift, word, direction):
        e_word = ""
        if direction == 'decode':
            shift *= -1
        for letter in word:
            if letter in alphabet:
                for x in range(len(alphabet)):  # alternative way is index = alphabet.index(letter)
                    if letter == alphabet[x]:  # temp_letter = alphabet[(index + shift) % 26]
                        temp_letter = alphabet[(x + shift) % 26]
                        e_word += temp_letter
            else:
                e_word += letter
        print(e_word)

# def encryption(shift, word):
#     e_word = ""
#     for letter in word:
#         for x in range(len(alphabet)):  # alternative way is index = alphabet.index(letter)
#             if letter == alphabet[x]:  # temp_letter = alphabet[(index + shift) % 26]
#                 temp_letter = alphabet[(x+shift) % 26]
#                 e_word += temp_letter
#     print(e_word)
#
# def decryption(shift, word):
#     d_word = ""
#     for letter in word:
#         index = alphabet.index(letter)
#         temp_letter = alphabet[(index - shift) % 26]
#         d_word += temp_letter
#     print(d_word)
finished_ciphering = False
while not finished_ciphering:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt. ").lower()
    word = input(f"Type your message to {direction}. ").lower()
    shift = int(input('Type the shift number. '))

    if direction == 'encode':
        ceasar(shift=shift, word=word, direction=direction)
    elif direction == 'decode':
        ceasar(shift=shift, word=word, direction=direction)
    else:
        print('Invalid input.')
    want_to_continue = input("Type 'yes' if you want to go again, 'no' otherwise. ").lower()
    if want_to_continue == 'no':
        finished_ciphering = True
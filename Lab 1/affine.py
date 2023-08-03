# Solving 1. Affine cipher

from string import ascii_uppercase

a_arr = [1,3,5,7,9,11,15,17,19,21,23,25]
a_arr_inverse = [1, 9,21,15,3,19,7,23,11,5,17,25]

def affine_encrypt(pt: str,a: int,b: int):

    if a not in a_arr_inverse:
         raise Exception('a not in [1,3,5,7,9,11,15,17,19,21,23,25]')

    pt = pt.upper()
    pt_arr = pt.split(' ')
    encrypted_arr = []
    for word in pt_arr:
         temp_word_array = []
         for letter in word:
            letter_index = ascii_uppercase.index(letter)
            enc_letter_index = ((a*letter_index) + b) % 26
            temp_word_array.append(ascii_uppercase[enc_letter_index])
         encrypted_arr.append("".join(temp_word_array))

    return " ".join(encrypted_arr)
    

def affine_decrypt(y: str,a: int,b: int):
    y = y.upper()
    if a not in a_arr:
         raise Exception('a not in [1,3,5,7,9,11,15,17,19,21,23,25]')
    y_arr = y.split(' ')
    decrypted_arr = []
    for word in y_arr:
         temp_word_array = []
         for letter in word:
            letter_index = ascii_uppercase.index(letter)
            dec_letter_index = (a_arr_inverse[a_arr.index(a)] * (letter_index - b)) % 26
            temp_word_array.append(ascii_uppercase[dec_letter_index])
         decrypted_arr.append("".join(temp_word_array))

    return " ".join(decrypted_arr)


choice = int(input('Decrypt (1) or Encrypt (2) ?'))

if choice == 1 :
    print(affine_decrypt(input('Plain text?'), int(input('Value of a?')), int(input('Value of b?'))))
elif choice == 2:
        print(affine_encrypt(input('Cipher Text?'), int(input('Value of a?')), int(input('Value of b?'))))

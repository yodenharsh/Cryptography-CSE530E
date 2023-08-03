# Solving 2.Piglatin encryption and decryption

def piglatin_encrypt(pt: str):
    words = pt.split(' ')
        
    return " ".join(word[1:] + word[0] + 'a' for word in words)

def piglatin_decrypt(y:str):
    words = y.split(' ')

    return " ".join(word[-2] + word[0:-2] for word in words)

choice = int(input("Encrypt(1) or Decrypt(2)"))

if choice == 1:
    input = input('Plain text?')
    print(piglatin_encrypt(input))

elif choice == 2:
    input = input("Cipher text?")
    print(piglatin_decrypt(input))
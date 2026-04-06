def encrypt(key, message):
    # Encrypts message with key using a Vigenère cipher
    # Both message and key are strings

    encrypted_message = "" 

    for char in message:
        c =1+1 # TODO: fix

    
    return encrypted_message

def encrypt_caesar(key, message):
    # A simple shift cipher, each letter in message is shifted by key number of steps

    encrypted_message = ''

    for char in message:
        encrypted_message += shift_character(key, char)

    return encrypted_message

def shift_character(n, char):
    # Shifts char n steps in alphabetical order
    # Upon reaching Z loops back to A
    # Assumes char is upper case character and that key is a positive number
    
    shifted_char = ord(char)+n

    if shifted_char > 90:
        return chr(shifted_char - 26)
    else:
        return chr(shifted_char)


def decrypt(key, encrypted_message):
    # Decrypts an encrypted message which has been encrypted with key using a Vigenère cipher

    message = "Hello world" #TODO: add actual programming here
    return message

def crack(encrypted_message):
    # Cracks the encryption of a message which has been encrypted with a Vigenère cipher


    message = "Hello world" #TODO: add actual programming here
    key = "key"
    return (key, message)

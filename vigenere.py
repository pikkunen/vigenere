def encrypt_vigenere(key, message):
    # Encrypts message with key using a Vigenère cipher
    # Both message and key are strings

    formatted_message = format_message(message)
    formatted_key = format_message(key)
    encryption_key = generate_key(formatted_key)
    key_length = len(formatted_key)

    encrypted_message = ''
    i = 0 # iterator tracking which letter in key to use for 

    for char in formatted_message:
        encrypted_message += shift_character(encryption_key[i%key_length],char)
        i += 1

    return encrypted_message

def decrypt_vigenere(key, encrypted_message):
    # Decrypts an encrypted message which has been encrypted with key using a Vigenère cipher

    formatted_key = format_message(key)
    encryption_key = generate_key(formatted_key)
    key_length = len(formatted_key)

    decrypted_message = ''
    i = 0 # iterator tracking which letter in key to use for decryption

    for char in encrypted_message:
        decrypted_message += unshift_character(encryption_key[i%key_length],char)
        i += 1

    return decrypted_message

def encrypt_caesar(key, message):
    # A simple shift cipher, each character in message is shifted by key number of steps

    encrypted_message = ''

    for char in message:
        encrypted_message += shift_character(key, char)

    return encrypted_message

def decrypt_caesar(key, encrypted_message):
    # Decrypts a simple shift cipher, where each character has been shifted by key number of steps

    decrypted_message = ''

    for char in encrypted_message:
        decrypted_message += unshift_character(key, char)
    
    return decrypted_message

def shift_character(n, char):
    # Shifts char n steps in alphabetical order
    # Upon reaching Z loops back to A
    # Assumes char is an upper case character and that n is a positive number
    
    shifted_char = ord(char)+n

    if shifted_char > 90:
        return chr(shifted_char - 26)
    else:
        return chr(shifted_char)

def unshift_character(n, char):
    # Shifts char n steps in reverse alphabetical order
    # Upon reaching A loops back to Z
    # Assumes char is an upper case character and that n is a positive number

    unshifted_char = ord(char)-n

    if unshifted_char < 65:
        return chr(unshifted_char + 26)
    else:
        return chr(unshifted_char)

def format_message(message):
    # Formats any text to only upper case letters
    # By removing all non-letter characters and shifting lower case letters to upper case

    uppercase_message = message.upper()

    formatted_message = ''

    for char in uppercase_message:
        if 65 <= ord(char) and ord(char) <= 90:
            formatted_message += char

    return formatted_message

def generate_key(key):
    # Generates a list of integers for the position values of all characters in key
    # So A = 0, B = 1, C = 2 etc
    # Assumes key contains only upper case letters
    encryption_key = []
    for char in key:
        encryption_key.append(ord(char)-65)
        
    return encryption_key

                                                                                                                                                                                                                                







def crack_vigenere(encrypted_message):
    # Cracks the encryption of a message which has been encrypted with a Vigenère cipher


    message = "Message" #TODO: add actual programming here
    key = "key"
    return (key, message)

def crack_caesar(encrypted_message):
    # Cracks the encryption of a message which has been encrypted with a Vigenère cipher

    message = "Message" #TODO: add actual programming here
    key = "key"
    return (key, message)


# The statistical frequency at which letters occur in English (percentages)
# List of (char,num) touples
letter_frequency_eng = [('E', 12.7),('T', 9.1),('A', 8.2),('O', 7.5),('I', 7.0),('N', 6.7),('S',6.3),('H', 6.1),('R', 6.0),('D', 4.3),('L', 4.0),('C', 2.8),('U', 2.8),('M', 2.4),('W', 2.4),('F', 2.2),('G', 2.0),('Y', 2.0),('P', 1.9),('B', 1.5),('V', 1.0),('K', 0.8),('J', 0.15),('X', 0.15),('Q', 0.10),('Z',0.07)]

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def count_character_frequency(encrypted_message):
    # Counts the number of time each letter occurs in the encrypted message
    # Returns a list of touples of char int pairs

    letter_count=[]

    for letter in alphabet:
        count = encrypted_message.count(letter)
        letter_count.append((letter, count))
                            

    return letter_count

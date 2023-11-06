import string

def caeasar_shift(plaintext, num_of_shift):
    ciphertext = ""

    for element in plaintext:
        print(element)
        old_char = element
        if old_char.isalpha():
            new_char = ord(old_char) + int(num_of_shift)
            if old_char.islower():
                if new_char > ord('z'):
                    new_char -= 26
                elif new_char < ord('a'):
                    new_char += 26
            elif old_char.isupper():
                if new_char > ord('Z'):
                    new_char -= 26
                elif new_char < ord('A'):
                    new_char += 26
            ciphertext += chr(new_char)
        else:
            ciphertext += old_char  # Keep non-alphabetic characters unchanged
    ciphertext = ciphertext.upper()
    return ciphertext
    

def generate_keyword_cipher_alphabet(keyword):
    alphabet = string.ascii_uppercase
    keyword = keyword.upper()
    cipher_alphabet = ""

    for char in keyword:
        if char not in cipher_alphabet:
            cipher_alphabet += char

    for char in alphabet:
        if char not in cipher_alphabet:
            cipher_alphabet += char


    print(cipher_alphabet)
    return cipher_alphabet


def keyword_cipher_encrypt(text, keyword):
    cipher_alphabet = generate_keyword_cipher_alphabet(keyword)
    text = text.upper()
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            index = string.ascii_uppercase.index(char)
            encrypted_text += cipher_alphabet[index]
        else:
            encrypted_text += char

    return encrypted_text

def generate_giovanni_cipher_alphabet(keyword, starting_letter):
    alphabet = string.ascii_uppercase
    keyword = keyword.upper()
    kw_len = len(keyword)
    starting_letter = starting_letter.upper()
    starting_letter_index = alphabet.index(starting_letter)
    total_alphabet = 26 - starting_letter_index

    cipher_alphabet = ""
    final_letters = ""

    count = kw_len
    for char in alphabet:
        char = char.upper()
        if char not in keyword and char in string.ascii_uppercase:
            if count<total_alphabet:
                cipher_alphabet += char
                count+=1
                print(cipher_alphabet)
                print(count)
            elif total_alphabet<=count:
                final_letters +=char
                count+=1
                print(final_letters)
                print(count)

    cipher_alphabet = final_letters+ keyword +cipher_alphabet
    return cipher_alphabet    

def giovanni_cipher_encrypt(text, keyword, starting_char):
    cipher_alphabet = generate_giovanni_cipher_alphabet(keyword, starting_char)
    text = text.upper()
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            index = string.ascii_uppercase.index(char)
            encrypted_text += cipher_alphabet[index]
        else:
            encrypted_text += char

    return encrypted_text

def transposition(text):

    transposit = ""
    first_str = ""
    second_str = ""
    index = 0
    for letter in text:
        
        modulo = index % 2
        print(index)
        print(modulo)
        if (index == 0 or (modulo == 0)):
            print("EVEN")
            first_str += letter
            print(first_str)
        elif (index == 1 or (modulo == 1)):
            print("ODD")
            second_str += letter
            print(second_str)
        index +=1
        
    transposit= first_str + second_str
    return transposit.upper()
import string

def caeasar_shift(plaintext, num_of_shift):
    ciphertext = ""
    #ciphertext = ''.join(chr(ord(character) + num_of_shift) for character in plaintext)

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
    return ciphertext
    

def generate_cipher_alphabet(keyword):
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
    cipher_alphabet = generate_cipher_alphabet(keyword)
    text = text.upper()
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            index = string.ascii_uppercase.index(char)
            encrypted_text += cipher_alphabet[index]
        else:
            encrypted_text += char

    return encrypted_text



def giovanni_cipher(text, keyword, key_letter, decrypt=False):
    text = text.upper()
    keyword = keyword.upper()
    key_letter = key_letter.upper()

    key = (keyword + key_letter * (len(text) // len(keyword)))[:len(text)]
    print(key)
    result = ""
    for i in range(len(text)):
        if text[i].isalpha():
            keyword_shift = string.ascii_uppercase.index(key[i]) + 1
            text_shift = string.ascii_uppercase.index(text[i]) + 1
            shift = keyword_shift if not decrypt else -keyword_shift
            shifted_index = (text_shift + shift - 1) % 26
            result += string.ascii_uppercase[shifted_index]
            print(result)
        else:
            result += text[i]
    print(result)
    return result

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
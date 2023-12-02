def generate_vigenere_table():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    table = [[(i + j) % 26 for j in range(26)] for i in range(26)]
    return table, alphabet

def vigenere_encrypt(plain_text, key):
    table, alphabet = generate_vigenere_table()
    key = key.upper()
    encrypted_text = ""

    for i, char in enumerate(plain_text):
        if char.isalpha():
            char_index = alphabet.index(char.upper())
            key_char = key[i % len(key)]
            key_index = alphabet.index(key_char)

            encrypted_char = alphabet[table[key_index][char_index]]
            if char.islower():
                encrypted_char = encrypted_char.lower()

            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    table, alphabet = generate_vigenere_table()
    key = key.upper()
    decrypted_text = ""

    for i, char in enumerate(encrypted_text):
        if char.isalpha():
            char_index = alphabet.index(char.upper())
            key_char = key[i % len(key)]
            key_index = alphabet.index(key_char)

            decrypted_char = alphabet[table[key_index].index(char_index)]
            if char.islower():
                decrypted_char = decrypted_char.lower()

            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text

# Пример 
# plain_text = "HelloWorld"
# key = "KEY"

plain_text = "Two roads diverged in a yellow wood,\
and sorry I could not travel both \
and be one traveler, long I stood\
and looked down one as far as I could\
to where it bent in the undergrowth."
key = 'UDSU'

encrypted_text = vigenere_encrypt(plain_text, key)

print("ORIGINAL TEXT:", plain_text)
print()
print(':D  ' * 20)
print()
print("ENCRYPTED TEXT:", encrypted_text)
def encrypt_caesar(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_caesar(encrypted_text, shift):
    return encrypt_caesar(encrypted_text, -shift)

def break_caesar_cipher(encrypted_text):
    
    possible_decryptions = []

    # Перебор сдвигов (от 1 до 25)
    for shift in range(1, 26):
        decrypted_text = decrypt_caesar(encrypted_text, shift)
        possible_decryptions.append(decrypted_text)

    return possible_decryptions

#Пример
text_to_encrypt = "Hello, World!"
shift_value = 7

# text_to_encrypt = "Hochu spat"
# shift_value = 12

#Шифрование
encrypted_text = encrypt_caesar(text_to_encrypt, shift_value)
print(f"Encrypted Text: {encrypted_text}")

#Расшифрование взломом
possible_decryptions = break_caesar_cipher(encrypted_text)

# Вывод всех вариантов с разными сдвигами
print("Decrypted text:")
for i, decryption in enumerate(possible_decryptions):
    print(f"    Variant {i + 1}: {decryption}")

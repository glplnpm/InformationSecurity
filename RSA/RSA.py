import random


def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def euler_totient(phi):
    return phi * (1 - 1/phi)


def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2
    while gcd(e, phi) != 1:
        e += 1
    d = 1
    while (d * e) % phi != 1:
        d += 1
    return ((e, n), (d, n))


def encrypt(pk, plain_text):
    characters = list(plain_text)
    ascii_values = [ord(char) for char in characters]
    encrypted_values = [pow(value, pk[0]) % pk[1] for value in ascii_values]
    return encrypted_values


def decrypt(pk, encrypted_text):
    decrypted_values = [pow(value, pk[0]) % pk[1] for value in encrypted_text]
    characters = [chr(value) for value in decrypted_values]
    return ''.join(characters)

# p = 61
# q = 53

p = random.randint(0, 100)
q = random.randint(0, 100)

pk, sk = generate_keys(p, q)


# message = "Hello, world!"
message = 'skoro sessiya'
print("ORIGINAL:", message)
encrypted_message = encrypt(pk, message)
print("ENCRYPTED:", *encrypted_message)


decrypted_message = decrypt(sk, encrypted_message)
print("DECRYPTED:", decrypted_message)
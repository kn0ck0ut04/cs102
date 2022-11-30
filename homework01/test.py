def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    len_alphabet = ord('z') - ord('a') + 1
    
    for i in range(len(plaintext)):
        o = ord(plaintext[i])
        if plaintext[i].islower():
            shift = ord(keyword[i % len(keyword)]) - ord("a")
            ciphertext += chr((o + shift - ord("a")) % len_alphabet + ord("a"))
        elif plaintext[i].isupper():
            shift = ord(keyword[i % len(keyword)]) - ord("A")
            ciphertext += chr((o + shift - ord("A")) % len_alphabet + ord("A"))
        else:
            ciphertext += plaintext[i]

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    len_alphabet = ord('z') - ord('a') + 1

    for i in range(len(ciphertext)):
        o = ord(ciphertext[i])
        if ciphertext[i].islower():
            shift = ord(keyword[i % len(keyword)]) - ord("a")
            plaintext += chr((o - shift - ord("a")) % len_alphabet + ord("a"))
        elif ciphertext[i].isupper():
            shift = ord(keyword[i % len(keyword)]) - ord("A")
            plaintext += chr((o - shift - ord("A")) % len_alphabet + ord("A"))
        else:
            plaintext += ciphertext[i]

    return plaintext

print(encrypt_vigenere('ATTACKATDAWN', "LEMON"))
print(decrypt_vigenere('LXFOPVEFRNHR', 'LEMON'))
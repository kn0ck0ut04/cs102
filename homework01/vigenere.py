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
    len_alphabet = ord("z") - ord("a") + 1

    for i in range(len(plaintext)):
        if plaintext[i].islower():
            shift = ord(keyword[i % len(keyword)]) - ord("a")
            ciphertext += chr((ord(plaintext[i]) + shift - ord("a")) % len_alphabet + ord("a"))
        elif plaintext[i].isupper():
            shift = ord(keyword[i % len(keyword)]) - ord("A")
            ciphertext += chr((ord(plaintext[i]) + shift - ord("A")) % len_alphabet + ord("A"))
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
    len_alphabet = ord("z") - ord("a") + 1

    for i in range(len(ciphertext)):
        if ciphertext[i].islower():
            shift = ord(keyword[i % len(keyword)]) - ord("a")
            plaintext += chr((ord(ciphertext[i]) - shift - ord("a")) % len_alphabet + ord("a"))
        elif ciphertext[i].isupper():
            shift = ord(keyword[i % len(keyword)]) - ord("A")
            plaintext += chr((ord(ciphertext[i]) - shift - ord("A")) % len_alphabet + ord("A"))
        else:
            plaintext += ciphertext[i]

    return plaintext

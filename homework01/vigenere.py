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
    for i in range(len(plaintext)):
        if ord("a") <= ord(ciphertext) <= ord("z"):
            shift = ord(keyword[i % len(keyword)]) - ord("a")
            ciphertext += chr((ord(ciphertext) + shift - ord("a")) % 26 + ord("a"))
        elif ord("A") <= ord(ciphertext) <= ord("Z"):
            shift = ord(keyword[i % len(keyword)]) - ord("A")
            ciphertext += chr((ord(ciphertext) + shift - ord("A")) % 26 + ord("A"))
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
    for i in range(len(ciphertext)):
        if ord("a") <= ord(ciphertext) <= ord("z"):
            shift = ord(keyword[i % len(keyword)]) - ord("a")
            plaintext += chr((ord(ciphertext) - shift - ord("a")) % 26 + ord("a"))
        elif ord("A") <= ord(ciphertext) <= ord("Z"):
            shift = ord(keyword[i % len(keyword)]) - ord("A")
            plaintext += chr((ord(ciphertext) - shift - ord("A")) % 26 + ord("A"))
        else:
            plaintext += ciphertext[i]
    return plaintext

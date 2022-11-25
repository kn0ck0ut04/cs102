import caesar


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
    while len(keyword) < len(plaintext):
        keyword += keyword

    low_range = range(ord("a"), ord("z") + 1)
    ciphertext = ""

    for i in range(len(plaintext)):
        c = plaintext[i]
        k = keyword[i]
        if ord(k) in low_range:
            shift = ord(k) - ord("a")
        else:
            shift = ord(k) - ord("A")
        ciphertext += caesar.encrypt_caesar(c, shift)
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
    while len(keyword) < len(ciphertext):
        keyword += keyword

    low_range = range(ord("a"), ord("z") + 1)
    plaintext = ""

    for i in range(len(ciphertext)):
        c = ciphertext[i]
        k = keyword[i]
        if ord(k) in low_range:
            shift = ord(k) - ord("a")
        else:
            shift = ord(k) - ord("A")
        plaintext += caesar.decrypt_caesar(c, shift)
    return plaintext

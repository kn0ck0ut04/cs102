def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    lowercase = range(ord("a"), ord("z") + 1)
    highercase = range(ord("A"), ord("Z") + 1)

    for i in plaintext:
        if ord(i) not in lowercase and ord(i) not in highercase:
            ciphertext += i
            continue
        if ord(i) in lowercase:
            index = (ord(i) - ord("a") + shift) % len(lowercase)
            ciphertext += chr(ord("a") + index)
        elif ord(i) in highercase:
            index = (ord(i) - ord("A") + shift) % len(highercase)
            ciphertext += chr(ord("A") + index)
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    return encrypt_caesar(ciphertext, ord("z") - ord("a") - shift + 1)
    return plaintext

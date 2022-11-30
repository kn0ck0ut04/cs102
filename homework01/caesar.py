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
    alph_len = ord("z") - ord("a") + 1

    for i in plaintext:
        if i.islower():
            index = (ord(i) - ord("a") + shift) % alph_len
            ciphertext += chr(ord("a") + index)
        elif i.isupper():
            index = (ord(i) - ord("A") + shift) % alph_len
            ciphertext += chr(ord("A") + index)
        else:
            ciphertext += i
            continue
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
    plaintext = encrypt_caesar(ciphertext, ord("z") - ord("a") - shift + 1)
    return plaintext


print(encrypt_caesar("PYTHON python3.6"))

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
        if i.isupper == False and i.islower == False:
            ciphertext += i
            continue
        if i.islower:
            index = (ord(i) - ord("a") + shift) % len(lowercase)
            ciphertext += chr(ord("a") + index)
        elif i.isupper:
            index = (ord(i) - ord("A") + shift) % len(highercase)
            ciphertext += chr(ord("A") + index)
    return ciphertext

print(encrypt_caesar('python'))
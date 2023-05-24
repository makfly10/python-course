def caesar_encrypt(message: str, n: int) -> str:
    """Encrypt message using caesar cipher

    :param message: message to encrypt
    :param n: shift
    :return: encrypted message
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lookup = {letter: i for i, letter in enumerate(alphabet)}

    encrypted = ''
    for char in message:
        if char.isalpha():
            is_upper = char.isupper()
            char_index = lookup[char.lower()]
            shifted_index = (char_index + n) % 26
            shifted_char = alphabet[shifted_index]
            encrypted += shifted_char.upper() if is_upper == True else shifted_char
        else:
            encrypted += char

    return encrypted

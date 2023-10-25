def decode(encoded):
    for i in encoded:
        decreased_digit = str(((int(i) - 3) % 10))
        encoded += decreased_digit
        return decoded_pass
def hex_to_bytes(hex_str):
    return bytes.fromhex(hex_str)

def xor_bytes_with_single_byte(data, key_byte):
    return bytes(b ^ key_byte for b in data)

def score_text(text):
    english_freq = {
        'a': 0.082, 'b': 0.015, 'c': 0.028, 'd': 0.043, 'e': 0.127,
        'f': 0.022, 'g': 0.02, 'h': 0.061, 'i': 0.07, 'j': 0.0015,
        'k': 0.0077, 'l': 0.04, 'm': 0.024, 'n': 0.067, 'o': 0.075,
        'p': 0.019, 'q': 0.00095, 'r': 0.06, 's': 0.063, 't': 0.091,
        'u': 0.028, 'v': 0.0098, 'w': 0.024, 'x': 0.0015, 'y': 0.02,
        'z': 0.00074, ' ': 0.1918
    }

    return sum(english_freq.get(chr(byte), 0) for byte in text.lower())

def single_byte_xor_cipher(hex_str):
    ciphertext = hex_to_bytes(hex_str)
    best_score = -1
    best_key: int = None # type: ignore
    best_plaintext: bytes = None # type: ignore

    for key in range(256):
        plaintext = xor_bytes_with_single_byte(ciphertext, key)
        score = score_text(plaintext)

        if score > best_score:
            best_score = score
            best_key = key
            best_plaintext = plaintext

    return best_key, best_plaintext.decode('ascii')

hex_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
key, plaintext = single_byte_xor_cipher(hex_str)
print(f"Key: {chr(key)} ({key})")
print(plaintext)

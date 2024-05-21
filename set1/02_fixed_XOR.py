def fixed_xor(hex_str1, hex_str2):
    bytes1 = bytes.fromhex(hex_str1)
    bytes2 = bytes.fromhex(hex_str2)

    xor_bytes = bytes(b1 ^ b2 for b1, b2 in zip(bytes1, bytes2))

    return xor_bytes.hex()

hex_str1 = "1c0111001f010100061a024b53535009181c"
hex_str2 = "686974207468652062756c6c277320657965"

output = fixed_xor(hex_str1, hex_str2)
print(output)

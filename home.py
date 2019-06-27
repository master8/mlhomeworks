import codecs

# TASK 1

hex = '49276d207374756479696e672043727970746f677261706879206c696b6520436c6175646520456c776f6f64205368616e6e6f6e21'
# b64 = codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()
# print('SSdtIHN0dWR5aW5nIENyeXB0b2dyYXBoeSBsaWtlIENsYXVkZSBFbHdvb2QgU2hhbm5vbiE=' == b64.strip())

base64_index_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def hex_to_base64(hex: str):
    input_bytes = bytes.fromhex(hex)
    encoded_output = ''

    bit_list = ''.join([bin(byte)[2:].zfill(8) for byte in input_bytes])

    chunks = [bit_list[i:i + 6] for i in range(0, len(bit_list), 6)]

    for chunk in chunks:

        # Checks the length of the chunk, adding trailing zeroes, mapping the
        # value to the b64_index_table, and adding '=' characters as necessary.
        if len(chunk) == 2:
            if '1' in chunk:
                chunk += '0000'
                encoded_output += base64_index_table[int(chunk, 2)] + '=='
            else:
                encoded_output += '=='
        elif len(chunk) == 4:
            if '1' in chunk:
                chunk += '00'
                encoded_output += base64_index_table[int(chunk, 2)] + '='
            else:
                encoded_output += '='
        elif len(chunk) == 6:
            encoded_output += base64_index_table[int(chunk, 2)]
    return encoded_output


print('SSdtIHN0dWR5aW5nIENyeXB0b2dyYXBoeSBsaWtlIENsYXVkZSBFbHdvb2QgU2hhbm5vbiE=' == hex_to_base64(hex))



# TASK 2


hex_one = '506561636520416c6c204f7665722054686520576f726c64'
hex_two = '4949544353551c0111001f010100061a021f010100061a02'


def xor(hex_one: str, hex_two: str):
    input_bytes_1 = bytes.fromhex(hex_one)
    input_bytes_2 = bytes.fromhex(hex_two)

    return bytes([b1 ^ b2 for b1, b2 in zip(input_bytes_1, input_bytes_2)]).hex()


print('192C352036755D6D7D2050776472264E6A7A21566F747666'.lower() == xor(hex_one, hex_two))



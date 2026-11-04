byte1 = 0b10101010
byte2 = 0b01010101

def parity(byte1, byte2):
    return  byte1 ^ byte2
final_byte = bytes([byte1, byte2, parity(byte1, byte2)])
output_binary = ''.join(f'{byte:08b}' for byte in final_byte)
print(final_byte)
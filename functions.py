def transmit_bytes(byte1, byte2): 
    return ''.join(f'{byte:08b}' for byte in (byte1, byte2, byte1 ^ byte2))
#print(transmit_bytes(0b10101010, 0b01010101)) #testfunction
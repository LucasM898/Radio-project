import os
def transmit_bytes(byte1, byte2): 
    return ''.join(f'{byte:08b}' for byte in (byte1, byte2, byte1 ^ byte2))
#print(transmit_bytes(0b10101010, 0b01010101)) #testfunction

#play tone??? idk if it works
def play_tone(frequency, duration=1/1200):
    os.system(f"play -n synth {duration} sine {frequency}")
def play_bit(bit):
    if bit == 1:
        play_tone(2200)
    else:
        play_tone(1200)
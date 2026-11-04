import os

def get_payload(string):
    result = ""
    for char in string:
        number = ord(char)
        bits = format(number, '08b')
        result = result + bits
    return result

#play tone??? idk if it works
def play_tone(frequency, duration=1/1200):
    os.system(f"play -n synth {duration} sine {frequency}")

#plays frequency based on bit
def play_bit(bit):
    if bit == 1:
        play_tone(2200)
    else:
        play_tone(1200)
print(get_payload('chatgpt is retarded'))
from functions import get_payload

chunks = []
raw = input("input string you tard: ")
final = ""
for x in range(0, len(raw), 32):
    chunk = raw[x:x+32]
    chunks.append(chunk)
packetnumber = 1
for chunk in chunks:
    transmit = ''
    transmit += format(packetnumber, '08b')
    packetnumber += 1
    transmit += get_payload(chunk)
    transmit = transmit.ljust(512, '0')
    print(transmit)




print("Input emoji, otherwise write 0 for poop default")
inputy = input()
if inputy == "0":
    emoji = "💩"
else:
    emoji = inputy

byte = bytes(emoji, 'utf-8')
if byte.__len__() < 4:  # checks if too few bytes, adds 0 if too short
    byte += bytes([0])


ip = str(byte[0]) + "." + str(byte[1]) + "." + str(byte[2]) + "." + str(byte[3])
print(emoji, "\n", ip)

emoji = "💩"
print("Input emoji, otherwise write 0 for poop default")
if input() == "0":
    emoji = "💩"
else:
    emoji = input()  # throws error because enter too much

byte = bytes(emoji, 'utf-8')
ip = str(byte[0]) + "." + str(byte[1]) + "." + str(byte[2]) + "." + str(byte[3])
print(ip)

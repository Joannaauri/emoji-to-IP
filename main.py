a = "💩"
print(a)
b = bytes(a, 'utf-8')
ip = str(b[0]) + "." + str(b[1]) + "." + str(b[2]) + "." + str(b[3])
print(ip)

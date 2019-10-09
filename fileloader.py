f = open("file", 'r')
while True:
    piece = f.read(128)
    if not piece:
        break
    print(str("chunk:") + str(piece))
f.close()
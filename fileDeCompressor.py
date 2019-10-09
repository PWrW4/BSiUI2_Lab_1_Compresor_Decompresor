import math

f = open("4char_100MB.dat", 'r')

# dictionary length
x = ord(f.read(1))

# number of bits that represent one dictionary char
N = math.ceil(math.log(x, 2))

# array for setting chars
dict_array = [0] * 256

# text length
k = 0

while True:
    piece = f.read(1)
    if not piece:
        break
    k = k + 1
    dict_array[int(ord(piece))] = 1

print(k)
print(dict_array)
f.close()

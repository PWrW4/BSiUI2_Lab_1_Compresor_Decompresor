import numpy as np
import sys
import math

file_in_name = "4char_100MB.dat"
file_out_name = "4char_100MB.wwc"

f = open(file_in_name, 'rb')
o = open(file_out_name, 'wb')

# array for setting chars
dict_array = [0] * 256

# dict length
x = 0

# text length
k = 0

while True:
    piece = f.read(1)
    if not piece:
        break
    dict_array[int(ord(piece))] = 1
    k = k + 1

f.close()

f = open(file_in_name, 'r')

# dictionary length
x = dict_array.count(1)

# number of bits that represent one dictionary char
N = math.ceil(math.log(x, 2))

if x >= 128:
    f.close()
    o.close()
    print("to many chars, compression doesnt make any sens")
    sys.exit()

chars_in_int_array = np.where(np.array(dict_array) == 1)[0]

o.write(bytes([x]))

o.write(bytes(list(chars_in_int_array)))

# rest of bits at the end of file
R = (8 - (3 + (k * N)) % 8) % 8

str_to_write = str(bin(R)[2:])


while True:
    piece = f.read(1)
    if not piece:
        break
    if len(str_to_write) >= 8:
        o.write(bytes([int(str_to_write[:8], 2)]))
        str_to_write = str_to_write[8:]
    piece_ascii = ord(piece)
    piece_order = list(chars_in_int_array).index(piece_ascii)
    str_to_write += bin(piece_order)[2:]

while len(str_to_write) > 0:
    o.write(bytes([int(str_to_write[:8], 2)]))
    str_to_write = str_to_write[8:]

f.close()
o.close()

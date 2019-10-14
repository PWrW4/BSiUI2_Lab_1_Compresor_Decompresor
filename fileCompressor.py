import numpy as np
import sys
import math

file_in_name = "test"  # test is from laboratory example
file_out_name = "test.wca"  # Wojciech compression algorithm xD

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

print("Liczba znaków: " + str(x))
print("Liczba potrzebnych bitów na jeden znak: " + str(N))
print("Długość tekstu: " + str(k))
print("Nadmiarowe bity: " + str(R))

str_to_write = format(R, '03b')

while True:
    piece = f.read(1)
    if not piece:
        break
    if len(str_to_write) >= 8:
        o.write(bytes([int(str_to_write[:8], 2)]))
        str_to_write = str_to_write[8:]
    piece_ascii = ord(piece)
    piece_order = list(chars_in_int_array).index(piece_ascii)
    str_to_write += format(piece_order, '02b')

if len(str_to_write) != 0:
    while len(str_to_write) != 8:
        str_to_write += '1'

    o.write(bytes([int(str_to_write[:8], 2)]))
    str_to_write = str_to_write[8:]

f.close()
o.close()

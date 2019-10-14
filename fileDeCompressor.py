import math

file_without_extension = 'test'  # file base name

file_in_name = file_without_extension + '.wca'  # Wojciech compression algorithm xD
file_out_name = file_without_extension + '_DeCompressed'  # out file

in_file = open(file_in_name, 'rb')
out_file = open(file_out_name, 'wb')

# dict length
x = int.from_bytes(in_file.read(1), byteorder='big')

# number of bits that represent one dictionary char
N = math.ceil(math.log(x, 2))

file_dict = {}

for i in range(x):
    file_dict.update({format(i, '0' + str(N) + 'b'): chr(int.from_bytes(in_file.read(1), byteorder='big'))})

print('Dict from file: ' + str(file_dict))
print('Dict length: ' + str(x))
print('Dict one char length in bits in input file: ' + str(N))

bytes_from_file_buffer = format(int.from_bytes(in_file.read(1), byteorder='big'), '08b')

# rest bytes at the end of file (not information, just filling to 8 bits in compression)
R = int(bytes_from_file_buffer[:3], 2)

bytes_from_file_buffer = bytes_from_file_buffer[3:]

while True:
    piece = in_file.read(1)
    if not piece:
        break
    bytes_from_file_buffer += format(int.from_bytes(piece, byteorder='big'), '08b')
    while len(bytes_from_file_buffer) > 8:
        out_file.write(file_dict.get(bytes_from_file_buffer[:N]).encode('ascii'))
        bytes_from_file_buffer = bytes_from_file_buffer[N:]

bytes_from_file_buffer = bytes_from_file_buffer[:len(bytes_from_file_buffer)-R]

while len(bytes_from_file_buffer) != 0:
    out_file.write(file_dict.get(bytes_from_file_buffer[:N]).encode('ascii'))
    bytes_from_file_buffer = bytes_from_file_buffer[N:]

in_file.close()
out_file.close()

print('Decompressed in file' + file_out_name)

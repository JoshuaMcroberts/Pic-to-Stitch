from tkinter import filedialog
# from import codecs encode

bytes_array = bytearray(b'')

# filename = "OSQ
# file = open("C:/Users/Joshu/Desktop/Decode Jef/"+ filename + ".txt", "r")

file_path = filedialog.askopenfilename()
byte_list = []

def readBytes(filename, nBytes):

    with open(filename, "rb") as file:

        while True:
            byte = file.read(1)

            if byte:
                yield byte
            else:
                break

            if nBytes > 0:
                nBytes -= 1
                if nBytes == 0:
                    break


for b in readBytes(file_path, -1):

    i = int.from_bytes(b, byteorder='big', signed=True)

    print(f"raw({b}) - int({i}) - hex({hex(i)})")
    byte_list.append(b)

print(byte_list)


# out[0] + out [1]      Offset
offset = byte_list[0:4]
print(offset)
del byte_list[0:4]
print(byte_list)


# out[2] + out [3]      Flags
flags_list = byte_list[0:4]
print(flags_list)
del byte_list[0:4]
print(byte_list)

# out[4] + out [5] + out[6] + out [7] Date
date_list = byte_list[0:8]
print(date_list)
del byte_list[0:8]
print(byte_list)

# out[8] + out [9] + out[10] + out [11] time
time_list = byte_list[0:8]
print(time_list)
del byte_list[0:8]
print(byte_list)

# out[12] + out[13]     Thread Changes
# out[14] + out [15]    Stitch count
# out[16] + out[17]     Hoop code

# out[18] + out [19]    Extent 1 left - in 0.1mm units
# out[20] + out [21]    Extent 1 top
# out[22] + out [23]    Extent 1 right
# out[24] + out [25]    Extent 1 bottom

# out[26] + out [27]    Extent 2 left - in 0.1mm units
# out[28] + out [29]    Extent 2 top
# out[30] + out [31]    Extent 2 right
# out[32] + out [33]    Extent 2 bottom

# out[34] + out [35]    Extent 3 left - in 0.1mm units
# out[36] + out [37]    Extent 3 top
# out[38] + out [39]    Extent 3 right
# out[40] + out [41]    Extent 3 bottom

# out[42] + out [43]    Extent 4 left - in 0.1mm units
# out[44] + out [45]    Extent 4 top
# out[46] + out [47]    Extent 4 right
# out[48] + out [49]    Extent 4 bottom

# out[50] + out [51]    Extent 5 left - in 0.1mm units
# out[52] + out [53]    Extent 5 top
# out[54] + out [55]    Extent 5 right
# out[56] + out [57]    Extent 5 bottom

# out[58] + out[59]    Colour change List
# n ~
# out[n] + out[n+1]

# out[n+2] + out[n+3]   0d00 0000 matching change list
# l = n ~
# out[l+2] + out[l+3]

# out[l+4] if 80** then l+5 yx
#           else: yx

# bytes_array.append(str(byte))

    # print(int.from_bytes(b'\x00\x01', "big"))                      # 1
    # print(int.from_bytes(b'\x00\x01', "little"))                   # 256
    #
    # print(int.from_bytes(b'\x00\x10', byteorder='little'))            # 4096
    # print(int.from_bytes(b'\xfc\x00', byteorder='big', signed=True))  #-1024
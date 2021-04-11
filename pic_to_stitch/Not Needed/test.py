from tkinter import filedialog
# from import codecs encode


jan_colour = ["Black", "White", "Yellow", "Orange", "Olive Green", "Green", "Sky", "Purple", "Pink", "Red", "Brown",
              "Blue", "Gold", "Dark Brown", "Pale Violet", "Pale Yellow", "Pale Pink", "Peach", "Beige", "Wine Red",
              "Pale Sky", "Yellow Green", "Silver Gray", "Gray", "Pale Aqua", "Baby Blue", "Powder Blue",
              "Bright Blue", "Slate Blue", "Navy Blue", "Salmon Pink", "Coral", "Burnt Orange", "Cinnamon", "Umber",
              "Blond", "Sunflower", "Orchid Pink", "Peony Purple", "Burgundy", "Royal Purple", "Cardinal Red",
              "Opal Green", "Moss Green", "Meadow Green", "Dark Green", "Aquamarine", "Emerald Green", "Peacock Green",
              "Dark Gray", "Ivory White", "Hazel", "Toast", "Salmon", "Cocoa Brown", "Sienna", "Sepia", "Dark Sepia",
              "Violet Blue", "Blue Ink", "Solar Blue", "Green Dust", "Crimson", "Floral Pink", "Wine", "Olive Drab",
              "Meadow", "Mustard", "Yellow Ocher", "Old Gold", "Honey Dew", "Tangerine", "Canary Yellow",
              "Vermilion", "Bright Green", "Ocean Blue", "Beige Gray", "Bamboo"]

bytes_array = bytearray(b'')

# filename = "OSQ
# file = open("C:/Users/Joshu/Desktop/Decode Jef/"+ filename + ".txt", "r")

file_path = filedialog.askopenfilename()
byte_list = []


def read_bytes(filename, nbytes):

    with open(filename, "rb") as file:

        while True:
            byte = file.read(1)

            if byte:
                yield byte
            else:
                break

            if nbytes > 0:
                nbytes -= 1
                if nbytes == 0:
                    break


def process_bytes():
    for b in read_bytes(file_path, -1):

        # i = int.from_bytes(b, byteorder='big', signed=True)
        # print(f"raw({b}) - int({i}) - hex({hex(i)})")

        byte_list.append(b)

    # print("byte_list:\n{}\n".format(byte_list))

    test = 0
    # Offset - Header Size - byte index of first stitch directly after 0d00 0000 section
    offset = byte_list[0:4]
    offset_byte = b"".join(offset)
    offset_int = int.from_bytes(offset_byte, byteorder='little', signed=True)
    del byte_list[0:4]
    print_offset = "Offset:\n  " + str(offset_int)
    if test == 1:
        print("offset_list:\n{}".format(offset))
        print("byte_list:\n{}\n".format(byte_list))

    # Flags
    flags_list = byte_list[0:4]
    flags_byte = b"".join(flags_list)
    flags_int = int.from_bytes(flags_byte, byteorder='little', signed=True)
    del byte_list[0:4]
    print_flags = "Flag:\n  " + str(flags_int)

    if test == 1:
        print("flags_list:\n{}".format(flags_list))
        print("flags_byte: {} flags_int: {}\n".format(flags_byte, flags_int))
        # print("byte_list:\n{}\n".format(byte_list))

    # Date
    date_list = byte_list[0:8]
    print_date = "Date:\n  "
    for i in date_list:
        print_date += i.decode("utf-8")
    # print_date += "\n"
    del byte_list[0:8]
    if test == 1:
        print("date_list:\n{}".format(date_list))
        # print("byte_list:\n{}\n".format(byte_list))

    # Time
    time_list = byte_list[0:8]
    print_time = "Time:\n  "
    for i in time_list:
        print_time += i.decode("utf-8")
    # print_time += "\n"
    del byte_list[0:8]
    if test == 1:
        print("time_list:\n{}".format(time_list))
        # print("byte_list:\n{}\n".format(byte_list))

    # Thread Changes
    thread_list = byte_list[0:4]
    thread_byte = b"".join(thread_list)
    thread_int = int.from_bytes(thread_byte, byteorder='little', signed=True)
    del byte_list[0:4]

    print_thread_count = "Thread Count:\n  " + str(thread_int)

    if test == 1:
        print("thread_list:\n{}".format(thread_list))
        # print("byte_list:\n{}\n".format(byte_list))

    # Stitch count
    count_list = byte_list[0:4]
    count_byte = b"".join(count_list)
    count_int = int.from_bytes(count_byte, byteorder='little', signed=True)
    del byte_list[0:4]

    print_stitch_count = "Stitch Count:\n  " + str(count_int) + "\n"

    if test == 1:
        print("count_list:\n{}".format(count_list))
        # print("byte_list:\n{}\n".format(byte_list))

    # Hoop code
    hoop_list = byte_list[0:4]

    del byte_list[0:4]
    if test == 1:
        print("hoop_list:\n{}".format(hoop_list))
        # print("byte_list:\n{}\n".format(byte_list))

    # Extent Section
    ext_list = byte_list[0:80]
    del byte_list[0:80]
    count = 0
    print_ext_list = []
    for i in range(5):

        extent = "Extent {}\n  ".format(count+1)

        # Left
        ext_left = ext_list[0:4]
        # print(ext_left)
        left_byte = b''.join(ext_left)
        left = str(int.from_bytes(left_byte, "little", signed=True))

        ext = 0
        while ext != 1:
            if len(left) < 11:
                left += " "
            else:
                ext = 1

        extent += "Left:   " + str(left)

        # Top
        ext_top = ext_list[4:8]
        # print(ext_top)
        top_byte = b''.join(ext_top)
        top = str(int.from_bytes(top_byte, "little", signed=True))

        ext = 0
        while ext != 1:
            if len(top) < 11:
                top += " "
            else:
                ext = 1

        extent += "Top:    " + str(top)

        # Right
        ext_right = ext_list[8:12]
        # print(ext_right)
        right_byte = b''.join(ext_right)
        right = str(int.from_bytes(right_byte, "little", signed=True))

        ext = 0
        while ext != 1:
            if len(right) < 11:
                right += " "
            else:
                ext = 1

        extent += "Right:  " + str(right)

        # Bottom
        ext_bottom = ext_list[12:16]
        # print(ext_bottom)
        bottom_byte = b''.join(ext_bottom)
        bottom = str(int.from_bytes(bottom_byte, "little", signed=True))

        ext = 0
        while ext != 1:
            if len(bottom) < 11:
                bottom += " "
            else:
                ext = 1

        extent += "Bottom: " + str(bottom)

        print_ext_list.append(extent)
        count += 1

        del ext_list[0:16]

    print_ext_list.append("\n")

    if test == 1:

        print("ext_list:\n{}".format(ext_list))
        print("byte_list:\n{}\n".format(byte_list))

    # out[58] + out[59]    Colour change List
    # n ~
    # out[n] + out[n+1]
    # out[n+2] + out[n+3]   0d00 0000 matching change list
    #     # l = n ~
    #     # out[l+2] + out[l+3]
    print_colour_list = "Colour Change List:\n  "
    byte = byte_list[0]
    count = 0
    xd_list = "Repeat 0d00 0000:(+1 for each colour change)\n  "
    while byte != b'\r':
        colour_byte_list = byte_list[0:4]
        del byte_list[0:4]

        colour_byte = b''.join(colour_byte_list)
        colour = int.from_bytes(colour_byte, "little")

        colour_name = jan_colour[colour - 1]
        ext = 0
        while ext != 1:
            if len(colour_name) < 15:
                colour_name += " "
            else:
                ext = 1
        print_colour_list += colour_name
        xd_list += "0d00 0000      "
        count += 1
        if count % 4 == 0:
            print_colour_list += "\n  "
            xd_list += "\n  "
        byte = byte_list[0]

    print_colour_list += "\n"
    xd_list += "\n  "

    # print(count)
    # print(print_colour_list)

    # out[l+4] if 80** then l+5 yx
    #           else: yx

    print_yx = "Stitching Co-ordinates (y,x):\n  "
    count = 0
    ext = 0
    while ext != 1:
        b = byte_list[count]

        if b == b'\x80':  # if command

            instr_byte = byte_list[count + 1]

            if instr_byte == b'\x01':
                print_yx += "(Colour...  "
                # print("Colour Count: {} ".format(count))
                count += 2
                if count % 16 == 0:
                    print_yx += "\n  "
                print_yx += "...Change)  "
                count += 1
                # print("Count: {} ".format(count))

            elif instr_byte == b'\x02':

                x_byte = int.from_bytes(byte_list[count + 2], "little", signed=True)
                y_byte = int.from_bytes(byte_list[count + 3], "little", signed=True)
                # del byte_list[0]
                # del byte_list[1]
                pad = " "
                y_str = str(y_byte)
                # print(len(y_str))
                if len(y_str) == 1:
                    pad += "   "
                if len(y_str) == 2:
                    pad += "  "
                if len(y_str) == 3:
                    pad += " "
                x_str = str(x_byte)
                # print("Count: {} Y: {} X: {}".format(count, len(y_str), len(x_str)))
                if len(x_str) == 1:
                    pad += "   "
                if len(x_str) == 2:
                    pad += "  "
                if len(x_str) == 3:
                    pad += " "

                print_yx += "(Jump -> )  "
                # print("Jump Count: {} ".format(count))
                count += 2
                if count % 16 == 0:
                    print_yx += "\n  "
                print_yx += "(" + y_str + "," + x_str + ")" + pad
                count += 1
                # print("Count: {} ".format(count))
            else:
                print_yx += "(End)"
                break

        else:
            x_byte = int.from_bytes(byte_list[count], "little", signed=True)
            y_byte = int.from_bytes(byte_list[count + 1], "little", signed=True)
            count += 1
            # del byte_list[0]
            # del byte_list[1]
            pad = " "
            y_str = str(y_byte)
            # print(len(y_str))
            if len(y_str) == 1:
                pad += "   "
            if len(y_str) == 2:
                pad += "  "
            if len(y_str) == 3:
                pad += " "
            x_str = str(x_byte)
            # print("Count: {} Y: {} X: {}".format(count, len(y_str), len(x_str)))
            if len(x_str) == 1:
                pad += "   "
            if len(x_str) == 2:
                pad += "  "
            if len(x_str) == 3:
                pad += " "

            print_yx += "(" + y_str + "," + x_str + ")" + pad
            # print(b)
            # print(byte_list)
        count += 1

        if count % 16 == 0:
            print_yx += "\n  "
    print(print_offset)
    print(print_flags)
    print(print_date)
    print(print_time)
    print(print_thread_count)
    print(print_stitch_count)
    for i in print_ext_list:
        print(i)
    print(print_colour_list)
    print(xd_list)
    # print(print_yx)

process_bytes()

# print(b'\x0d')
# print(int.from_bytes(b'\xff\xff\xff\xff', "big"))                      # 1
# print(int.from_bytes(b'\xff\xff\xff\xff', "little"))                   # 256
# print(int.from_bytes(b'\xff\xff\xff\xff', "big", signed=True))                      # 1
# print(int.from_bytes(b'\x7f\x7f\x7f\x7f', "little", signed=True))
# print(int.from_bytes(b'\x80', byteorder='big', signed=True))  #-1024
# print(int.from_bytes(b'\x00', byteorder='little', signed=True))            # 4096
# print(int.from_bytes(b'\x80', byteorder='big'))  #-1024
# print(int.from_bytes(b'\x00', byteorder='little'))            # 4096
# #
# import datetime
#
# date = datetime.datetime.now()
#
# print(str(date.strftime("%Y%m%d")))
# print(str(date.strftime("%H%M%S") + "00"))

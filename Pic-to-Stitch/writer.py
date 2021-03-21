import tkinter as tk
from tkinter import filedialog
from tkinter import *


# filename = "tm"
# file = open("C:/Users/Joshu/Desktop/" + filename + ".jef", "wb")
# #
# #
# int_1 = [124, 0, 0, 0, 20, 0, 0, 16, 65, 0, 0, 1, 200, 34, 20, 0, 0, 16, 65, 0, 0, 1]
# # words = ["t", "h", "i", "s", "t", "h", "e", "t", "i", "m", "e", "2", "0", ":", "0", "0"]
# # word = "2021"


def write_to_file(mata_file):
    test = 1
    f = filedialog.asksaveasfilename(defaultextension=".jef", filetypes=(("Janome (*.jef)", ".jef"),))
    f = open(f, 'wb')
    if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return

    # print(four_byte_int(20))
    # print(co_or_byte((23, -68)))


    # write all bytes here

    # offset
    offset = mata_file.offset
    w_byte = four_byte_int(offset)
    f.write(w_byte)

    # flags
    flag = mata_file.flags
    w_byte = four_byte_int(flag)
    f.write(w_byte)

    # date - set
    date = mata_file.date
    f.write(bytes(date, 'ascii'))

    # time - set
    time = mata_file.time
    f.write(bytes(time, 'ascii'))

    # thread count
    thread_count = mata_file.thread_count
    w_byte = four_byte_int(thread_count)
    f.write(w_byte)

    # stitch count
    stitch_count = mata_file.stitch_count
    w_byte = four_byte_int(stitch_count)
    f.write(w_byte)

    # hoop code
    hoop_code = mata_file.hoop_code
    w_byte = four_byte_int(hoop_code)
    f.write(w_byte)

    # extents
    entent1_list = mata_file.extent1
    for item in entent1_list:
        w_byte = four_byte_int(item)
        f.write(w_byte)

    entent2_list = mata_file.extent2
    for item in entent2_list:
        w_byte = four_byte_int(item)
        f.write(w_byte)

    entent3_list = mata_file.extent3
    for item in entent3_list:
        w_byte = four_byte_int(item)
        f.write(w_byte)

    entent4_list = mata_file.extent4
    for item in entent4_list:
        w_byte = four_byte_int(item)
        f.write(w_byte)

    entent5_list = mata_file.extent1
    for item in entent5_list:
        w_byte = four_byte_int(item)
        f.write(w_byte)

    # colour change list
    col_change_list = mata_file.colour_change
    for item in col_change_list:
        w_byte = four_byte_int(item)
        f.write(w_byte)

    # 0d00 0000's
    for i in range(len(col_change_list)):
        f.write(b'\x0d\x00\x00\x00')


    # xy's
    jump_lists = mata_file.emb_jump_to_lists
    stitch_lists = mata_file.emb_stitch_lists

    for i, jump_list in enumerate(jump_lists):
        if i != 0:
            f.write(b'\x80\x01\x00\x00')
        # - jump_list
        for jump in jump_list:
            j_byte = co_or_byte(jump)
            f.write(b'\x80\x02')
            for j in j_byte:
                f.write(j)

        stitch_list = stitch_lists[i]
        for stitch in stitch_list:
            s_byte = co_or_byte(stitch)
            for s in s_byte:
                f.write(s)

            # 8001 0000 at start
            # 8002 then xy
        # - stitch list
    f.write(b'\x80\x10')
    # End 8010


    f.close()


def four_byte_int(val):     # returns byte to be written
    val = val.to_bytes(4, byteorder='little', signed=True)
    return val


def co_or_byte(co_or):      # returns byte to be written
    x_co, y_co = co_or
    n_x = x_co.to_bytes(1, byteorder='little', signed=True)
    n_y = y_co.to_bytes(1, byteorder='little', signed=True)
    return n_x, n_y








# file.write(bytes(word, 'utf-8'))


# file.write(bytes(word, 'ascii'))
#
# file.close()
#
# write_to_file(0)

def write_to_file(mata_file, file_path):
    test = 0
    if test == 5:
        print("write_to_file - writer.py")

    f = open(file_path, 'wb')

    # write all bytes here

    # offset
    offset = mata_file.get_offset()
    w_byte = four_byte_int(offset)
    f.write(w_byte)

    # flags
    flag = mata_file.get_flags()
    w_byte = four_byte_int(flag)
    f.write(w_byte)

    # date - set
    date = mata_file.get_date()
    f.write(bytes(date, 'ascii'))

    # time - set
    time = mata_file.get_time()
    f.write(bytes(time, 'ascii'))

    # thread count
    thread_count = mata_file.get_thread_count()
    w_byte = four_byte_int(thread_count)
    f.write(w_byte)

    # stitch count
    stitch_count = mata_file.get_stitch_count()
    w_byte = four_byte_int(stitch_count)
    f.write(w_byte)

    # hoop code
    hoop_code = mata_file.get_hoop_code()
    w_byte = four_byte_int(hoop_code)
    f.write(w_byte)

    # extents
    extent_1_list = mata_file.get_extent_1()
    for item in extent_1_list:
        w_byte = four_byte_int(item)
        f.write(w_byte)

    extent_2_list = mata_file.get_extent_2()
    for item in extent_2_list:
        w_byte = four_byte_int(item)
        f.write(w_byte)

    extent_3_list = mata_file.get_extent_3()
    for item in extent_3_list:
        w_byte = four_byte_int(item)
        f.write(w_byte)

    extent_4_list = mata_file.get_extent_4()
    for item in extent_4_list:
        w_byte = four_byte_int(item)
        f.write(w_byte)

    extent_5_list = mata_file.get_extent_5()
    for item in extent_5_list:
        w_byte = four_byte_int(item)
        f.write(w_byte)

    # colour change list
    col_change_list = mata_file.get_colour_change()
    for item in col_change_list:
        w_byte = four_byte_int(item)
        f.write(w_byte)

    # 0d00 0000's
    for i in range(len(col_change_list)):
        f.write(b'\x0d\x00\x00\x00')

    # xy's
    jump_lists = mata_file.get_emb_jump_to_lists()
    stitch_lists = mata_file.get_emb_stitch_lists()

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
    test = 0
    if test == 5:
        print("four_byte_int - writer.py")
    val = val.to_bytes(4, byteorder='little', signed=True)
    return val


def co_or_byte(co_or):      # returns byte to be written
    test = 0
    if test == 5:
        print("co_or_byte - writer.py")
    x_co, y_co = co_or
    n_x = x_co.to_bytes(1, byteorder='little', signed=True)
    n_y = y_co.to_bytes(1, byteorder='little', signed=True)
    return n_x, n_y

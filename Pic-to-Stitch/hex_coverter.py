from tkinter import filedialog

# filename = "OSQ"
# file = open("C:/Users/Joshu/Desktop/Decode Jef/"+ filename + ".txt", "r")

file_path = filedialog.askopenfilename()
file = open(file_path)

content = file.read()
coor = ""
content_list = content.split()
new_content_list = []
count = 0
s_dec = "null"
change = 0
last_dec = 0
print(content_list)
for x in content_list:
    if count == 8:
        count = 0
    print(x)
    word = list(x)
    n = 2
    out = [(word[i:i + n]) for i in range(0, len(word), n)]

    print_list = []
    # out[0] + out [1]      Offset
    i_list = [out.pop(0), out.pop(1)]
    for i in i_list:
        number = i
        hex_num1 = str(number[0])
        hex_num2 = str(number[1])
        dec1 = int(hex_num1, 16)
        dec2 = int(hex_num2, 16)

        val = "Offset: {} Hex: {}\n".format(dec1, number)
        print(val)
        print_list.append(val)


    # out[2] + out [3]      Flags
    i_list = [out.pop(0), out.pop(1)]
    for i in i_list:
        number = i
        hex_num1 = str(number[0])
        hex_num2 = str(number[1])
        dec1 = int(hex_num1, 16)
        dec2 = int(hex_num2, 16)

        val = "Flags: {} Hex: {}\n".format(dec1, number)
        print(val)
        print_list.append(val)

    # out[4] + out [5] + out[6] + out [7] Date
    # out[8] + out [9] + out[10] + out [11] time
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



    # dec_list = []
    # for i in out:
    #     number = i
    #     hex_num = ""
    #     hex_num = hex_num + number[0]
    #     hex_num = hex_num + number[1]
    #     # print(hex_num)
    #     dec = int(hex_num, 16)
    #
    #     if dec == 128:
    #         change = 1
    #
    #     if change == 1:
    #         if dec == 0:
    #             pass
    #         elif dec == 128:
    #             pass
    #         elif last_dec == 128:
    #             pass
    #         else:
    #             dec = dec - 128
    #
    #     if dec < 0:
    #         if dec > -10:
    #             s_dec = "00n" + str(dec*-1)
    #         elif dec > -100:
    #             s_dec = "0n" + str(dec*-1)
    #         else:
    #             s_dec = "n" + str(dec*-1)
    #     elif dec >= 0:
    #         if dec < 10:
    #             s_dec = "000" + str(dec)
    #         elif dec < 100:
    #             s_dec = "00" + str(dec)
    #         else:
    #             s_dec = "0" + str(dec)
    #     last_dec = dec
    #     dec_list.append(s_dec)
    #     # print(dec)

#
#
#     coor = coor + str(dec_list[0]) + "/" + str(dec_list[1])
#     count += 1
#     if count == 8:
#         coor = coor + "\n"
#     else:
#         coor = coor + " - "
#     # print(coor)
#         # =< 7 is + hex
#         # > 7 is - hex
#
# new_content_list.append(coor)
#
# new_content_list.append("word")
# filename = "hex"
# new_file = open("C:/Users/Joshu/Desktop/Decode Jef/" + filename + " DECODED.txt", "w+")
#
# # new_file = open("C:/Users/Joshu/Desktop/Decode Jef/" + filename + " COOR_DECODED.txt", "w+")
#
# for x in new_content_list:
#     new_file.write(x + "\n")
#
# new_file.close()

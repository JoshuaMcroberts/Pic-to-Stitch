filename = "OSQ"
file = open("C:/Users/Joshu/Desktop/Decode Jef/"+ filename + ".txt", "r")

content = file.read()
coor = ""
content_list = content.split()
new_content_list = []
count = 0
s_dec = "null"
change = 0
last_dec = 0
for x in content_list:
    if count == 8:
        count = 0
    print(x)
    word = list(x)
    n = 2
    out = [(word[i:i + n]) for i in range(0, len(word), n)]

    dec_list = []
    for i in out:
        number = i
        hex_num = ""
        hex_num = hex_num + number[0]
        hex_num = hex_num + number[1]
        # print(hex_num)
        dec = int(hex_num, 16)

        if dec == 128:
            change = 1

        if change == 1:
            if dec == 0:
                pass
            elif dec == 128:
                pass
            elif last_dec == 128:
                pass
            else:
                dec = dec - 128

        if dec < 0:
            if dec > -10:
                s_dec = "00n" + str(dec*-1)
            elif dec > -100:
                s_dec = "0n" + str(dec*-1)
            else:
                s_dec = "n" + str(dec*-1)
        elif dec >= 0:
            if dec < 10:
                s_dec = "000" + str(dec)
            elif dec < 100:
                s_dec = "00" + str(dec)
            else:
                s_dec = "0" + str(dec)
        last_dec = dec
        dec_list.append(s_dec)
        # print(dec)
    coor = coor + str(dec_list[0]) + "/" + str(dec_list[1])
    count += 1
    if count == 8:
        coor = coor + "\n"
    else:
        coor = coor + " - "
    # print(coor)
        # =< 7 is + hex
        # > 7 is - hex

new_content_list.append(coor)

new_content_list.append("word")

new_file = open("C:/Users/Joshu/Desktop/Decode Jef/" + filename + " COOR_DECODED.txt", "w+")

for x in new_content_list:
    new_file.write(x + "\n")

new_file.close()

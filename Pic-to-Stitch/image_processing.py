from PIL import Image, ImageTk, ImageFilter, ImageOps
import numpy as np

import plot_objects as po


def image_resize(main, image, hoop_size, option, new_w, new_h):
    test = 0
    if test == 5:
        print("image_resize image_processing.py")

    img_w, img_h = image.size
    px = 3.77
    new_w = float(new_w) * px
    new_h = float(new_h) * px
    new_w = int(new_w)
    new_h = int(new_h)

    if option == 1:

        if hoop_size == 1:
            main.hoop_code = 0
            if test == 1:
                print('4x4" hoop')
            set_w = 415
            set_h = 415
        elif hoop_size == 2:
            main.hoop_code = 1
            if test == 1:
                print('2x2" hoop')
            set_w = 188
            set_h = 188
        elif hoop_size == 3:
            main.hoop_code = 2
            if test == 1:
                print('5.5x8" hoop')
            set_w = 529
            set_h = 756
        elif hoop_size == 4:
            main.hoop_code = 3
            if test == 1:
                print('5x4" hoop')
            set_w = 476
            set_h = 415
        elif hoop_size == 5:
            main.hoop_code = 4
            if test == 1:
                print('8x8" hoop')
            set_w = 756
            set_h = 756
        else:
            set_w = 1
            set_h = 1

        if img_w > set_w:
            x = img_w / set_w
            temp_h = img_h / x
            img_h = int(temp_h)
            img_w = int(set_w)

        if img_h > new_h:
            x = img_h / set_h
            temp_w = img_w / x
            img_w = int(temp_w)
            img_h = int(set_h)

    elif option == 2:

        img_w = new_w
        img_h = new_h

    elif option == 3:

        x = img_w / new_w
        temp_h = img_h / x
        img_h = int(temp_h)
        img_w = int(new_w)

    elif option == 4:

        x = img_h / new_h
        temp_w = img_w / x
        img_w = int(temp_w)
        img_h = int(new_h)

    image = image.resize((int(img_w), int(img_h)), Image.ANTIALIAS)
    return image


# ** Working **
def auto_colour_step(main):
    test = 0
    if test == 5 or test == 1:
        print("auto_colour_step image_processing.py")

    bar_count = 0
    levels = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    main.bar("Colour Levels", "Processing Image...", len(levels), 1)
    main.bar_update_progress(0, 0, 1)

    main.temp_images.clear()

    if len(main.images) == 2:
        global pix
        pix = (0, 0, 0)
        for x in levels:
            floors = x
            image = main.images[1]

            pixel_matrix = np.array(image)
            image_copy = pixel_matrix.copy()

            for i, row in enumerate(pixel_matrix):

                for j, pix in enumerate(row):

                    if len(pix) == 4:
                        r, g, b, t = pix
                        pix = (r, g, b)

                    if pix[0] > 230 and pix[1] > 230 and pix[2] > 230:  # Near white equals white
                        pix = (255, 255, 255)
                    pix = list(pix)
                    comb_val = int(pix[0]) + int(pix[1]) + int(pix[2])
                    pix_val = 0
                    if pix[0] < 70:

                        if pix[1] < 70:

                            if pix[2] < 70:
                                pix_val = 1

                    val = 160
                    if comb_val < val and pix_val == 1:  # Near white equals white
                        pix = (0, 0, 0)

                    image_copy[i, j] = floor_step(pix, floors)

            temp = Image.fromarray(image_copy, "RGB")
            main.temp_images.append(temp)
            bar_count += 1

            main.bar_update_progress(bar_count, 0, 1)

            if test == 1:
                print("Image: ", x)

        if test == 1:
            print("**Finished Process**")
        main.bar_des()
        main.colour_select_pop()
    else:
        if test == 1:
            print("failed to run")


def floor_step(pixel, floors):
    test = 0
    if test == 5:
        print("floor_step gui.py")

    max_val = 2**8 - 1
    coarseness = max_val / floors

    return [coarseness * np.floor(val / coarseness) for val in pixel]


def pix_restrict(main):     # og first different colour
    test = 4
    if test == 5:
        print("pix_restrict image_processing.py")

    global pix
    if test == 1:
        print("image merge")

    if len(main.images) == 2:
        if test == 1:
            print("yup")

        image = main.images[1]
        pixel_matrix = np.array(image)
        image_copy = pixel_matrix
        delete_colour = []
        pixel_list = []
        colour_count = []
        pix_total = len(pixel_matrix) * len(pixel_matrix[0])

        # progress pop_up section
        msg_pix_total = pix_total
        msg_pix = 1
        msg_count = 1
        message = "Collecting Pixel Information..."
        main.bar("Colour Merge", message, msg_pix_total, 1)
        main.bar_update_progress(msg_count, 0, 0)
        # end

        for y, row in enumerate(pixel_matrix):

            # progress pop_up update
            msg = "Collecting Pixel Information... (Pixel: " + str(msg_pix) + " of " + str(msg_pix_total) + ")"
            main.bar_update_message(msg)
            main.bar_update_progress(msg_pix, 0, 1)
            # end

            for x, pix in enumerate(row):

                if test == 1:
                    print("(Y,X): ", y, ",", x)

                # count the number of times a pixel appears
                if len(pixel_list) == 0:
                    pixel_list.append(list(pix))
                    colour_count.append(1)
                else:
                    count = 0
                    for i in pixel_list:

                        if i[0] == pix[0]:
                            if i[1] == pix[1]:
                                if i[2] == pix[2]:
                                    index = pixel_list.index(i)

                                    ind = index

                                    colour_count[ind] += 1
                                else:
                                    count += 1
                            else:
                                count += 1
                        else:
                            count += 1

                        if count >= len(pixel_list):
                            pixel_list.append(list(pix))
                            colour_count.append(1)
                            break

                # progress pop_up count
                msg_pix += 1
                # end

        # print list of all individual colours
        if test == 1:
            e = 1
            for x in pixel_list:
                num = colour_count[e-1]
                print("Colour ", e, " Value: ", x, " Amount: ", num,)
                e += 1

        # progress pop_up reset
        msg_count = 0
        msg_colour_total = len(colour_count)
        msg = "Collecting Pixel Information... (Pixel: " + str(msg_pix) + " of " + str(msg_pix_total) + ")"
        main.bar_reset(msg, msg_count, len(colour_count), 1)
        # end

        # make a list of the colours that appear the least
        # make into a percentage formula
        # value = len(pixel_matrix) * len(pixel_matrix[0]) / colour
        # value = 2000
        value = pix_total / 100
        value = value * 4
        value = round(value)
        index_list = []
        for i in colour_count:

            # progress pop_up update
            msg = "Setting Delete Colours... (Deleted Colours: " + str(msg_count) + " of " + str(msg_colour_total) + ")"
            main.bar_update_message(msg)
            main.bar_update_progress(msg_count, 0.1, 1)
            # end

            if i <= value:
                index = colour_count.index(i)
                delete_colour.append(pixel_list[index])
                index_list.append(index)

                # progress pop_up count
                msg_count += 1
                # end

        # progress pop_up update/reset
        msg_count += msg_colour_total - msg_count
        main.bar_update_progress(msg_count, 0.1, 1)
        msg_pix_total = len(pixel_matrix) * len(pixel_matrix[0])
        msg_pix = 1
        msg_count = 1
        msg = "Removing Deleted Colours... (Pixel: " + str(msg_pix) + " of " + str(msg_pix_total) + ")"
        main.bar_reset(msg, msg_pix, msg_pix_total, 1)
        main.bar_update_progress(msg_count, 0, 1)
        # end

        # for each pixel in image
        colour_count.clear()
        pixel_list.clear()

        for y, row in enumerate(pixel_matrix):

            # progress pop_up update
            msg = "Removing Deleted Colours... (Pixel: " + str(msg_pix) + " of " + str(msg_pix_total) + ")"
            main.bar_update_message(msg)
            main.bar_update_progress(msg_pix, 0, 1)
            # end

            for x, pix in enumerate(row):
                # pic += 1
                # print("Pixel Count: ", pix)
                # check pixel against the delete list
                # if it needs to be deleted get surrounding pixels
                d = 0
                for i in delete_colour:
                    if i[0] == pix[0]:
                        if i[1] == pix[1]:
                            if i[2] == pix[2]:
                                pix = get_liner_pixel(pixel_matrix, y, x, delete_colour)

                    if test == 1:
                        str_i = str(i)
                        str_pix = str(pix)

                        while len(str_i) != 16 or len(str_i) > 16:
                            str_i += " "

                        while len(str_pix) != 16 or len(str_pix) > 16:
                            str_pix += " "

                        print("Deleted Value: {} New value: {} Count: {} ".format(str_i, str_pix, d))

                    image_copy[y, x] = pix
                    d += 1

                # progress pop_up count
                msg_pix += 1

        if test == 1:
            print("making image")
        out_img = Image.fromarray(image_copy, "RGB")
        main.undo_list.append(main.images[1])
        main.undo_function_list.append(3)
        if test == 4:
            print("3 - Functions so far: {}".format(main.undo_function_list))
        main.images[1] = out_img
        main.display_cy_image()

        # progress pop_up update/destroy
        msg_pix += msg_pix_total - msg_pix
        main.bar_update_progress(msg_pix, 0, 1)
        main.bar_des()
    else:
        if test == 1:
            print("Error: Pix_change failed")


def get_liner_pixel(pixel_matrix, y, x, deleted_list):
    test = 0
    if test == 5:
        print("get_liner_pixel image_processing.py")

    pixel_list = []
    count = 0
    option = 1

# get N E S W pixels that are valid and not black

    while option != 5:
        if count > 3:
            option = 5
            count = 0

            if test == 1:
                print("stuck in a loop on: ", y + 1, ",", x + 1, " Val :", pixel_matrix[y, x])

        if len(pixel_list) > 0:
            break

        if option == 1:

            nx = x - 1
            while nx >= 0:

                new_pix = pixel_matrix[y, nx]

                if new_pix[0] == 0 and new_pix[1] == 0 and new_pix[2] == 0:
                    option = 2
                    break

                bool_val = check_delete(deleted_list, new_pix)

                if bool_val:
                    nx -= 1
                else:
                    pixel_list.append(new_pix)
                    option = 2
                    break

        if option == 2:

            ny = y - 1
            while ny >= 0:

                new_pix = pixel_matrix[ny, x]

                if new_pix[0] == 0 and new_pix[1] == 0 and new_pix[2] == 0:
                    option = 3
                    break

                bool_val = check_delete(deleted_list, new_pix)

                if bool_val:
                    ny -= 1
                else:
                    pixel_list.append(new_pix)
                    option = 3
                    break

        if option == 3:

            nx = x + 1
            while nx < len(pixel_matrix[0]):

                new_pix = pixel_matrix[y, nx]

                if new_pix[0] == 0 and new_pix[1] == 0 and new_pix[2] == 0:
                    option = 4
                    break

                bool_val = check_delete(deleted_list, new_pix)

                if bool_val:
                    nx += 1
                else:
                    pixel_list.append(new_pix)
                    option = 4
                    break

        if option == 4:

            ny = y + 1
            if test == 1:
                print("ny:", ny, "pixel: ", pix, "new pixel: ", new_pix, "option: ", option)

            while ny < len(pixel_matrix):

                new_pix = pixel_matrix[ny, x]

                if new_pix[0] == 0 and new_pix[1] == 0 and new_pix[2] == 0:
                    option = 5
                    break

                bool_val = check_delete(deleted_list, new_pix)

                if bool_val:
                    ny += 1
                else:
                    pixel_list.append(new_pix)
                    option = 5
                    break

        count += 1  # ##### this needs checked to make sure the loop breaks

    if len(pixel_list) == 0:
        pixel = (0, 255, 50)
        if test == 1:
            print("black")

        return pixel

    else:
        colour_count = []
        count_list = []
        z = 0
        for e in pixel_list:

            if len(count_list) == 0:

                count_list.append(list(e))
                colour_count.append(1)

            count = 0
            for i in count_list:

                if i[0] == e[0]:
                    if i[1] == e[1]:
                        if i[2] == e[2]:
                            index = count_list.index(i)

                            ind = index

                            colour_count[ind] += 1
                        else:
                            count += 1
                    else:
                        count += 1
                else:
                    count += 1

                if count >= len(count_list):
                    count_list.append(list(e))
                    colour_count.append(1)
                    break
            z += 1
            if test ==1:
                print(z)

        pick = max(colour_count)
        ind = colour_count.index(pick)
        if test == 1:
            print("Pixel: ", count_list[ind])
        return count_list[ind]


def check_delete(deleted_list, pixel):
    test = 0
    if test == 5:
        print("check_delete image_processing.py")

    value = 0
    for i in deleted_list:

        if i[0] == pixel[0]:
            if i[1] == pixel[1]:
                if i[2] == pixel[2]:

                    value = 1
                    break

    if value == 1:
        return True
    else:
        return False


def pix_change(main):
    test = 1
    if test == 5:
        print("pix_change gui.py")

    global pix


    if len(main.images) == 2:

        image = main.images[1]
        pixel_matrix = np.array(image)
        image_copy = pixel_matrix.copy()
        row_num = len(pixel_matrix)
        col_num = len(pixel_matrix[0])
        total_pix = row_num * col_num

        message = "Running 3x3 Search..."
        main.bar("Denoise", message, total_pix, 1)
        main.bar_update_progress(0, 0, 1)

        # 3x3
        set_3 = 0
        msg_count = 0
        for y, row in enumerate(pixel_matrix):

            main.bar_update_progress(msg_count, 0, 1)

            for x, pix in enumerate(row):
                if test == 2:
                    print("X: ", x, "Pixel Matrix Height: ", len(pixel_matrix[0]))

                pixels, pixel_yx = get_surrounding_pixels_3x3(pixel_matrix, y, x)
                cur_pix = image_copy[y, x]

                # if cur_pix != in list:
                val = 0
                for i, pix_a in enumerate(pixels):
                    if cur_pix[0] == pix_a[0]:
                        if cur_pix[1] == pix_a[1]:
                            if cur_pix[2] == pix_a[2]:
                                val = 1
                                break
                # print("3x3")
                if val == 0:
                    pixel_list = []
                    colour_count = []
                    count_list = []
                    count_colour_list(pixels, pixel_list, colour_count, count_list)

                    if len(pixel_list) == 1:
                        image_copy[y, x] = pixel_list[0]
                        if test == 1:
                            print("3 Cur: {} set: {} Q".format(cur_pix, pixel_list[0]))
                            set_3 += 1

                            msg = "Running 3x3 Search...(Pixels Changed: " + str(set_3) + ")"
                            main.bar_update_message(msg)
                    else:
                        #    get inner lists
                        #    find most common pixel
                        max_colour = max(colour_count)
                        ind = colour_count.index(max_colour)
                        new_pixel = pixel_list[ind]

                        for j, l_pix in enumerate(pixels):

                            if l_pix[0] == cur_pix[0]:
                                if l_pix[1] == cur_pix[1]:
                                    if l_pix[2] == cur_pix[2]:
                                        img_y, img_x = pixel_yx[j]
                                        image_copy[img_y, img_x] = new_pixel
                                        if test == 1:
                                            print("3 Cur: {} set: {} L".format(cur_pix, new_pixel))
                                        set_3 += 1

                                        msg = "Running 3x3 Search...(Pixels Changed: " + str(set_3) + ")"
                                        main.bar_update_message(msg)
                msg_count += 1

        message = "Running 5x5 Search..."
        main.bar_reset(message, 0, total_pix, 1)

                        # break

        # 5x5
        set_a = 0
        count_a = 0
        msg_count = 0
        for y, row in enumerate(pixel_matrix):

            main.bar_update_progress(msg_count, 0, 1)

            for x, pix in enumerate(row):
                if test == 2:
                    print("X: ", x, "Pixel Matrix Height: ", len(pixel_matrix[0]))

                pixels_og, pixel_yx_og = get_surrounding_pixels_5x5(pixel_matrix, y, x)
                cur_pix = image_copy[y, x]

                # if cur_pix != in list:
                val = 0
                for i, pix_a in enumerate(pixels_og):
                    if cur_pix[0] == pix_a[0]:
                        if cur_pix[1] == pix_a[1]:
                            if cur_pix[2] == pix_a[2]:
                                val = 1
                                break
               # print("5x5")
                if val == 0:
                    pixels, pixel_yx = get_surrounding_pixels_3x3(pixel_matrix, y, x)
                    pixel_yx_og += pixel_yx
                    pixels_og += pixels

                    pixel_yx_og.append((y, x))
                    pixels_og.append(tuple(image_copy[y, x]))

                    pix_3x3 = pixels
                    pixel_list = []
                    colour_count = []
                    count_list = []
                    count_colour_list(pixels_og, pixel_list, colour_count, count_list)

                    ext = 0
                    while ext != 1:
                        max_colour = max(colour_count)  # get max colour
                        ind = colour_count.index(max_colour)  # get max colour index
                        new_pix = pixel_list[ind]  # get max colour value using index

                        n_m = 0
                        for j, l_pix in enumerate(pix_3x3):   # set pixels with new colour

                            if l_pix[0] == new_pix[0]:
                                if l_pix[1] == new_pix[1]:
                                    if l_pix[2] == new_pix[2]:
                                        ext = 1
                                        if test == 1:
                                            count_a += 1
                                            print("5 ({}) Cur: {} Set: {}".format(count_a, cur_pix, new_pix))
                                            print("5 Pix list: {} \nPix_3x3: {}\n".format(pixel_list, pix_3x3))
                                        break
                                    else:
                                        n_m = 1
                                else:
                                    n_m = 1
                            else:
                                n_m = 1

                        if n_m == 1:
                            del colour_count[ind]
                            del pixel_list[ind]

                        if not colour_count:
                            if test == 1:
                                print("nope")
                            break

                    for j, l_pix in enumerate(pixels_og):   # set pixels with new colour

                        if l_pix[0] == cur_pix[0]:
                            if l_pix[1] == cur_pix[1]:
                                if l_pix[2] == cur_pix[2]:
                                    img_y, img_x = pixel_yx_og[j]
                                    image_copy[img_y, img_x] = new_pix
                                    set_a += 1

                                    msg = "Running 5x5 Search...(Pixels Changed: " + str(set_a) + ")"
                                    main.bar_update_message(msg)
                msg_count += 1


        message = "Running 7x7 Search..."
        main.bar_reset(message, 0, total_pix, 1)
                # break

        # 7x7
        set_b = 0
        count_b = 0
        msg_count = 0
        for y, row in enumerate(pixel_matrix):

            main.bar_update_progress(msg_count, 0, 1)

            for x, pix in enumerate(row):
                if test == 2:
                    print("X: ", x, "Pixel Matrix Height: ", len(pixel_matrix[0]))

                pixels_og, pixel_yx_og = get_surrounding_pixels_7x7(pixel_matrix, y, x)
                cur_pix = image_copy[y, x]

                # if cur_pix != in list:
                val = 0
                for i, pix_a in enumerate(pixels_og):
                    if cur_pix[0] == pix_a[0]:
                        if cur_pix[1] == pix_a[1]:
                            if cur_pix[2] == pix_a[2]:
                                val = 1
                                break
        #         print("7x7")
                if val == 0:
                    pixels, pixel_yx = get_surrounding_pixels_5x5(pixel_matrix, y, x)
                    pixel_yx_og += pixel_yx
                    pixels_og += pixels

                    pixels, pixel_yx = get_surrounding_pixels_3x3(pixel_matrix, y, x)
                    pixel_yx_og += pixel_yx
                    pixels_og += pixels

                    pixel_yx_og.append((y, x))
                    pixels_og.append(tuple(image_copy[y, x]))

                    pixel_list = []
                    colour_count = []
                    count_list = []
                    count_colour_list(pixels_og, pixel_list, colour_count, count_list)

                    pix_3x3 = pixels
                    ext = 0
                    while ext != 1:
                        max_colour = max(colour_count)  # get max colour
                        ind = colour_count.index(max_colour)  # get max colour index
                        new_pix = pixel_list[ind]  # get max colour value using index
                        n_m = 0
                        for j, l_pix in enumerate(pix_3x3):  # set pixels with new colour

                            if l_pix[0] == new_pix[0]:
                                if l_pix[1] == new_pix[1]:
                                    if l_pix[2] == new_pix[2]:
                                        ext = 1
                                        if test == 1:
                                            count_b += 1
                                            print("7 ({}) Cur: {} Set: {}".format(count_b, cur_pix, new_pix))
                                            print("7 Pix list: {} \nPix_3x3: {}\n".format(pixel_list, pix_3x3))
                                        break
                                    else:
                                        n_m = 1
                                else:
                                    n_m = 1
                            else:
                                n_m = 1

                        if n_m == 1:
                            del colour_count[ind]
                            del pixel_list[ind]

                        if not colour_count:
                            if test == 1:
                                print("nope")
                            break

                    for j, l_pix in enumerate(pixels_og):  # set pixels with new colour

                        if l_pix[0] == cur_pix[0]:
                            if l_pix[1] == cur_pix[1]:
                                if l_pix[2] == cur_pix[2]:
                                    img_y, img_x = pixel_yx_og[j]
                                    image_copy[img_y, img_x] = new_pix
                                    set_b += 1

                                    msg = "Running 7x7 Search...(Pixels Changed: " + str(set_a) + ")"
                                    main.bar_update_message(msg)
                msg_count += 1
                    # break

        message = "Running 9x9 Search..."
        main.bar_reset(message, 0, total_pix, 1)

        # 9x9
        set_c = 0
        count_c = 0
        msg_count = 0
        for y, row in enumerate(pixel_matrix):

            main.bar_update_progress(msg_count, 0, 1)

            for x, pix in enumerate(row):
                if test == 2:
                    print("X: ", x, "Pixel Matrix Height: ", len(pixel_matrix[0]))

                pixels_og, pixel_yx_og = get_surrounding_pixels_9x9(pixel_matrix, y, x)
                cur_pix = image_copy[y, x]

                # if cur_pix != in list:
                val = 0
                for i, pix_a in enumerate(pixels_og):
                    if cur_pix[0] == pix_a[0]:
                        if cur_pix[1] == pix_a[1]:
                            if cur_pix[2] == pix_a[2]:
                                val = 1
                                break
        #         print("9x9")
                if val == 0:
                    pixels, pixel_yx = get_surrounding_pixels_7x7(pixel_matrix, y, x)
                    pixels_og += pixels
                    pixel_yx_og += pixel_yx
                    pixels, pixel_yx = get_surrounding_pixels_5x5(pixel_matrix, y, x)
                    pixels_og += pixels
                    pixel_yx_og += pixel_yx
                    pixels, pixel_yx = get_surrounding_pixels_3x3(pixel_matrix, y, x)
                    pixels_og += pixels
                    pixel_yx_og += pixel_yx
                    pixel_yx_og.append((y, x))
                    pixels_og.append(tuple(image_copy[y, x]))

                    pixel_list = []
                    colour_count = []
                    count_list = []
                    count_colour_list(pixels_og, pixel_list, colour_count, count_list)

                    pix_3x3 = pixels
                    ext = 0
                    while ext != 1:
                        max_colour = max(colour_count)  # get max colour
                        ind = colour_count.index(max_colour)  # get max colour index
                        new_pix = pixel_list[ind]  # get max colour value using index

                        n_m = 0
                        for j, l_pix in enumerate(pix_3x3):  # set pixels with new colour

                            if l_pix[0] == new_pix[0]:
                                if l_pix[1] == new_pix[1]:
                                    if l_pix[2] == new_pix[2]:
                                        ext = 1
                                        if test == 1:
                                            count_c += 1
                                            print("9 ({}) Cur: {} Set: {}".format(count_c, cur_pix, new_pix))
                                            print("9 Pix list: {} \nPix_3x3: {}\n".format(pixel_list, pix_3x3))
                                        break

                                    else:
                                        n_m = 1
                                else:
                                    n_m = 1
                            else:
                                n_m = 1

                        if n_m == 1:
                            del colour_count[ind]
                            del pixel_list[ind]

                        if not colour_count:
                            if test == 1:
                                print("nope")
                            break

                    for j, l_pix in enumerate(pixels_og):  # set pixels with new colour

                        if l_pix[0] == cur_pix[0]:
                            if l_pix[1] == cur_pix[1]:
                                if l_pix[2] == cur_pix[2]:
                                    img_y, img_x = pixel_yx_og[j]
                                    image_copy[img_y, img_x] = new_pix
                                    set_c += 1

                                    msg = "Running 9x9 Search...(Pixels Changed: " + str(set_a) + ")"
                                    main.bar_update_message(msg)

                msg_count += 1
                    # break
        main.bar_des()

        out_img = Image.fromarray(image_copy, "RGB")
        main.undo_list.append(main.images[1])
        main.undo_function_list.append(4)
        if test == 4 or test == 1:
            print("should 5x5: {} 7x7: {} 9x9: {}\n".format(count_a, count_b, count_c))
            print("actual 5x5: {} 7x7: {} 9x9: {}\n".format(set_a, set_b, set_c))
            print("D - Functions so far: {}".format(main.undo_function_list))

        main.images[1] = out_img
        main.display_cy_image()
    else:
        if test == 1:
            print("Error: Pix_change failed")


def count_colour_list(pixels, pixel_list, colour_count, combine_count):
    test = 0
    if test == 5:
        print("count_colour_list gui.py")

    for x, pix in enumerate(pixels):

        # count the number of times a pixel appears
        if len(pixel_list) == 0:
            pixel_list.append(list(pix))
            colour_count.append(1)
            val = int(pix[0]) + int(pix[1]) + int(pix[2])
            combine_count.append(val)
        else:
            count = 0
            for i in pixel_list:

                if i[0] == pix[0]:
                    if i[1] == pix[1]:
                        if i[2] == pix[2]:
                            index = pixel_list.index(i)

                            ind = index

                            colour_count[ind] += 1
                        else:
                            count += 1
                    else:
                        count += 1
                else:
                    count += 1

                if count >= len(pixel_list):
                    pixel_list.append(list(pix))
                    colour_count.append(1)
                    val = int(pix[0]) + int(pix[1]) + int(pix[2])
                    combine_count.append(val)
                    break


def get_surrounding_pixels_3x3(pixel_matrix, y, x):
    test = 0
    if test == 5:
        print("get_surrounding_pixels_3x3 gui.py")

    row_num = len(pixel_matrix)
    col_num = len(pixel_matrix[0])
    pixels = []
    pixel_yx = []
    yn1 = y - 1
    y1 = y + 1
    xn1 = x - 1
    x1 = x + 1

    if y > 0:                                       # y - 1
        # pixels.append(pixel_matrix[yn1, x])
        pixels.append(tuple(pixel_matrix[yn1, x]))

        pixel_yx.append((yn1, x))
        if x > 0:                                   # x - 1
            # pixels.append(pixel_matrix[yn1, xn1])
            pixels.append(tuple(pixel_matrix[yn1, xn1]))
            pixel_yx.append((yn1, xn1))
        if x < col_num - 1:                         # x + 1
            # pixels.append(pixel_matrix[yn1, x1])
            pixels.append(tuple(pixel_matrix[yn1, x1]))
            pixel_yx.append((yn1, x1))
    if y < row_num - 1:                             # y + 1
        # pixels.append(pixel_matrix[y1, x])
        pixels.append(tuple(pixel_matrix[y1, x]))
        pixel_yx.append((y1, x))
        if x > 0:                                   # x - 1
            # pixels.append(pixel_matrix[y1, xn1])
            pixels.append(tuple(pixel_matrix[y1, xn1]))
            pixel_yx.append((y1, xn1))
        if x < col_num - 1:                         # x + 1
            # pixels.append(pixel_matrix[y1, x1])
            pixels.append(tuple(pixel_matrix[y1, x1]))
            pixel_yx.append((y1, x1))
    if x > 0:                                       # x - 1
        pixels.append(tuple(pixel_matrix[y, xn1]))
        pixel_yx.append((y, xn1))
    if x < col_num - 1:                             # x + 1
        pixels.append(tuple(pixel_matrix[y, x1]))
        pixel_yx.append((y, x1))
    # pixels = np.array(pixels)

    # print("pixel: {}\nPixels: {}".format(pixel_matrix[y, x], pixels))
    return pixels, pixel_yx


def get_surrounding_pixels_5x5(pixel_matrix, y, x):
    test = 0
    if test == 5:
        print("get_surrounding_pixels_5x5 gui.py")

    row_num = len(pixel_matrix)
    col_num = len(pixel_matrix[0])
    pixels = []
    pixel_yx = []
    yn2 = y - 2
    y2 = y + 2
    xn2 = x - 2
    x2 = x + 2
    yn1 = y - 1
    y1 = y + 1
    xn1 = x - 1
    x1 = x + 1

    if y > 1:                                       # y - 2
        # pixels.append(pixel_matrix[yn2, x])
        pixels.append(tuple(pixel_matrix[yn2, x]))
        pixel_yx.append((yn2, x))
        if x > 1:                                   # x - 2
            # pixels.append(pixel_matrix[yn2, xn2])
            pixels.append(tuple(pixel_matrix[yn2, xn2]))
            pixel_yx.append((yn2, xn2))
        if x < col_num - 2:                         # x + 2
            # pixels.append(pixel_matrix[yn2, x2])
            pixels.append(tuple(pixel_matrix[yn2, x2]))
            pixel_yx.append((yn2, x2))
        if x > 0:                                   # x - 1
            # pixels.append(pixel_matrix[yn2, xn1])
            pixels.append(tuple(pixel_matrix[yn2, xn1]))
            pixel_yx.append((yn2, xn1))
        if x < col_num - 1:                         # x + 1
            # pixels.append(pixel_matrix[yn2, x1])
            pixels.append(tuple(pixel_matrix[yn2, x1]))
            pixel_yx.append((yn2, x1))

    if y > 0:                                       # y - 1

        if x > 1:                                   # x - 2
            # pixels.append(pixel_matrix[yn1, xn2])
            pixels.append(tuple(pixel_matrix[yn1, xn2]))
            pixel_yx.append((yn1, xn2))
        if x < col_num - 2:                         # x + 2
            # pixels.append(pixel_matrix[yn1, x2])
            pixels.append(tuple(pixel_matrix[yn1, x2]))
            pixel_yx.append((yn1, x2))

    if y < row_num - 2:                             # y + 2
        # pixels.append(pixel_matrix[y2, x])
        pixels.append(tuple(pixel_matrix[y2, x]))
        pixel_yx.append((y2, x))
        if x > 1:                                   # x - 2
            # pixels.append(pixel_matrix[y2, xn2])
            pixels.append(tuple(pixel_matrix[y2, xn2]))
            pixel_yx.append((y2, xn2))
        if x < col_num - 2:                         # x + 2
            # pixels.append(pixel_matrix[y2, x2])
            pixels.append(tuple(pixel_matrix[y2, x2]))
            pixel_yx.append((y2, x2))
        if x > 0:                                   # x - 1
            # pixels.append(pixel_matrix[y2, xn1])
            pixels.append(tuple(pixel_matrix[y2, xn1]))
            pixel_yx.append((y2, xn1))
        if x < col_num - 1:                         # x + 1
            # pixels.append(pixel_matrix[y2, x1])
            pixels.append(tuple(pixel_matrix[y2, x1]))
            pixel_yx.append((y2, x1))

    if y < row_num - 1:                             # y + 1

        if x > 1:                                   # x - 2
            # pixels.append(pixel_matrix[y1, xn2])
            pixels.append(tuple(pixel_matrix[y1, xn2]))
            pixel_yx.append((y1, xn2))
        if x < col_num - 2:                         # x + 2
            # pixels.append(pixel_matrix[y1, x2])
            pixels.append(tuple(pixel_matrix[y1, x2]))
            pixel_yx.append((y1, x2))

    if x > 1:                                       # x - 2
        # pixels.append(pixel_matrix[y, xn2])
        pixels.append(tuple(pixel_matrix[y, xn2]))
        pixel_yx.append((y, xn2))
    if x < col_num - 2:                             # x + 2
        # pixels.append(pixel_matrix[y, x2])
        pixels.append(tuple(pixel_matrix[y, x2]))
        pixel_yx.append((y, x2))
    # pixels = np.array(pixels)
    return pixels, pixel_yx


def get_surrounding_pixels_7x7(pixel_matrix, y, x):
    test = 0
    if test == 5:
        print("get_surrounding_pixels_7x7 gui.py")

    row_num = len(pixel_matrix)
    col_num = len(pixel_matrix[0])
    pixels = []
    pixel_yx = []
    yn3 = y - 3
    y3 = y + 3
    xn3 = x - 3
    x3 = x + 3
    yn2 = y - 2
    y2 = y + 2
    xn2 = x - 2
    x2 = x + 2
    yn1 = y - 1
    y1 = y + 1
    xn1 = x - 1
    x1 = x + 1

    if y > 2:                                       # y - 3
        pixels.append(tuple(pixel_matrix[yn3, x]))
        pixel_yx.append((yn3, x))
        if x > 2:                                   # x - 3
            pixels.append(tuple(pixel_matrix[yn3, xn3]))
            pixel_yx.append((yn3, xn3))
        if x < col_num - 3:                         # x + 3
            pixels.append(tuple(pixel_matrix[yn3, x3]))
            pixel_yx.append((yn3, x3))
        if x > 1:                                   # x - 2
            pixels.append(tuple(pixel_matrix[yn3, xn2]))
            pixel_yx.append((yn3, xn2))
        if x < col_num - 2:                         # x + 2
            pixels.append(tuple(pixel_matrix[yn3, x2]))
            pixel_yx.append((yn3, x2))
        if x > 0:                                   # x - 1
            pixels.append(tuple(pixel_matrix[yn3, xn1]))
            pixel_yx.append((yn3, xn1))
        if x < col_num - 1:                         # x + 1
            pixels.append(tuple(pixel_matrix[yn3, x1]))
            pixel_yx.append((yn3, x1))

    if y > 1:                                       # y - 2

        if x > 2:                                   # x - 3
            pixels.append(tuple(pixel_matrix[yn2, xn3]))
            pixel_yx.append((yn2, xn3))
        if x < col_num - 3:                         # x + 3
            pixels.append(tuple(pixel_matrix[yn2, x3]))
            pixel_yx.append((yn2, x3))

    if y > 0:                                       # y - 1

        if x > 2:                                   # x - 3
            pixels.append(tuple(pixel_matrix[yn1, xn3]))
            pixel_yx.append((yn1, xn3))
        if x < col_num - 3:                         # x + 3
            pixels.append(tuple(pixel_matrix[yn1, x3]))
            pixel_yx.append((yn1, x3))

    if y < row_num - 3:                             # y + 3
        pixels.append(tuple(pixel_matrix[y3, x]))
        pixel_yx.append((y3, x))
        if x > 2:                                   # x - 3
            pixels.append(tuple(pixel_matrix[y3, xn3]))
            pixel_yx.append((y3, xn3))
        if x < col_num - 3:                         # x + 3
            pixels.append(tuple(pixel_matrix[y3, x3]))
            pixel_yx.append((y3, x3))
        if x > 1:                                   # x - 2
            pixels.append(tuple(pixel_matrix[y3, xn2]))
            pixel_yx.append((y3, xn2))
        if x < col_num - 2:                         # x + 2
            pixels.append(tuple(pixel_matrix[y3, x2]))
            pixel_yx.append((y3, x2))
        if x > 0:                                   # x - 1
            pixels.append(tuple(pixel_matrix[y3, xn1]))
            pixel_yx.append((y3, xn1))
        if x < col_num - 1:                         # x + 1
            pixels.append(tuple(pixel_matrix[y3, x1]))
            pixel_yx.append((y3, x1))

    if y < row_num - 2:                             # y + 2

        if x > 2:                                   # x - 3
            pixels.append(tuple(pixel_matrix[y2, xn3]))
            pixel_yx.append((y2, xn3))
        if x < col_num - 3:                         # x + 3
            pixels.append(tuple(pixel_matrix[y2, x3]))
            pixel_yx.append((y2, x3))

    if y < row_num - 1:                             # y + 1

        if x > 2:                                   # x - 3
            pixels.append(tuple(pixel_matrix[y1, xn3]))
            pixel_yx.append((y1, xn3))
        if x < col_num - 3:                         # x + 3
            pixels.append(tuple(pixel_matrix[y1, x3]))
            pixel_yx.append((y1, x3))

    if x > 2:                                       # x - 3
        pixels.append(tuple(pixel_matrix[y, xn3]))
        pixel_yx.append((y, xn3))
    if x < col_num - 3:                             # x + 3
        pixels.append(tuple(pixel_matrix[y, x3]))
        pixel_yx.append((y, x3))
    # pixels = np.array(pixels)
    return pixels, pixel_yx


def get_surrounding_pixels_9x9(pixel_matrix, y, x):
    test = 0
    if test == 5:
        print("get_surrounding_pixels_9x9 gui.py")

    row_num = len(pixel_matrix)
    col_num = len(pixel_matrix[0])
    pixels = []
    pixel_yx = []
    yn4 = y - 4
    y4 = y + 4
    xn4 = x - 4
    x4 = x + 4
    yn3 = y - 3
    y3 = y + 3
    xn3 = x - 3
    x3 = x + 3
    yn2 = y - 2
    y2 = y + 2
    xn2 = x - 2
    x2 = x + 2
    yn1 = y - 1
    y1 = y + 1
    xn1 = x - 1
    x1 = x + 1

    if y > 3:                                       # y - 4
        pixels.append(tuple(pixel_matrix[yn4, x]))
        pixel_yx.append((yn4, x))
        if x > 3:                                   # x - 4
            pixels.append(tuple(pixel_matrix[yn4, xn4]))
            pixel_yx.append((yn4, xn4))
        if x < col_num - 4:                         # x + 4
            pixels.append(tuple(pixel_matrix[yn4, x4]))
            pixel_yx.append((yn4, x4))
        if x > 2:                                   # x - 3
            pixels.append(tuple(pixel_matrix[yn4, xn3]))
            pixel_yx.append((yn4, xn3))
        if x < col_num - 3:                         # x + 3
            pixels.append(tuple(pixel_matrix[yn4, x3]))
            pixel_yx.append((yn4, x3))
        if x > 1:                                   # x - 2
            pixels.append(tuple(pixel_matrix[yn4, xn2]))
            pixel_yx.append((yn4, xn2))
        if x < col_num - 2:                         # x + 2
            pixels.append(tuple(pixel_matrix[yn4, x2]))
            pixel_yx.append((yn4, x2))
        if x > 0:                                   # x - 1
            pixels.append(tuple(pixel_matrix[yn4, xn1]))
            pixel_yx.append((yn4, xn1))
        if x < col_num - 1:                         # x + 1
            pixels.append(tuple(pixel_matrix[yn4, x1]))
            pixel_yx.append((yn4, x1))

    if y > 2:                                       # y - 3

        if x > 3:                                   # x - 4
            pixels.append(tuple(pixel_matrix[yn3, xn4]))
            pixel_yx.append((yn3, xn4))
        if x < col_num - 4:                         # x + 4
            pixels.append(tuple(pixel_matrix[yn3, x4]))
            pixel_yx.append((yn3, x4))

    if y > 1:                                       # y - 2

        if x > 3:                                   # x - 4
            pixels.append(tuple(pixel_matrix[yn2, xn4]))
            pixel_yx.append((yn2, xn4))
        if x < col_num - 4:                         # x + 4
            pixels.append(tuple(pixel_matrix[yn2, x4]))
            pixel_yx.append((yn2, x4))

    if y > 0:                                       # y - 1

        if x > 3:                                   # x - 4
            pixels.append(tuple(pixel_matrix[yn1, xn4]))
            pixel_yx.append((yn1, xn4))
        if x < col_num - 4:                         # x + 4
            pixels.append(tuple(pixel_matrix[yn1, x4]))
            pixel_yx.append((yn1, x4))

    if y < row_num - 4:                             # y + 4
        pixels.append(tuple(pixel_matrix[y4, x]))
        pixel_yx.append((y4, x))
        if x > 3:                                   # x - 4
            pixels.append(tuple(pixel_matrix[y4, xn4]))
            pixel_yx.append((y4, xn4))
        if x < col_num - 4:                         # x + 4
            pixels.append(tuple(pixel_matrix[y4, x4]))
            pixel_yx.append((y4, x4))
        if x > 2:                                   # x - 3
            pixels.append(tuple(pixel_matrix[y4, xn3]))
            pixel_yx.append((y4, xn3))
        if x < col_num - 3:                         # x + 3
            pixels.append(tuple(pixel_matrix[y4, x3]))
            pixel_yx.append((y4, x3))
        if x > 1:                                   # x - 2
            pixels.append(tuple(pixel_matrix[y4, xn2]))
            pixel_yx.append((y4, xn2))
        if x < col_num - 2:                         # x + 2
            pixels.append(tuple(pixel_matrix[y4, x2]))
            pixel_yx.append((y4, x2))
        if x > 0:                                   # x - 1
            pixels.append(tuple(pixel_matrix[y4, xn1]))
            pixel_yx.append((y4, xn1))
        if x < col_num - 1:                         # x + 1
            pixels.append(tuple(pixel_matrix[y4, x1]))
            pixel_yx.append((y4, x1))

    if y < row_num - 3:                             # y + 3

        if x > 3:                                   # x - 4
            pixels.append(tuple(pixel_matrix[y3, xn4]))
            pixel_yx.append((y3, xn4))
        if x < col_num - 4:                         # x + 4
            pixels.append(tuple(pixel_matrix[y3, x4]))
            pixel_yx.append((y3, x4))

    if y < row_num - 2:                             # y + 2

        if x > 3:                                   # x - 4
            pixels.append(tuple(pixel_matrix[y2, xn4]))
            pixel_yx.append((y2, xn4))
        if x < col_num - 4:                         # x + 4
            pixels.append(tuple(pixel_matrix[y2, x4]))
            pixel_yx.append((y2, x4))

    if y < row_num - 1:                             # y + 1

        if x > 3:                                   # x - 4
            pixels.append(tuple(pixel_matrix[y1, xn4]))
            pixel_yx.append((y1, xn4))
        if x < col_num - 4:                         # x + 4
            pixels.append(tuple(pixel_matrix[y1, x4]))
            pixel_yx.append((y1, x4))

    if x > 3:                                       # x - 4
        pixels.append(tuple(pixel_matrix[y, xn4]))
        pixel_yx.append((y, xn4))
    if x < col_num - 4:                             # x + 4
        pixels.append(tuple(pixel_matrix[y, x4]))
        pixel_yx.append((y, x4))
    # pixels = np.array(pixels)
    return pixels, pixel_yx


def get_man_merge_vals(main, change_list, pixel_list):
    test = 4
    if test == 5:
        print("get_man_merge_vals gui.py")

    image = main.images[1]
    val_list = []
    pixel_change = []
    new_pixel_list = []

    for i in change_list:
        val = i.get()
        val_list.append(val)

    if test == 1:
        print(val_list)

    for val in val_list:

        if val != 0:
            val_index = val_list.index(val)
            change_ind = val - 1
            pixel_change.append(pixel_list[change_ind])
            new_pixel_list.append(pixel_list[val_index])

    if test == 1:
        print("This test")
        print(pixel_list)
        print(new_pixel_list)
        print(pixel_change)

    image_copy = set_new_pixel_colour(image, new_pixel_list, pixel_change)
    out_img = Image.fromarray(image_copy, "RGB")
    main.undo_list.append(main.images[1])
    main.undo_function_list.append(4)
    if test == 4:
        print("M - Functions so far: {}".format(main.undo_function_list))
    main.images[1] = out_img
    main.display_cy_image()


def set_new_pixel_colour(image, new_pixel_list, pixel_change):
    test = 0
    if test == 5:
        print("set_new_pixel_colour image_processing.py")

    pixel_matrix = np.array(image)
    image_copy = pixel_matrix.copy()

    for y, row in enumerate(pixel_matrix):
        if test == 1:
            print("Y: ", y)
        for x, pixel in enumerate(row):
            if test == 1:
                print("(Y,X): ", y, ",", x)

            # count the number of times a pixel appears

            for i in new_pixel_list:

                if i[0] == pixel[0]:
                    if i[1] == pixel[1]:
                        if i[2] == pixel[2]:
                            index = new_pixel_list.index(i)

                            image_copy[y, x] = pixel_change[index]

    return image_copy


def janome_colours(main):
    test = 4
    if test == 5:
        print("janome_colours image_processing.py")

    janome_colour_list = [(0, 0, 0), (240, 240, 240), (255, 255, 23), (255, 102, 0), (47, 89, 51), (35, 115, 54),
                            (101, 194, 200), (171, 90, 150), (246, 105, 160), (255, 0, 0),
                            (156, 100, 69), (11, 47, 132), (228, 195, 93), (72, 26, 5),
                            (172, 156, 199), (253, 245, 181), (249, 153, 183), (250, 179, 129),
                            (215, 189, 164), (151, 5, 51), (160, 184, 204), (127, 194, 28),
                            (229, 229, 229), (136, 155, 155), (152, 214, 189), (178, 225, 227),
                            (152, 243, 254), (112, 169, 226), (29, 84, 120), (7, 22, 80),
                            (255, 187, 187), (255, 96, 72), (255, 90, 39), (226, 161, 136),
                            (181, 148, 116), (245, 219, 139), (255, 204, 0), (255, 189, 227),
                            (195, 0, 126), (168, 0, 67), (84, 5, 113), (255, 9, 39),
                            (198, 238, 203), (96, 133, 65), (96, 148, 24), (6, 72, 13),
                            (91, 210, 181), (76, 181, 143), (4, 145, 123), (89, 91, 97),
                            (255, 255, 220), (230, 101, 30), (230, 150, 90), (240, 156, 150),
                            (167, 108, 61), (180, 90, 48), (110, 57, 55), (92, 38, 37),
                            (98, 49, 189), (20, 50, 156), (22, 95, 167), (196, 227, 157),
                            (253, 51, 163), (238, 113, 175), (132, 49, 84), (163, 145, 102),
                            (12, 137, 24), (247, 242, 151), (204, 153, 0), (199, 151, 50),
                            (255, 157, 0), (255, 186, 94), (252, 241, 33), (255, 71, 32),
                            (0, 181, 82), (2, 87, 181), (208, 186, 176), (227, 190, 129)]

    image = main.images[1]
    pixel_matrix = np.array(image)
    image_copy = pixel_matrix.copy()
    pixel_list = []

    colour_count = []
    combine_count = []
    count_colour(pixel_matrix, pixel_list, colour_count, combine_count)
    change_pix = [0] * len(pixel_list)

    for i in pixel_list:

        diff_list = get_colour_diff(janome_colour_list, i)

        min_dif = min(diff_list)
        ind = diff_list.index(min_dif)
        pix_ind = pixel_list.index(i)

        change_pix[pix_ind] = janome_colour_list[ind]
        image_copy = set_new_pixel_colour(image, pixel_list, change_pix)

    out_img = Image.fromarray(image_copy, "RGB")
    main.undo_list.append(main.images[1])
    main.undo_function_list.append(4)
    if test == 4:
        print("J - Functions so far: {}".format(main.undo_function_list))
    main.images[1] = out_img
    main.display_cy_image()


def get_colour_diff(pixels, pixel):
    test = 0
    if test == 5:
        print("get_colour_diff image_processing.py")

    dif_val = []
    dif_list = []

    for i in pixels:
        a = 0
        dif = [0, 0, 0]
        if i[0] == pixel[0] and i[1] == pixel[1] and i[2] == pixel[2]:
            # dif = (1000, 1000, 1000)
            dif = (0, 0, 0)
        else:
            while a < 3:
                if i[a] == pixel[a]:
                    dif[a] = 0
                elif i[a] > pixel[a]:
                    p = pixel[a]
                    o_p = i[a]
                    dif[a] = o_p - p
                elif i[a] < pixel[a]:
                    p = pixel[a]
                    o_p = i[a]
                    dif[a] = p - o_p

                a += 1
        dif_list.append(dif)

    for i in dif_list:
        dif_val.append(i[0] + i[1] + i[2])

    return dif_val


def count_colour(pixel_matrix, pixel_list, colour_count, combine_count):
    test = 0
    if test == 5:
        print("count_colour image_processing.py")

    for y, row in enumerate(pixel_matrix):
        if test == 1:
            print("Y: ", y)

        for x, pix in enumerate(row):
            if test == 1:
                print("(Y,X): ", y, ",", x)

            # count the number of times a pixel appears
            if len(pixel_list) == 0:
                pixel_list.append(list(pix))
                colour_count.append(1)
                combine_count.append(int(pix[0]) + int(pix[1]) + int(pix[2]))
            else:
                count = 0
                for i in pixel_list:

                    if i[0] == pix[0]:
                        if i[1] == pix[1]:
                            if i[2] == pix[2]:
                                index = pixel_list.index(i)

                                ind = index

                                colour_count[ind] += 1
                            else:
                                count += 1
                        else:
                            count += 1
                    else:
                        count += 1

                    if count >= len(pixel_list):
                        pixel_list.append(list(pix))
                        colour_count.append(1)
                        combine_count.append(int(pix[0]) + int(pix[1]) + int(pix[2]))
                        break

    # print list of all individual colours
    if test == 1:
        e = 1
        for x in pixel_list:
            comb = combine_count[e - 1]
            num = colour_count[e - 1]
            print("Colour ", e, " Value: ", x," Comb Val:", comb, " Amount: ", num,)
            e += 1


def sort_algorithm(pixel_list, combine_value, colour_count):
    test = 0
    if test == 5:
        print("sort_algorithm gui.py")

    for i in range(len(combine_value)-1):
        min_index = i

        for j in range(i+1, len(combine_value)):

            if combine_value[j] < combine_value[min_index]:
                min_index = j

        combine_value[i], combine_value[min_index] = combine_value[min_index], combine_value[i]
        pixel_list[i], pixel_list[min_index] = pixel_list[min_index], pixel_list[i]
        colour_count[i], colour_count[min_index] = colour_count[min_index], colour_count[i]


# new - used
def create_image_plot(main):
    test = 0
    if test == 5 or test == 1:
        print("create_image_plot image_processing.py")

    main.objects.clear()    # clear existing objects
    image = main.images[1]
    pixel_matrix = np.array(image)
    image_copy = pixel_matrix.copy()

    img_height = len(pixel_matrix)
    img_width = len(pixel_matrix[0])

    # Create plot of image
    row = [0] * img_width
    plot = np.array([row] * img_height)

    pixel_list = []
    count_list = []
    combine_list = []

    # find the first 0 in plot
    count_colour(image_copy, pixel_list, count_list, combine_list)

    # set colours to numbers referencing image
    for y, row in enumerate(image_copy):
        for x, pixel in enumerate(row):

            for i in pixel_list:

                if i[0] == pixel[0]:
                    if i[1] == pixel[1]:
                        if i[2] == pixel[2]:
                            ind = pixel_list.index(i)
                            ind += 1
                            plot[y, x] = ind
    if test == 1:
        po.print_plot(plot)

    # create main_plot object from
    main_plot = po.Plot(plot)
    main_plot.set_num_list(pixel_list)

    # create ColourObjects from individual main_plot colours - progress pop added
    main_plot.create_sub_plot(main)

    if test == 1:
        main_plot.print_col_matrix_list()

    col_obj_list = main_plot.col_matrix_list
    count = 1

    msg_count = 1
    for i in col_obj_list:

        msg = "Processing Colour Plot " + str(msg_count) + "..."
        main.bar_update_message(msg)

        if test == 1:
            print("count: {}".format(count))
        col_obj = i

        col_obj.process_colour_plot(main, msg_count, main_plot.matrix)

        col_obj.create_object_sub_plot()

        text_count = 1
        for j in col_obj.ob_matrix_list:
            msg = "Colour Plot " + str(msg_count) + " - Creating Object " + str(text_count) + "..."
            main.bar_update_message(msg)
            main.bar_update_progress(1, 0, 0)

            col_sub_obj = j

            col_sub_obj.process_matrix()

            out_image = create_section_image(col_sub_obj.matrix, main.images[1])
            col_sub_obj.section_image = out_image

            main.objects.append(col_sub_obj)

            text_count += 1

        count += 1
        msg_count += 1

    count = 1
    for ob in main.objects:
        ob.ob_id = "# " + str(count)
        count += 1
    main.bar_des()

def create_section_image(ref_plot, image):
    test = 0
    if test == 5:
        print("create_section_image image_processing.py")

    ref_plot = ref_plot.copy()
    image_array = np.array(image)
    grey_image = image.convert('LA')
    n_g_image = np.array(grey_image)
    g_image = image_array.copy()
    if test == 1:
        print("REFPLOT")
        po.print_plot(ref_plot)

    for y, row in enumerate(n_g_image):
        for x, pixel in enumerate(row):

            val, null = pixel

            if test == 1:
                print("Value: {} Null: {}".format(val, null))

            if val > 200:
                val = val - 70
            elif val < 30:
                val = val + 90

            tup = (val, val, val)
            g_image[y, x] = tup
            if test == 1:
                print("pixel value: {} RBG Pixel:{}".format(pixel, g_image[y, x]))

    for y, row in enumerate(ref_plot):

        for x, point in enumerate(row):
            if test == 1:
                print(point.dtype)
            if point == 1:
                if test == 1:
                    print(" point == 1")

                points, yx_points = po.get_surrounding_points_5x5(ref_plot, y, x)

                for i, val in enumerate(points):

                    if val == 1:
                        g_image[y, x] = image_array[y, x]

    out_image = Image.fromarray(g_image, "RGB")
    if test == 1:
        po.print_plot(g_image)
        po.print_plot(image_array)

    return out_image

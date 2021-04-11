
# new
def image_object1():
    image = images[1]
    pixel_matrix = np.array(image)
    image_copy = pixel_matrix.copy()
    col_num_list = []
    col_val_list = []
    row = [0]*len(pixel_matrix[0])
    plot = np.array([row]*len(pixel_matrix))
    ind_list = []
    plot_check_val = True
    c_x = 0
    c_y = 0
    x = 0
    y = 0
    last_pix = 8
    count = 1
    c_colour = image_copy[y, x]
    i = 0
    a = 0
    while plot_check_val:

        # One
        if last_pix == 8:

            if y - 1 >= 0 and x - 1 >= 0:

                new_pix = image_copy[y - 1, x - 1]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:

                            pix_a = image_copy[y, x-1]
                            pix_b = image_copy[y-1, x]

                            if pix_a[0] == c_colour[0]:
                                if pix_a[1] == c_colour[1]:
                                    if pix_a[2] == c_colour[2]:
                                        comp_a = True
                                    else:
                                        comp_a = False
                                else:
                                    comp_a = False
                            else:
                                comp_a = False

                            if pix_b[0] == c_colour[0]:
                                if pix_b[1] == c_colour[1]:
                                    if pix_b[2] == c_colour[2]:
                                        comp_b = True
                                    else:
                                        comp_b = False
                                else:
                                    comp_b = False
                            else:
                                comp_b = False

                            if comp_a or comp_b:
                                y = y - 1
                                x = x - 1
                                plot[y, x] = count
                                a = check_index_list(ind_list, y, x)

                                if a == 0:
                                    ind_list.append((y, x))
                                    last_pix = 5
                                else:
                                    break

            if last_pix != 5:
                last_pix = 1

        # Two
        elif last_pix == 1:

            if y - 1 >= 0:

                new_pix = image_copy[y - 1, x]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:
                            y = y - 1
                            plot[y, x] = count

                            a = check_index_list(ind_list, y, x)

                            if a == 0:
                                ind_list.append((y, x))
                                last_pix = 6
                            else:
                                break

            if last_pix != 6:
                last_pix = 2

        # Three
        elif last_pix == 2:

            if y - 1 >= 0 and x + 1 < len(image_copy[0]):

                new_pix = image_copy[y - 1, x + 1]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:

                            pix_a = image_copy[y, x + 1]
                            pix_b = image_copy[y - 1, x]

                            if pix_a[0] == c_colour[0]:
                                if pix_a[1] == c_colour[1]:
                                    if pix_a[2] == c_colour[2]:
                                        comp_a = True
                                    else:
                                        comp_a = False
                                else:
                                    comp_a = False
                            else:
                                comp_a = False

                            if pix_b[0] == c_colour[0]:
                                if pix_b[1] == c_colour[1]:
                                    if pix_b[2] == c_colour[2]:
                                        comp_b = True
                                    else:
                                        comp_b = False
                                else:
                                    comp_b = False
                            else:
                                comp_b = False

                            if comp_a or comp_b:
                                y = y - 1
                                x = x + 1
                                plot[y, x] = count
                                a = check_index_list(ind_list, y, x)

                                if a == 0:
                                    ind_list.append((y, x))
                                    last_pix = 7
                                else:
                                    break

            if last_pix != 7:
                last_pix = 3

        # Four
        elif last_pix == 3:

            if x + 1 < len(image_copy[0]):

                new_pix = image_copy[y, x + 1]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:

                            x = x + 1
                            plot[y, x] = count
                            a = check_index_list(ind_list, y, x)

                            if a == 0:
                                ind_list.append((y, x))
                                last_pix = 8
                            else:
                                break

            if last_pix != 8:
                last_pix = 4

        # Five
        elif last_pix == 4:

            if y + 1 < len(image_copy) and x + 1 < len(image_copy[0]):

                new_pix = image_copy[y + 1, x + 1]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:

                            pix_a = image_copy[y, x + 1]
                            pix_b = image_copy[y + 1, x]

                            if pix_a[0] == c_colour[0]:
                                if pix_a[1] == c_colour[1]:
                                    if pix_a[2] == c_colour[2]:
                                        comp_a = True
                                    else:
                                        comp_a = False
                                else:
                                    comp_a = False
                            else:
                                comp_a = False

                            if pix_b[0] == c_colour[0]:
                                if pix_b[1] == c_colour[1]:
                                    if pix_b[2] == c_colour[2]:
                                        comp_b = True
                                    else:
                                        comp_b = False
                                else:
                                    comp_b = False
                            else:
                                comp_b = False

                            if comp_a or comp_b:
                                y = y + 1
                                x = x + 1
                                plot[y, x] = count
                                a = check_index_list(ind_list, y, x)

                                if a == 0:
                                    ind_list.append((y, x))
                                    last_pix = 1
                                else:
                                    break

            if last_pix != 1:
                last_pix = 5

        # Six
        elif last_pix == 5:

            if y + 1 < len(image_copy):

                new_pix = image_copy[y + 1, x]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:
                            y = y + 1

                            plot[y, x] = count
                            a = check_index_list(ind_list, y, x)

                            if a == 0:
                                ind_list.append((y, x))
                                last_pix = 2
                            else:
                                break

            if last_pix != 2:
                last_pix = 6

        # Seven
        elif last_pix == 6:

            if y + 1 < len(image_copy) and x - 1 >= 0:

                new_pix = image_copy[y + 1, x - 1]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:

                            pix_a = image_copy[y, x - 1]
                            pix_b = image_copy[y + 1, x]

                            if pix_a[0] == c_colour[0]:
                                if pix_a[1] == c_colour[1]:
                                    if pix_a[2] == c_colour[2]:
                                        comp_a = True
                                    else:
                                        comp_a = False
                                else:
                                    comp_a = False
                            else:
                                comp_a = False

                            if pix_b[0] == c_colour[0]:
                                if pix_b[1] == c_colour[1]:
                                    if pix_b[2] == c_colour[2]:
                                        comp_b = True
                                    else:
                                        comp_b = False
                                else:
                                    comp_b = False
                            else:
                                comp_b = False

                            if comp_a or comp_b:
                                y = y + 1
                                x = x - 1
                                plot[y, x] = count
                                a = check_index_list(ind_list, y, x)

                                if a == 0:
                                    ind_list.append((y, x))
                                    last_pix = 3
                                else:
                                    break

            if last_pix != 3:
                last_pix = 7

        # Eight
        elif last_pix == 7:

            if x - 1 >= 0:

                new_pix = image_copy[y, x - 1]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:

                            x = x - 1
                            plot[y, x] = count
                            a = check_index_list(ind_list, y, x)

                            if a == 0:
                                ind_list.append((y, x))
                                last_pix = 4
                            else:
                                break

            if last_pix != 4:
                last_pix = 8

        # a = check_index_list(ind_list, y, x)
        i += 1

    # start_val = 0
    # for y in plot:
    #     for x in y:
    #
    #         co = x
    #
    #         if co == start_val:
    #             for i in col_val_list:
    #
    #         if co == 0 and start_val != 0:
    #             col_val_list.append((y, x))
    #
    #         elif co != 0:
    #             start_val = co
    #
    #         else:
    #             print("x-1")

    print_plot(plot)
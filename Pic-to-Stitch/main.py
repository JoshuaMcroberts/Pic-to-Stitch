import gui_copy as gui

def print_hi(name):

    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')

    app = gui.GuiWindow
    app.gui_window("tim")

def find_outline(image_copy, plot, s_object, start_pix, start_point):

    ind_list = []

    y, x = start_point

    last_pix = start_pix
    count = 1
    # count = s_object.object_id
    c_colour = s_object.colour
    i = 0
    ind_list.append((y, x))
    plot[y, x] = count
    s_object.plot[y, x] = count
    # x += 1
    print("Colour: ", c_colour)

    for j in range(len(image_copy)*len(image_copy[0])):

        # One
        if last_pix == 8:
            print("#One")
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
                                # if not ind_list:
                                #     y = y - 1
                                #     x = x - 1
                                #     plot[y, x] = count
                                #     s_object.plot[y, x] = count
                                #     ind_list.append((y, x))
                                #
                                #     last_pix = 5
                                #
                                # el
                                if (y, x) == ind_list[0]:
                                    break

                                else:
                                    y = y - 1
                                    x = x - 1
                                    plot[y, x] = count
                                    s_object.plot[y, x] = count
                                    ind_list.append((y, x))
                                    print("Set")
                                    last_pix = 5

            if last_pix != 5:
                last_pix = 1

        # Two
        elif last_pix == 1:
            print("#Two")
            if y - 1 >= 0:

                new_pix = image_copy[y - 1, x]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:

                            # if not ind_list:
                            #     y = y - 1
                            #     plot[y, x] = count
                            #     s_object.plot[y, x] = count
                            #     ind_list.append((y, x))
                            #
                            #     last_pix = 6
                            #
                            # el
                            if (y, x) == ind_list[0]:
                                break

                            else:
                                y = y - 1
                                plot[y, x] = count
                                s_object.plot[y, x] = count
                                ind_list.append((y, x))
                                print("Set")
                                last_pix = 6

            if last_pix != 6:
                last_pix = 2

        # Three
        elif last_pix == 2:
            print("#Three")
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

                                # if not ind_list:
                                #     y = y - 1
                                #     x = x + 1
                                #     plot[y, x] = count
                                #     s_object.plot[y, x] = count
                                #
                                #     ind_list.append((y, x))
                                #     last_pix = 7
                                #
                                # el
                                if (y, x) == ind_list[0]:
                                    break

                                else:
                                    y = y - 1
                                    x = x + 1
                                    plot[y, x] = count
                                    s_object.plot[y, x] = count
                                    ind_list.append((y, x))
                                    print("Set")
                                    last_pix = 7

            if last_pix != 7:
                last_pix = 3

        # Four
        elif last_pix == 3:
            print("#Four")
            if x + 1 < len(image_copy[0]):

                new_pix = image_copy[y, x + 1]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:

                            # if not ind_list:
                            #     x = x + 1
                            #     plot[y, x] = count
                            #     s_object.plot[y, x] = count
                            #     ind_list.append((y, x))
                            #
                            #     last_pix = 8
                            #
                            # el
                            if (y, x) == ind_list[0]:
                                break

                            else:
                                x = x + 1
                                plot[y, x] = count
                                s_object.plot[y, x] = count
                                ind_list.append((y, x))
                                print("Set")
                                last_pix = 8

            if last_pix != 8:
                last_pix = 4

        # Five
        elif last_pix == 4:
            print("#Five")
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

                                # if not ind_list:
                                #     y = y + 1
                                #     x = x + 1
                                #     plot[y, x] = count
                                #     s_object.plot[y, x] = count
                                #     ind_list.append((y, x))
                                #
                                #     last_pix = 1
                                #
                                # el
                                if (y, x) == ind_list[0]:
                                    break

                                else:
                                    y = y + 1
                                    x = x + 1
                                    plot[y, x] = count
                                    s_object.plot[y, x] = count
                                    ind_list.append((y, x))
                                    print("Set")
                                    last_pix = 1

            if last_pix != 1:
                last_pix = 5

        # Six
        elif last_pix == 5:
            print("#Six")
            if y + 1 < len(image_copy):

                new_pix = image_copy[y + 1, x]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:

                            # if not ind_list:
                            #     y = y + 1
                            #     plot[y, x] = count
                            #     s_object.plot[y, x] = count
                            #     ind_list.append((y, x))
                            #
                            #     last_pix = 2
                            #
                            # el
                            if (y, x) == ind_list[0]:
                                break

                            else:
                                y = y + 1
                                plot[y, x] = count
                                s_object.plot[y, x] = count
                                ind_list.append((y, x))
                                print("Set")
                                last_pix = 2

            if last_pix != 2:
                last_pix = 6

        # Seven
        elif last_pix == 6:
            print("#Seven")
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

                                # if not ind_list:
                                #     y = y + 1
                                #     x = x - 1
                                #     plot[y, x] = count
                                #     s_object.plot[y, x] = count
                                #     ind_list.append((y, x))
                                #
                                #     last_pix = 3
                                #
                                # el
                                if (y, x) == ind_list[0]:
                                    break

                                else:
                                    y = y + 1
                                    x = x - 1
                                    plot[y, x] = count
                                    s_object.plot[y, x] = count
                                    ind_list.append((y, x))
                                    print("Set")
                                    last_pix = 3

            if last_pix != 3:
                last_pix = 7

        # Eight
        elif last_pix == 7:
            print("#Eight")
            if x - 1 >= 0:

                new_pix = image_copy[y, x - 1]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:

                            # if not ind_list:
                            #     x = x - 1
                            #     plot[y, x] = count
                            #     s_object.plot[y, x] = count
                            #     ind_list.append((y, x))
                            #
                            #     last_pix = 4
                            #
                            # el
                            if (y, x) == ind_list[0]:
                                break

                            else:
                                x = x - 1
                                plot[y, x] = count
                                s_object.plot[y, x] = count
                                ind_list.append((y, x))
                                print("Set")
                                last_pix = 4

            if last_pix != 4:
                last_pix = 8

        # a = check_index_list(ind_list, y, x)
        i += 1

    max_y = 0
    min_y = 0
    max_x = 0
    min_x = 0

    for k in ind_list:
        y, x = k
        if max_y < y:
            max_y = y
        if max_x < x:
            max_x = x
        if min_y > y:
            min_y = y
        if min_x > x:
            min_x = x

    s_object.max_yx = (max_y, max_x)
    s_object.min_yx = (min_y, min_x)
    s_object.object_outline = ind_list

    print_plot(plot)
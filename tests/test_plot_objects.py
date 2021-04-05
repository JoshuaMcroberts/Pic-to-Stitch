import unittest
from unittest import mock
import numpy as np
import sys
sys.path.append('../pic_to_stitch/')

from pic_to_stitch import plot_objects as po


class TestPlotObjects(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        self.plot_ob = po.Plot()
        row = [0] * 10
        matrix = np.array([row] * 10)
        self.plot_ob.matrix = matrix
        self.plot_ob.col_list = [(180, 154, 67), (120, 254, 0), (20, 90, 0), (243, 45, 123)]
        self.plot_ob.col_amount = 4
        self.plot_ob.matrix_width = 10
        self.plot_ob.matrix_height = 10
        self.plot_ob.col_matrix_list = [1, 2, 3, 4, 5]

    def tearDown(self):
        pass


    def get_object_outline(main_plot, ref_plot, start_yx, start_point, set_to, col_num):
        test = 0

        # console testing comment
        if test == 5:
            print("get_object_outline - plot_objects.py")

        plot = main_plot
        y, x = start_yx
        l_point = start_point
        ind_list = []
        plot_h = len(ref_plot)
        plot_w = len(ref_plot[0])

        if test == 2:
            print("COL_NUM: {}".format(col_num))

        bol = isinstance(ref_plot[0, 0], str)

        if bol:
            set_to = str(set_to)

        ref_plot[y, x] = set_to
        ind_list.append((y, x))

        count = 0
        ext = 0
        while ext != 1:

            # One
            if l_point == 8:
                if test == 1:
                    print("# One")

                if y - 1 >= 0 and x - 1 >= 0:
                    n_point = plot[y - 1, x - 1]

                    if n_point == col_num:
                        pon_a = plot[y, x - 1]
                        pon_b = plot[y - 1, x]

                        if pon_a == pon_b:
                            if test == 2:
                                print("1 can't go equal points pon_a: {} pon_b: {}".format(pon_a, pon_b))
                            points, yx_points = get_surrounding_points_5x5(plot, y - 1, x - 1)
                            val_list, amount_list = count_list(points)
                            anw = t_w_p_logic(col_num, pon_a, val_list, amount_list)

                            if anw == 1:
                                y -= 1
                                x -= 1
                                if test == 1 or test == 2:  # testing console comments
                                    print("Che 1 Set ({},{})".format(y, x))
                                ref_plot[y, x] = set_to
                                ind_list.append((y, x))
                                l_point = 5

                            elif anw == 2:
                                pass
                            elif anw == 3:
                                pass

                        else:
                            if (y - 1, x - 1) == ind_list[0]:
                                break
                            else:
                                y -= 1
                                x -= 1
                                if test == 1 or test == 2:  # testing console comments
                                    print("Pos 1 Set ({},{})".format(y, x))
                                ref_plot[y, x] = set_to
                                ind_list.append((y, x))
                                l_point = 5

                if l_point != 5:
                    l_point = 1

            # Two
            elif l_point == 1:
                if test == 1:
                    print("# Two")

                if y - 1 >= 0:
                    n_point = plot[y - 1, x]

                    if n_point == col_num:

                        if (y - 1, x) == ind_list[0]:
                            break
                        else:
                            y -= 1
                            if test == 1 or test == 2:  # testing console comments
                                print("Pos 2 Set ({},{})".format(y, x))
                            ref_plot[y, x] = set_to
                            ind_list.append((y, x))
                            l_point = 6

                if l_point != 6:
                    l_point = 2

            # Three
            elif l_point == 2:
                if test == 1:
                    print("# Three")

                if y - 1 >= 0 and x + 1 < len(plot[0]):
                    n_point = plot[y - 1, x + 1]

                    if n_point == col_num:
                        pon_a = plot[y, x + 1]
                        pon_b = plot[y - 1, x]

                        if pon_a == pon_b:

                            if test == 1 or test == 2:
                                print("3 can't go")

                            points, yx_points = get_surrounding_points_5x5(plot, y - 1, x + 1)
                            val_list, amount_list = count_list(points)
                            anw = t_w_p_logic(col_num, pon_a, val_list, amount_list)

                            if anw == 1:
                                y -= 1
                                x += 1

                                if test == 1 or test == 2:  # testing console comments
                                    print("Che 3 Set ({},{})".format(y, x))

                                ref_plot[y, x] = set_to
                                ind_list.append((y, x))
                                l_point = 7

                            elif anw == 2:
                                pass
                            elif anw == 3:
                                pass

                        else:
                            if (y - 1, x + 1) == ind_list[0]:
                                break
                            else:
                                y -= 1
                                x += 1

                                if test == 1 or test == 2:  # testing console comments
                                    print("Pos 3 Set ({},{})".format(y, x))

                                ref_plot[y, x] = set_to
                                ind_list.append((y, x))
                                l_point = 7

                if l_point != 7:
                    l_point = 3

            # Four
            elif l_point == 3:
                if test == 1:
                    print("# Four")

                if x + 1 < len(plot[0]):
                    n_point = plot[y, x + 1]

                    if n_point == col_num:

                        if (y, x + 1) == ind_list[0]:
                            break
                        else:

                            x += 1
                            if test == 1 or test == 2:  # testing console comments
                                print("Pos 4 Set ({},{})".format(y, x))
                            ref_plot[y, x] = set_to
                            ind_list.append((y, x))
                            l_point = 8

                if l_point != 8:
                    l_point = 4

            # Five
            elif l_point == 4:
                if test == 1:
                    print("# Five")

                if y + 1 < len(plot) and x + 1 < len(plot[0]):

                    n_point = plot[y + 1, x + 1]

                    if n_point == col_num:
                        pon_a = plot[y, x + 1]
                        pon_b = plot[y + 1, x]

                        if pon_a == pon_b:

                            if test == 1 or test == 2:
                                print("5 can't go equal points pon_a: {} pon_b: {}".format(pon_a, pon_b))

                            points, yx_points = get_surrounding_points_5x5(plot, y + 1, x + 1)
                            val_list, amount_list = count_list(points)
                            anw = t_w_p_logic(col_num, pon_a, val_list, amount_list)

                            if anw == 1:
                                y += 1
                                x += 1

                                if test == 1 or test == 2:  # testing console comments
                                    print("Che 5 Set ({},{})".format(y, x))

                                ref_plot[y, x] = set_to
                                ind_list.append((y, x))
                                l_point = 1

                            elif anw == 2:
                                pass
                            elif anw == 3:
                                pass

                        else:
                            if (y + 1, x + 1) == ind_list[0]:
                                break
                            else:
                                y += 1
                                x += 1
                                if test == 1 or test == 2:  # testing console comments
                                    print("Pos 5 Set ({},{})".format(y, x))
                                ref_plot[y, x] = set_to
                                ind_list.append((y, x))
                                l_point = 1

                if l_point != 1:
                    l_point = 5

            # Six
            elif l_point == 5:
                if test == 1:
                    print("# Six")

                if y + 1 < len(plot):
                    n_point = plot[y + 1, x]

                    if n_point == col_num:

                        if (y + 1, x) == ind_list[0]:
                            break
                        else:
                            y += 1
                            if test == 1 or test == 2:  # testing console comments
                                print("Pos 6 Set ({},{})".format(y, x))
                            ref_plot[y, x] = set_to
                            ind_list.append((y, x))
                            l_point = 2

                if l_point != 2:
                    l_point = 6

            # Seven
            elif l_point == 6:
                if test == 1:
                    print("# Seven")

                if y + 1 < len(plot) and x - 1 >= 0:
                    n_point = plot[y + 1, x - 1]

                    if n_point == col_num:
                        pon_a = plot[y, x - 1]
                        pon_b = plot[y + 1, x]

                        if pon_a == pon_b:

                            if test == 1 or test == 2:
                                print("7 can't go")

                            points, yx_points = get_surrounding_points_5x5(plot, y + 1, x - 1)
                            val_list, amount_list = count_list(points)
                            anw = t_w_p_logic(col_num, pon_a, val_list, amount_list)

                            if anw == 1:
                                y += 1
                                x -= 1

                                if test == 1 or test == 2:  # testing console comments
                                    print("Che 7 Set ({},{})".format(y, x))

                                ref_plot[y, x] = set_to
                                ind_list.append((y, x))
                                l_point = 3

                            elif anw == 2:
                                pass
                            elif anw == 3:
                                pass
                        else:
                            if (y + 1, x - 1) == ind_list[0]:
                                break
                            else:
                                y += 1
                                x -= 1
                                if test == 1 or test == 2:  # testing console comments
                                    print("Pos 7 Set ({},{})".format(y, x))
                                ref_plot[y, x] = set_to
                                ind_list.append((y, x))
                                l_point = 3

                if l_point != 3:
                    l_point = 7

            # Eight
            elif l_point == 7:
                if test == 1:
                    print("# Eight")

                if x - 1 >= 0:
                    n_point = plot[y, x - 1]

                    if n_point == col_num:

                        if (y, x - 1) == ind_list[0]:
                            break
                        else:

                            x -= 1
                            if test == 1 or test == 2:  # testing console comments
                                print("Pos 8 Set ({},{})".format(y, x))
                            ref_plot[y, x] = set_to
                            ind_list.append((y, x))
                            l_point = 4

                if l_point != 4:
                    l_point = 8

            if count > len(main_plot)*len(main_plot[0])*10:
                ext = 1
            count += 1

        max_y = 0
        min_y = plot_h
        max_x = 0
        min_x = plot_w

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

        if test == "mxy":
            print("{} < y > {} {} < x > {}".format(min_y, max_y, min_x, max_x))
            print(ind_list)

        max_yx = (max_y, max_x)
        min_yx = (min_y, min_x)

        return max_yx, min_yx, ind_list


    def get_object_outline_fill(main, main_plot, ref_plot, start_yx, start_point, set_to, col_num, ind_list):
        test = 0
        if test == 5:
            print("get_object_outline_fill - plot_objects.py")
        msg_count = 0

        # progress bar update
        if main is not None:
            msg = "Getting Running Fill...(Points Set: " + str(msg_count) + ")"
            main.bar_update_message(msg)
        # end

        ref_plot = ref_plot.copy()
        plot = main_plot.copy()
        y, x = start_yx
        l_point = start_point
        ind_list = ind_list

        if test == 1:
            print(ind_list)

        ext = 0
        loop = 0
        if test == 2:
            print("COL_NUM: {}".format(col_num))

        bol = isinstance(ref_plot[0, 0], str)

        if bol:
            set_to = str(set_to)

        if ref_plot[y, x] == 1:
            ref_plot[y, x] = set_to  # setting start point
            ind_list.append((y, x))  # setting start point in list

            if test == 1:
                print("First Set ({},{})".format(y, x))

        if test == 1:
            print("plot")
            print_plot(plot)
            print("ref")
            print_plot(ref_plot)

        while ext != 1:

            # One
            if l_point == 8:    # check loop start
                if test == 1:   # testing console comments
                    print("# One")

                if y - 1 >= 0 and x - 1 >= 0:   # check if this point is within the plot limits
                    n_point = ref_plot[y - 1, x - 1]    # set this point

                    if n_point == col_num:       # check against colour_number

                        y -= 1  # set y to y - 1
                        x -= 1  # set x to x - 1

                        if test == 1 or test == 2:  # testing console comments
                            print("Pos 1 Set ({},{})".format(y, x))

                        ref_plot[y, x] = set_to     # set point
                        ind_list.append((y, x))     # add point to list
                        loop = 0        # reset loop check value
                        l_point = 5     # set loop start for next point

                        msg_count += 1

                if l_point != 5:    # check if loop start was set
                    l_point = 1     # if not, set to the next position

            # Two
            elif l_point == 1:  # check loop start
                if test == 1:   # testing console comments
                    print("# Two")

                if y - 1 >= 0:  # check if this point is within the plot limits
                    n_point = ref_plot[y - 1, x]    # set this point

                    if n_point == col_num:  # check against colour_number

                        y -= 1  # set y to y - 1

                        if test == 1 or test == 2:   # testing console comments
                            print("Pos 2 Set ({},{})".format(y, x))

                        ref_plot[y, x] = set_to     # set point
                        ind_list.append((y, x))     # add point to list
                        loop = 0        # reset loop check value
                        l_point = 6     # set loop start for next point

                        msg_count += 1

                if l_point != 6:    # check if loop start was set
                    l_point = 2     # if not, set to the next position

            # Three
            elif l_point == 2:  # check if this point is within the plot limits
                if test == 1:   # set this point
                    print("# Three")

                if y - 1 >= 0 and x + 1 < len(plot[0]):     # check if this point is within the plot limits
                    n_point = ref_plot[y - 1, x + 1]    # set this point

                    if n_point == col_num:      # check against colour_number

                        y -= 1  # set y to y - 1
                        x += 1  # set x to x + 1

                        if test == 1 or test == 2:   # testing console comments
                            print("Pos 3 Set ({},{})".format(y, x))

                        ref_plot[y, x] = set_to     # set point
                        ind_list.append((y, x))     # add point to list
                        loop = 0        # reset loop check value
                        l_point = 7     # set loop start for next point

                        msg_count += 1

                if l_point != 7:    # check if loop start was set
                    l_point = 3     # if not, set to the next position

            # Four
            elif l_point == 3:  # check loop start
                if test == 1:   # testing console comments
                    print("# Four")

                if x + 1 < len(plot[0]):        # check if this point is within the plot limits
                    n_point = ref_plot[y, x + 1]    # set this point

                    if n_point == col_num:  # check against colour_number

                        x += 1  # set x to x + 1

                        if test == 1 or test == 2:   # testing console comments
                            print("Pos 4 Set ({},{})".format(y, x))

                        ref_plot[y, x] = set_to     # set point
                        ind_list.append((y, x))     # add point to list
                        loop = 0        # reset loop check value
                        l_point = 8     # set loop start for next point

                        msg_count += 1

                if l_point != 8:    # check if loop start was set
                    l_point = 4     # if not, set to the next position

            # Five
            elif l_point == 4:  # check loop start
                if test == 1:   # testing console comments
                    print("# Five")

                if y + 1 < len(plot) and x + 1 < len(plot[0]):  # check if this point is within the plot limits
                    n_point = ref_plot[y + 1, x + 1]    # set this point

                    if n_point == col_num:      # check against colour_number

                        y += 1  # set y to y + 1
                        x += 1  # set x to x + 1

                        if test == 1 or test == 2:   # testing console comments
                            print("Pos 5 Set ({},{})".format(y, x))

                        ref_plot[y, x] = set_to     # set point
                        ind_list.append((y, x))     # add point to list
                        loop = 0        # reset loop check value
                        l_point = 1     # set loop start for next point

                        msg_count +=1

                if l_point != 1:    # check if loop start was set
                    l_point = 5     # if not, set to the next position

            # Six
            elif l_point == 5:  # check loop start
                if test == 1:   # testing console comments
                    print("# Six")

                if y + 1 < len(plot):    # check if this point is within the plot limits
                    n_point = ref_plot[y + 1, x]    # set this point

                    if n_point == col_num:  # check against colour_number

                        y += 1  # set y to y + 1

                        if test == 1 or test == 2:   # testing console comments
                            print("Pos 6 Set ({},{})".format(y, x))

                        ref_plot[y, x] = set_to     # set point
                        ind_list.append((y, x))     # add point to list
                        loop = 0        # reset loop check value
                        l_point = 2     # set loop start for next point

                        msg_count += 1

                if l_point != 2:    # check if loop start was set
                    l_point = 6     # if not, set to the next position

            # Seven
            elif l_point == 6:  # check loop start
                if test == 1:   # testing console comments
                    print("# Seven")

                if y + 1 < len(plot) and x - 1 >= 0:    # check if this point is within the plot limits
                    n_point = ref_plot[y + 1, x - 1]     # set this point

                    if n_point == col_num:      # check against colour_number

                        y += 1  # set y to y + 1
                        x -= 1  # set x to x - 1

                        if test == 1 or test == 2:   # testing console comments
                            print("POS 7 Set ({},{})".format(y, x))

                        ref_plot[y, x] = set_to     # set point
                        ind_list.append((y, x))     # add point to list
                        loop = 0        # reset loop check value
                        l_point = 3     # set loop start for next point

                        msg_count += 1

                if l_point != 3:    # check if loop start was set
                    l_point = 7     # if not, set to the next position

            # Eight
            elif l_point == 7:  # check loop start
                if test == 1:   # testing console comments
                    print("# Eight")

                if x - 1 >= 0:  # check if this point is within the plot limits
                    n_point = ref_plot[y, x - 1]    # set this point

                    if n_point == col_num:  # check against colour_number

                        x -= 1  # set x to x - 1

                        if test == 1 or test == 2:   # testing console comments
                            print("Pos 8 Set ({},{})".format(y, x))

                        ref_plot[y, x] = set_to     # set point
                        ind_list.append((y, x))     # add point to list
                        loop = 0        # reset loop check value
                        l_point = 4     # set loop start for next point

                        msg_count += 1

                if l_point != 4:    # check if loop start was set
                    l_point = 8     # if not, set to the next position

            # progress bar update
            if main is not None:
                if msg_count % 10 == 0:
                    msg = "Getting Object Outline...(Points Set: " + str(msg_count) + ")"
                    main.bar_update_message(msg)
                    main.bar_update_progress(0, 0.001, 1)
            # end

            if loop > 16:

                if test == 1 or test == 2:
                    print("trapped")

                bol, yx = check_for_number(ref_plot, 1)

                if bol:
                    yx, ind_list = asp.move_to_a_star(main, plot, yx, ind_list[-1], ind_list)
                    y, x = yx
                    if test == 1:
                        print("OF Move_to Set ({},{})".format(y, x))
                    ref_plot[y, x] = set_to
                    loop = 0
                else:
                    if test == 1:
                        print("Exit")
                    ext = 1

            loop += 1   # counts the number of loops without a point being set

        if test == 1:
            print_plot(ref_plot)

        return ind_list


    def get_object_fill_stitch(main, template, plot, start_yx, max_yx, min_yx, ind_list):
        test = 0
        if test == 5:
            print("get_object_fill_stitch - plot_objects.py")

        msg_count = 0

        # progress bar update
        if main is not None:

            msg = "Getting Fill Base...(Points Set: " + str(msg_count) + ")"
            main.bar_update_message(msg)
        # end

        s_y, s_x = start_yx
        y = s_y
        x = s_x
        direct = 1
        ext = 0
        plot_c = plot.copy()
        max_y, max_x = max_yx
        min_y, min_x = min_yx

        if test == 1 or test == 2:
            print(ind_list)
            print("Fill Part 1")

        while ext != 1:     # vertical spaced stitches

            template[y, x] = "1"

            # Down
            if direct == 1:

                if test == 1:
                    print("# Down")

                a = y + 1

                if y + 1 < len(plot_c) and plot_c[a, x] == 1:     # if down is a valid move
                    y = a                   # set new y
                    template[y, x] = "1"    # set current point in template
                    ind_list.append((y, x))     # add co-or to list
                    if test == 2:
                        print("D Set: ({},{})". format(y, x))

                    msg_count += 1

                else:                       # if not set direction var to 2
                    direct = 2

            # Right 1
            elif direct == 2:
                if test == 1:
                    print("# Right 1")

                a = y + 1
                b = x + 1
                c = y - 1

                if test == 1:
                    print(max_x, " ", b)

                if b > max_x:
                    new_plot = compare_plots(plot_c, 1, template, "2")
                    if test == 2:
                        print_plot(new_plot)
                    anw, yx = check_for_number(new_plot, "1")

                    if anw:
                        yx, ind_list = asp.move_to_a_star(main, plot_c, yx, ind_list[-1], ind_list)  # run move_to
                        y, x = yx
                        direct = 1

                    else:
                        ext = 1  # if false, all areas have been visited, exit while loop

                # if position 5
                elif y + 1 < len(plot_c) and plot_c[a, b] == 1:

                    if test == 1:
                        print("Pos 5")

                    if template[a, b] == "1":  # hit already completed section
                        new_plot = compare_plots(plot_c, 1, template, "2")
                        if test == 2:
                            print_plot(new_plot)
                        anw, yx = check_for_number(new_plot, "1")  # check if any uncompleted parts left

                        if anw:  # if true
                            yx, ind_list = asp.move_to_a_star(main, plot_c, yx, ind_list[-1], ind_list)  # run move_to
                            y, x = yx
                            direct = 1
                        else:
                            ext = 1  # if false, all areas have been visited, exit while loop

                    else:

                        y = a
                        x = b
                        ind_list.append((y, x))

                        msg_count += 1

                        if test == 2:
                            print("Pos 5 Set: ({},{})".format(y, x))

                        j = 0
                        while j != 1:   # to the end of the line

                            if x + 1 < len(template[0]) and template[y, x + 1] == "1":
                                break
                            elif y + 1 < len(plot_c) and plot_c[y + 1, x] != 0:
                                y = y + 1
                                ind_list.append((y, x))
                                if test == 2:
                                    print("Por 5 Set: ({},{})".format(y, x))

                                msg_count += 1

                            else:
                                j = 1

                            if y + 1 >= len(plot_c):
                                direct = 3
                            elif plot_c[y + 1, x] == 0 and template[y + 1, x] == "2":
                                direct = 3

                        # look at the nest 2's column

                # if position 4
                elif plot_c[y, b] == 1:

                    if test == 1:
                        print("Pos 4")

                    if template[y, b] == "1":  # hit already completed section
                        new_plot = compare_plots(plot_c, 1, template, "2")
                        if test == 2:
                            print_plot(new_plot)
                        anw, yx = check_for_number(new_plot, "1")  # check if any uncompleted parts left

                        if anw:  # if true
                            yx, ind_list = asp.move_to_a_star(main, plot_c, yx, ind_list[-1], ind_list)  # run move_to
                            y, x = yx
                            direct = 1
                        else:
                            ext = 1  # if false, all areas have been visited, exit while loop

                    else:
                        x = x + 1
                        ind_list.append((y, x))

                        msg_count += 1

                        if test == 2:
                            print("Pos 4 Set: ({},{})".format(y, x))

                        if y + 1 >= len(plot_c) and template[y, x] == "0":
                            pass
                        elif y + 1 >= len(plot_c) and template[y, x] == "2":
                            direct = 3
                        elif plot_c[a, x] == 0 and template[y, x] == "2":
                            direct = 3
                        elif template[y, x] == "2":
                            print("error 1 right position 4")
                        elif template[y, x] == "0":
                            pass
                        # look at the nest 2's column

                # if position 3
                elif y - 1 >= 0 and plot_c[c, b] == 1:

                    if test == 1:
                        print("Pos 3")

                    if template[c, b] == "1":  # hit already completed section
                        new_plot = compare_plots(plot_c, 1, template, "2")
                        if test == 2:
                            print_plot(new_plot)
                        anw, yx = check_for_number(new_plot, "1")  # check if any uncompleted parts left

                        if anw:  # if true
                            yx, ind_list = asp.move_to_a_star(main, plot_c, yx, ind_list[-1], ind_list)  # run move_to
                            y, x = yx
                            direct = 1
                        else:
                            ext = 1  # if false, all areas have been visited, exit while loop

                    else:
                        y = c
                        x = b
                        ind_list.append((y, x))

                        msg_count += 1

                        if test == 2:
                            print("Pos 3 Set: ({},{})".format(y, x))
                        if y + 1 >= len(plot_c) and template[y, x] == "0":
                            pass
                        elif y + 1 >= len(plot_c) and template[y, x] == "2":
                            direct = 3
                        elif plot_c[y + 1, x] == 0 and template[y + 1, x] == "2":
                            direct = 3

                        elif template[y, x] == "2":
                            print("error 1 right position 3")
                        elif template[y, x] == "0":
                            pass

                else:
                    if test == 1:
                        print("Else")

                    if y - 1 >= 0 and plot_c[y-1, x] == 1:

                        y = y - 1
                        ind_list.append((y, x))

                        msg_count += 1

                        if test == 2:
                            print("Else  Set: ({},{})". format(y, x))
                    else:
                        if test == 2:
                            print("Else  Right 1 move_to")
                        new_plot = compare_plots(plot_c, 1, template, "2")
                        if test == 2:
                            print_plot(new_plot)
                        anw, yx = check_for_number(new_plot, "1")  # check if any uncompleted parts left

                        if anw:  # if true
                            yx, ind_list = asp.move_to_a_star(main, plot_c, yx, ind_list[-1], ind_list)  # run move_to
                            y, x = yx
                            direct = 1
                        else:
                            ext = 1  # if false, all areas have been visited, exit while loop

            # Up
            elif direct == 3:
                c = y - 1

                if y - 1 >= 0 and plot_c[c, x] == 1:     # if down is a valid move
                    y = c                   # set new y
                    template[y, x] = "1"    # set current point in template
                    ind_list.append((y, x))     # add co-or to list

                    msg_count += 1

                    if test == 2:
                        print("U Set: ({},{})". format(y, x))

                else:                       # if not set direction var to 2
                    direct = 4

            # Right 2
            elif direct == 4:
                a = y + 1
                b = x + 1
                c = y - 1

                # x + 1 is larger than shape
                if b > max_x:
                    new_plot = compare_plots(plot_c, 1, template, "2")
                    if test == 2:
                        print_plot(new_plot)
                    anw, yx = check_for_number(new_plot, "1")  # check if any uncompleted parts left

                    if anw:
                        yx, ind_list = asp.move_to_a_star(main, plot_c, yx, ind_list[-1], ind_list)  # run move_to
                        y, x = yx

                        direct = 1
                    else:
                        ext = 1  # if false, all areas have been visited, exit while loop

                # if position 3
                elif y - 1 >= 0 and plot_c[c, b] == 1:
                    if test == 2:
                        print(template[y, b])
                    if template[c, b] == "1":   # hit already completed section
                        new_plot = compare_plots(plot_c, 1, template, "2")
                        if test == 2:
                            print_plot(new_plot)
                        anw, yx = check_for_number(new_plot, "1")  # check if any uncompleted parts left

                        if anw:     # if true
                            yx, ind_list = asp.move_to_a_star(main, plot_c, yx, ind_list[-1], ind_list)  # run move_to
                            y, x = yx
                            direct = 1
                        else:
                            ext = 1  # if false, all areas have been visited, exit while loop

                    else:
                        y = c
                        x = b
                        ind_list.append((y, x))

                        msg_count += 1

                        if test == 2:
                            print("Pos 3 Set: ({},{})".format(y, x))

                        j = 0
                        while j != 1:   # to the end of the line

                            if x + 1 < len(template[0]) and template[y, x + 1] == "1":
                                break
                            elif y - 1 >= 0 and plot_c[y - 1, x] != 0:
                                y = y - 1
                                ind_list.append((y, x))

                                msg_count += 1

                                if test == 2:
                                    print("Por 3 Set: ({},{})".format(y, x))

                            else:
                                j = 1

                            if y - 1 <= 0:
                                direct = 1
                            elif plot_c[y - 1, x] == 0 and template[y - 1, x] == "2":
                                direct = 1

                # if position 4
                elif plot_c[y, b] == 1:

                    if template[y, b] == "1":  # hit already completed section
                        new_plot = compare_plots(plot_c, 1, template, "2")
                        if test == 2:
                            print_plot(new_plot)
                        anw, yx = check_for_number(new_plot, "1")  # check if any uncompleted parts left

                        if anw:  # if true
                            yx, ind_list = asp.move_to_a_star(main, plot_c, yx, ind_list[-1], ind_list)  # run move_to
                            y, x = yx
                            direct = 1
                        else:
                            ext = 1  # if false, all areas have been visited, exit while loop

                    else:
                        x = b
                        ind_list.append((y, x))

                        msg_count += 1

                        if test == 2:
                            print("Pos 4 Set: ({},{})".format(y, x))

                        if y - 1 < 0 and template[y, x] == "0":
                            pass
                        elif y - 1 < 0 and template[y, x] == "2":
                            direct = 1
                        elif plot_c[c, x] == 0 and template[y, x] == "2":
                            direct = 1
                        elif template[y, x] == "2":
                            if test == 2:
                                print("error 2 right position 4")
                        elif template[y, x] == "0":
                            pass
                        # look at the nest 2's column

                # if position 5
                elif y + 1 < len(plot_c) and plot_c[a, b] == 1:

                    if template[y, b] == "1":  # hit already completed section

                        new_plot = compare_plots(plot_c, 1, template, "2")
                        if test == 2:
                            print_plot(new_plot)
                        anw, yx = check_for_number(new_plot, "1")  # check if any uncompleted parts left

                        if anw:  # if true
                            yx, ind_list = asp.move_to_a_star(main, plot_c, yx, ind_list[-1], ind_list)  # run move_to
                            y, x = yx
                            direct = 1
                        else:
                            ext = 1  # if false, all areas have been visited, exit while loop

                    else:
                        y = a
                        x = b
                        ind_list.append((y, x))

                        msg_count += 1

                        if test == 2:
                            print("Pos 5  Set: ({},{})".format(y, x))

                        if y + 1 >= len(plot_c):
                            direct = 1
                        elif plot_c[y - 1, x] == 0 and template[y, x] == "2":
                            direct = 1
                        elif template[y, x] == "2":
                            if test == 2:
                                print("error 2 right position 5")
                                print(plot_c[y+1, x])
                                print_plot(plot_c)
                        elif template[y, x] == "0":
                            pass
                        # look at the nest 2's column

                else:
                    if y + 1 < len(plot_c) and plot_c[y + 1, x] == 1:

                        y = y + 1
                        ind_list.append((y, x))

                        msg_count += 1

                        if test == 2:
                            print("Else  Set: ({},{})".format(y, x))
                    else:
                        new_plot = compare_plots(plot_c, 1, template, "2")
                        if test == 2:
                            print("Else  Right 2 move_to")
                            print_plot(new_plot)
                        anw, yx = check_for_number(new_plot, "1")  # check if any uncompleted parts left

                        if anw:  # if true
                            yx, ind_list = asp.move_to_a_star(main, plot_c, yx, ind_list[-1], ind_list)  # run move_to
                            y, x = yx
                            direct = 1
                        else:
                            ext = 1  # if false, all areas have been visited, exit while loop
            # progress bar update
            if main is not None:
                if msg_count % 10 == 0:

                    msg = "Getting Fill Base...(Points Set: " + str(msg_count) + ")"
                    main.bar_update_message(msg)
                    main.bar_update_progress(0, 0.001, 1)
            # end

        plot_no_change = plot.copy()

        br_val = 0
        s2_yx = (0, 0)
        for y, row in enumerate(plot_c):
            for x, point in enumerate(row):
                if point == 1:
                    s2_yx = (y, x)
                    br_val = 1
                    break
            if br_val == 1:
                break
        if s2_yx != ind_list[-1]:
            s2_yx, ind_list = asp.move_to_a_star(main, plot_c, s2_yx, ind_list[-1], ind_list)

        # progress bar update
        if main is not None:
            msg_count = 0
            msg = "Getting Full Fill...(Points Set: " + str(msg_count) + ")"
            main.bar_update_message(msg)
        # end

        y, x = s2_yx
        direct = 1
        ext = 0
        if test == 2:
            print("Fill part 2")
        plot_c[y, x] = 2
        while ext != 1:     # horizontal tight stitches

            # Right
            if direct == 1:     # changed to x ****************
                b = x + 1

                if x + 1 < len(plot_c[0]) and plot_c[y, b] != 0:  # if Right is a valid move
                    x = b  # set new x
                    plot_c[y, x] = 2  # set current point in template
                    ind_list.append((y, x))  # add co-or to list

                    msg_count += 1

                    if test == 2:
                        print("R Set: ({},{})". format(y, x))
                else:  # if not set direction var to 2
                    direct = 2

            # Down 1
            elif direct == 2:
                a = y + 1
                b = x + 1
                d = x - 1

                # y + 1 is larger than shape
                if a > max_y or plot_c[a, d] == 2 or plot_c[a, x] == 2 or x + 1 < len(plot_c[0]) and plot_c[a, b] == 2:

                    anw, yx = check_for_number(plot_c, 1)

                    if anw:
                        y, x = yx
                        plot_c[y, x] = 2
                        yx, ind_list = asp.move_to_a_star(main, plot_no_change, yx, ind_list[-1], ind_list)
                        y, x = yx
                        direct = 1
                    else:
                        ext = 1  # if false, all areas have been visited, exit while loop

                # if position 5
                elif x + 1 < len(plot_c[0]) and plot_c[a, b] == 1:

                    y = a
                    x = b
                    ind_list.append((y, x))
                    plot_c[y, x] = 2

                    msg_count += 1

                    if test == 2:
                        print("Pos 5 Set: ({},{})". format(y, x))

                    j = 0
                    while j != 1:  # to the end of the line

                        if x + 1 < len(plot_c[0]) and plot_c[y, x + 1] != 0:
                            x = x + 1
                            ind_list.append((y, x))
                            plot_c[y, x] = 2

                            msg_count += 1

                            if test == 2:
                                print("Por 5 Set: ({},{})".format(y, x))
                        else:
                            j = 1

                        if x + 1 > len(plot_c[0]):
                            direct = 3
                        elif x + 1 > max_x or plot_c[y, x + 1] == 0:
                            direct = 3

                # if position 6
                elif plot_c[a, x] == 1:

                    y = a
                    ind_list.append((y, x))
                    plot_c[y, x] = 2

                    msg_count += 1

                    if test == 2:
                        print("Pos 6 Set: ({},{})". format(y, x))

                    if x + 1 >= len(plot_c[0]):
                        direct = 3
                    elif plot_c[y, b] == 0 or b > max_x:
                        direct = 3

                # if position 7
                elif x - 1 >= 0 and plot_c[a, d] == 1:
                    y = a
                    x = d
                    ind_list.append((y, x))
                    plot_c[y, x] = 2

                    msg_count += 1

                    if test == 2:
                        print("Pos 7 Set: ({},{})". format(y, x))

                    direct = 3

                else:

                    if x - 1 >= 0 and plot_c[y, d] == 2:
                        x = x - 1
                        ind_list.append((y, x))
                        plot_c[y, x] = 2

                        msg_count += 1

                        if test == 2:
                            print("Else Set: ({},{})".format(y, x))

                    else:
                        anw, yx = check_for_number(plot_c, 1)

                        if anw:
                            y, x = yx
                            plot_c[y, x] = 2
                            yx, ind_list = asp.move_to_a_star(main, plot_no_change, yx, ind_list[-1], ind_list)
                            y, x = yx
                            direct = 1
                        else:
                            ext = 1  # if false, all areas have been visited, exit while loop

            # Left
            elif direct == 3:
                d = x - 1

                if x - 1 >= 0 and plot_c[y, d] != 0:  # if left is a valid move
                    x = d  # set new x
                    ind_list.append((y, x))  # add co-or to list
                    plot_c[y, x] = 2

                    msg_count += 1

                    if test == 2:
                        print("L Set: ({},{})". format(y, x))

                else:  # if not set direction var to 2
                    direct = 4

            # Down 2
            elif direct == 4:
                a = y + 1
                b = x + 1
                d = x - 1

                # y + 1 is larger than shape
                if a > max_y or x - 1 >= 0 and plot_c[a, d] == 2 or plot_c[a, x] == 2 or x + 1 < len(plot_c[0]) and plot_c[a, b] == 2:
                    anw, yx = check_for_number(plot_c, 1)

                    if anw:
                        y, x = yx
                        plot_c[y, x] = 2
                        yx, ind_list = asp.move_to_a_star(main, plot_no_change, yx, ind_list[-1], ind_list)
                        y, x = yx
                        direct = 1
                    else:
                        ext = 1  # if false, all areas have been visited, exit while loop

                # if position 7
                elif x - 1 >= 0 and plot_c[a, d] == 1:

                    y = a
                    x = d
                    ind_list.append((y, x))
                    plot_c[y, x] = 2

                    msg_count += 1

                    if test == 2:
                        print("Pos 7 Set: ({},{})". format(y, x))

                    j = 0
                    while j != 1:  # to the end of the line

                        if plot_c[y, x - 1] != 0 and x - 1 >= 0:
                            x = x - 1
                            ind_list.append((y, x))
                            plot_c[y, x] = 2

                            msg_count += 1

                            if test == 2:
                                print("Por 7 Set: ({},{})".format(y, x))
                        else:
                            j = 1

                        if plot_c[y, x - 1] == 0 or x - 1 < min_x:
                            direct = 1

                # if position 6
                elif plot_c[a, x] == 1:

                    y = a
                    ind_list.append((y, x))
                    plot_c[y, x] = 2

                    msg_count += 1

                    if test == 2:
                        print("Pos 6 Set: ({},{})". format(y, x))

                    if plot_c[y, x - 1] == 0 or x - 1 < min_x:
                        direct = 1

                # if position 5
                elif x + 1 < len(plot_c[0]) and  plot_c[a, b] == 1:

                    y = a
                    x = b
                    ind_list.append((y, x))
                    plot_c[y, x] = 2

                    msg_count += 1

                    if test == 2:
                        print("Pos 5 Set: ({},{})". format(y, x))

                    if plot_c[y, x - 1] == 0 or x - 1 < min_x:
                        direct = 1

                else:

                    if x + 1 < len(plot_c[0]) and plot_c[y, b] == 2:
                        x = x + 1
                        ind_list.append((y, x))
                        plot_c[y, x] = 2

                        msg_count += 1

                        if test == 2:
                            print("Else Set: ({},{})".format(y, x))
                    else:
                        anw, yx = check_for_number(plot_c, 1)

                        if anw:
                            y, x = yx
                            plot_c[y, x] = 2
                            yx, ind_list = asp.move_to_a_star(main, plot_no_change, yx, ind_list[-1], ind_list)
                            y, x = yx
                            direct = 1
                        else:
                            ext = 1  # if false, all areas have been visited, exit while loop

            # progress bar update
            if main is not None:
                if msg_count % 10 == 0:
                    msg = "Getting Full Fill...(Points Set: " + str(msg_count) + ")"
                    main.bar_update_message(msg)
                    main.bar_update_progress(0, 0.001, 1)
            # end
        return ind_list


    def compare_plots(plot1, val1, plot2, val2):
        test = 0
        if test == 5:
            print("compare_plots - plot_objects.py")

        p_row = ["0"] * len(plot1[0])  # create blank plot make template plot
        blank_plot = np.array([p_row] * len(plot1))

        for y, row in enumerate(plot1):
            for x, point in enumerate(row):
                if point == val1 and plot2[y, x] == val2:
                    blank_plot[y, x] = "1"

        return blank_plot


    def find_path(main_plot, goto_yx, start_yx, ind_list):
        test = 0
        if test == 5:
            print("find_path - plot_objects.py")

        f_y, f_x = goto_yx
        y, x = start_yx
        col_num = 1

        p_row = [1] * len(main_plot[0])  # create blank plot make template plot
        plot = np.array([p_row] * len(main_plot))

        if test == 1 or test == 2 or test == 3:
            print("test in find_path")
            asp.print_node_plot(main_plot)
            print_plot(plot)

        ext = 0

        h = 0
        l_point = next_point(start_yx, goto_yx)

        if test == 2 or test == 3:
            print("Start: {} GoTo: {}".format(start_yx, goto_yx))

        if start_yx == goto_yx:
            return h, ind_list

        while ext != 1:

            # One
            if l_point == 1:  # check loop start

                if test == 1:  # testing console comments
                    print("# One")

                n_point = plot[y - 1, x - 1]  # set next point

                if n_point == col_num:  # check against colour_number
                    h += 14

                    if y - 1 == f_y and x - 1 == f_x:   # check if next point is destination
                        if test == 2:
                            print("return h: {}".format(h))
                        return h, ind_list  # if true then break loop and return h and ind_list

                    else:   # else record valid point
                        y -= 1  # set y to y - 1
                        x -= 1  # set x to x - 1

                        if test == 1 or test == 2:  # testing console comments
                            print("({},{}) +14".format(y, x))

                        ind_list.append((y, x))
                        cur_yx = (y, x)
                        l_point = next_point(cur_yx, goto_yx)  # get next position to check

            # Two
            elif l_point == 2:  # check loop start

                if test == 1:  # testing console comments
                    print("# Two")

                n_point = plot[y - 1, x]  # set next point

                if n_point == col_num:  # check against colour_number
                    h += 10

                    if y - 1 == f_y and x == f_x:  # check if next point is destination
                        if test == 2:
                            print("return h: {}". format(h))
                        return h, ind_list  # if true then break loop and return h and ind_list

                    else:  # else record valid point

                        y -= 1  # set y to y - 1

                        if test == 1 or test == 2:  # testing console comments
                            print("({},{}) +10".format(y, x))

                        ind_list.append((y, x))
                        cur_yx = (y, x)  # combine current y, x
                        l_point = next_point(cur_yx, goto_yx)  # get next position to check

            # Three
            elif l_point == 3:  # check if this point is within the plot limits

                if test == 1:  # set this point
                    print("# Three")

                n_point = plot[y - 1, x + 1]  # set next point

                if n_point == col_num:  # check against colour_number

                    h += 14

                    if y - 1 == f_y and x + 1 == f_x:  # check if next point is destination
                        if test == 2:
                            print("return h: {}".format(h))
                        return h, ind_list  # if true then break loop and return h and ind_list

                    else:  # else record valid point
                        y -= 1  # set y to y - 1
                        x += 1  # set x to x + 1

                        if test == 1 or test == 2:  # testing console comments
                            print("({},{}) +14".format(y, x))

                        ind_list.append((y, x))
                        cur_yx = (y, x)  # combine current y, x
                        l_point = next_point(cur_yx, goto_yx)  # get next position to check

            # Four
            elif l_point == 4:  # check loop start

                if test == 1:  # testing console comments
                    print("# Four")

                n_point = plot[y, x + 1]  # set this point

                if n_point == col_num:  # check against colour_number

                    h += 10

                    if y == f_y and x + 1 == f_x:  # check if next point is destination
                        if test == 2:
                            print("return h: {}".format(h))
                        return h, ind_list  # if true then break loop and return h and ind_list

                    else:  # else record valid point

                        x += 1  # set x to x + 1

                        if test == 1 or test == 2:  # testing console comments
                            print("({},{} +10)".format(y, x))

                        ind_list.append((y, x))
                        cur_yx = (y, x)  # combine current y, x
                        l_point = next_point(cur_yx, goto_yx)  # get next position to check

            # Five
            elif l_point == 5:  # check loop start

                if test == 1:  # testing console comments
                    print("# Five")

                n_point = plot[y + 1, x + 1]  # set this point

                if n_point == col_num:  # check against colour_number

                    h += 14

                    if y + 1 == f_y and x + 1 == f_x:  # check if next point is destination
                        if test == 2:
                            print("return h: {}".format(h))
                        return h, ind_list  # if true then break loop and return h and ind_list

                    else:  # else record valid point

                        y += 1  # set y to y + 1
                        x += 1  # set x to x + 1

                        if test == 1 or test == 2:  # testing console comments
                            print("({},{}) +14".format(y, x))

                        ind_list.append((y, x))
                        cur_yx = (y, x)  # combine current y, x
                        l_point = next_point(cur_yx, goto_yx)  # get next position to check

            # Six
            elif l_point == 6:  # check loop start

                if test == 1:  # testing console comments
                    print("# Six")

                n_point = plot[y + 1, x]  # set this point

                if n_point == col_num:  # check against colour_number

                    h += 10

                    if y + 1 == f_y and x == f_x:  # check if next point is destination
                        if test == 2:
                            print("return h: {}".format(h))
                        return h, ind_list  # if true then break loop and return h and ind_list

                    else:  # else record valid point

                        y += 1  # set y to y + 1

                        if test == 1 or test == 2:  # testing console comments
                            print("({},{}) +10".format(y, x))

                        ind_list.append((y, x))
                        cur_yx = (y, x)  # combine current y, x
                        l_point = next_point(cur_yx, goto_yx)  # get next position to check

            # Seven
            elif l_point == 7:  # check loop start

                if test == 1:  # testing console comments
                    print("# Seven")

                n_point = plot[y + 1, x - 1]  # set this point

                if n_point == col_num:  # check against colour_number

                    h += 14

                    if y + 1 == f_y and x - 1 == f_x:  # check if next point is destination
                        if test == 2:
                            print("return h: {}".format(h))
                        return h, ind_list  # if true then break loop and return h and ind_list

                    else:  # else record valid point

                        y += 1  # set y to y + 1
                        x -= 1  # set x to x - 1

                        if test == 1 or test == 2:  # testing console comments
                            print("({},{}) +14".format(y, x))

                        ind_list.append((y, x))
                        cur_yx = (y, x)  # combine current y, x
                        l_point = next_point(cur_yx, goto_yx)  # get next position to check

            # Eight
            elif l_point == 8:  # check loop start

                if test == 1:  # testing console comments
                    print("# Eight")

                n_point = plot[y, x - 1]  # set this point

                if n_point == col_num:  # check against colour_number

                    h += 10

                    if y == f_y and x - 1 == f_x:  # check if next point is destination
                        if test == 2:
                            print("return h: {}".format(h))
                        return h, ind_list  # if true then break loop and return h and ind_list

                    else:  # else record valid point

                        x -= 1  # set x to x - 1

                        if test == 1 or test == 2:  # testing console comments
                            print("({},{}) +10".format(y, x))

                        ind_list.append((y, x))
                        cur_yx = (y, x)  # combine current y, x
                        l_point = next_point(cur_yx, goto_yx)  # get next position to check


    def next_point(yx_st, yx_fn):
        test = 0
        if test == 5:
            print("next_point - plot_objects.py")
        start_p = 1

        c_y, c_x = yx_st
        f_y, f_x = yx_fn

        sum_y = f_y - c_y
        sum_x = f_x - c_x

        if sum_y < 0:
            # - y
            if sum_x < 0:
                # - x
                start_p = 1

            elif sum_x > 0:
                # + x
                start_p = 3

            else:
                # x
                start_p = 2

        elif sum_y > 0:
            # + y
            if sum_x < 0:
                # - x
                start_p = 7

            elif sum_x > 0:
                # + x
                start_p = 5

            else:
                # x
                start_p = 6

        elif sum_y == 0:
            # y
            if sum_x < 0:
                # - x
                start_p = 8

            elif sum_x > 0:
                # + x
                start_p = 4

        return start_p


    def reversible_mine_sweeper_fill(main_plot, ref_plot, max_yx, min_yx, set_to, col_num, arg):
        test = 0
        if test == 5:
            print("reversible_mine_sweeper_fill - plot_objects.py")

        copy_col_num = col_num
        plot = main_plot
        min_y, min_x = min_yx
        max_y, max_x = max_yx
        l_len = len(ref_plot)
        r_len = len(ref_plot[0])
        change = 1
        j = 0
        bol = isinstance(ref_plot[0, 0], str)

        if test == 1:
            print("max_yx: {} min_yx: {}".format(max_yx, min_yx))

        if bol and arg == 1:
            col_num = "a"
            set_to = str(set_to)
        elif bol and arg == 2:
            col_num = "b"
            set_to = str(set_to)
        elif bol and arg == 3:
            col_num = str(col_num)
            set_to = str(set_to)

        while change == 1:
            change = 0

            # while flip < 2:
            for y, row in enumerate(ref_plot):
                for x, point in enumerate(ref_plot[0]):
                    if min_x <= x <= max_x and min_y <= y <= max_y:
                        if plot[y, x] == copy_col_num:
                            if ref_plot[y, x] == col_num:
                                points = get_surrounding_points(plot, ref_plot, y, x, copy_col_num)

                                if set_to not in points:
                                    pass
                                else:

                                    if test == 1:
                                        print("Fill Set({},{})".format(y, x))
                                    ref_plot[y, x] = set_to
                                    change = 1

            while l_len >= 0:

                x = r_len
                while x >= 0:
                    y = l_len

                    if test == 1:
                        print("l_len: {} r_len: {}".format(l_len, x))

                    if min_x <= x <= max_x and min_y <= y <= max_y:
                        if plot[y, x] == copy_col_num:

                            if ref_plot[y, x] == col_num:
                                points = get_surrounding_points(plot, ref_plot, y, x, copy_col_num)

                                if set_to not in points:
                                    pass
                                else:
                                    if test == 1:
                                        print("Re Fill ({},{})".format(y, x))
                                    ref_plot[y, x] = set_to
                                    change = 1
                    x -= 1
                l_len -= 1


    def check_for_number(plot, num):
        test = 0
        if test == 5:
            print("check_for_number - class Plot - plot_objects.py")

        yx = (0, 0)
        bol = isinstance(plot[0, 0], str)
        bol2 = isinstance(num, str)
        if bol and not bol2:
            num = str(num)
        elif not bol and bol2:
            num = int(num)

        for y, row in enumerate(plot):
            for x, point in enumerate(row):
                if point == num:
                    yx = (y, x)
                    return True, yx

        return False, yx


    def valid_position(main_plot, y, x, col_num, con_col):
        test = 0
        if test == 5:
            print("valid_position - class Plot - plot_objects.py")

        test = 0

        if test >= 1:
            print("Valid position check: ({},{})".format(y, x))
            print("col_num Value: {}".format(col_num))

        points, yx_points = get_surrounding_points_5x5(main_plot, y, x)
        val_list, amount_list = count_list(points)
        anw = t_w_p_logic(col_num, con_col, val_list, amount_list)

        return anw


    def get_surrounding_points(plot, out_plot, y, x, col_num):
        test = 0
        if test == 5:
            print("get_surrounding_point - class Plot - plot_objects.py")

        row_num = len(out_plot)
        cul_num = len(out_plot[0])
        points = []
        a = y - 1
        b = y + 1
        c = x - 1
        d = x + 1
        if test == 1:
            print("Centre: ({},{})".format(y, x))
        if y > 0:
            p_a = plot[y - 1, x]
            points.append(out_plot[a, x])
            if test == 1:
                print(" Sur_2: ({},{})".format(a, x))

            if x > 0:
                p_c = plot[y, x - 1]
                if p_a != p_c:
                    points.append(out_plot[a, c])
                    if test == 1:
                        print(" Sur_1: ({},{})".format(a, c))
                elif p_a == p_c and p_a != col_num:  # and out_plot[a, c] == out_plot[y, x]:
                    anw = valid_position(plot, y - 1, x - 1, col_num, p_a)
                    if anw == 1:
                        points.append(out_plot[a, c])
                        if test == 1:
                            print(" Sur_1: ({},{})".format(a, c))
                    else:
                        if test == 1:
                            print("({},{}) not valid".format(a, c))

            if x < cul_num - 1:
                p_d = plot[y, x + 1]
                if p_a != p_d:
                    points.append(out_plot[a, d])
                    if test == 1:
                        print(" Sur_3: ({},{})".format(a, d))
                elif p_a == p_d and p_a != col_num:  # and out_plot[a, d] == out_plot[y, x]:
                    anw = valid_position(plot, y - 1, x + 1, col_num, p_a)
                    if anw == 1:
                        points.append(out_plot[a, d])
                        if test == 1:
                            print(" Sur_3: ({},{})".format(a, d))
                    else:
                        if test == 1:
                            print("({},{}) not valid".format(a, d))

        if y < row_num - 1:
            p_b = plot[y + 1, x]
            points.append(out_plot[b, x])
            if test == 1:
                print(" Sur_6: ({},{})".format(b, x))
            if x > 0:
                p_c = plot[y, x - 1]
                if p_b != p_c:
                    points.append(out_plot[b, c])
                    if test == 1:
                        print(" Sur_7: ({},{})".format(b, c))
                elif p_b == p_c and p_b != col_num:  # and out_plot[b, c] == out_plot[y, x]:
                    anw = valid_position(plot, y + 1, x - 1, col_num, p_b)
                    if anw == 1:
                        points.append(out_plot[b, c])
                        if test == 1:
                            print(" Sur_7: ({},{})".format(b, c))
                    else:
                        if test == 1:
                            print("({},{}) not valid".format(b, c))

            if x < cul_num - 1:
                p_c = plot[y, x + 1]
                if p_b != p_c:
                    points.append(out_plot[b, d])
                    if test == 1:
                        print(" Sur_5: ({},{})".format(b, d))
                elif p_b == p_c and p_b != col_num:  # and out_plot[b, d] == out_plot[y, x]:
                    anw = valid_position(plot, y + 1, x + 1, col_num, p_b)
                    if anw == 1:
                        points.append(out_plot[b, d])
                        if test == 1:
                            print(" Sur_5: ({},{})".format(b, d))
                    else:
                        if test == 1:
                            print("({},{}) not valid".format(b, d))

        if x > 0:
            points.append(out_plot[y, c])
            if test == 1:
                print(" Sur_8: ({},{})".format(y, c))
        if x < cul_num - 1:
            points.append(out_plot[y, d])
            if test == 1:
                print(" Sur_4: ({},{})".format(y, d))
        return points


    def get_surrounding_points_5x5(main_plot, y, x):
        test = 0
        if test == 5:
            print("get_surrounding_points_5x5 - class Plot - plot_objects.py")

        row_num = len(main_plot)
        col_num = len(main_plot[0])
        points = []
        yx_points = []
        a = y - 2
        b = y + 2
        c = x - 2
        d = x + 2
        e = y - 1
        f = y + 1
        g = x - 1
        h = x + 1

        points.append(main_plot[y, x])
        yx_points.append((y, x))

        if y >= 2:
            points.append(main_plot[a, x])
            yx_points.append((a, x))
            if x >= 2:
                points.append(main_plot[a, c])
                yx_points.append((a, c))

            if x >= 1:
                points.append(main_plot[a, g])
                yx_points.append((a, g))

            if x < col_num - 2:
                points.append(main_plot[a, d])
                yx_points.append((a, d))

            if x < col_num - 1:
                points.append(main_plot[a, h])
                yx_points.append((a, h))

        if y >= 1:
            points.append(main_plot[e, x])
            yx_points.append((e, x))
            if x >= 2:
                points.append(main_plot[e, c])
                yx_points.append((e, c))

            if x >= 1:
                points.append(main_plot[e, g])
                yx_points.append((e, g))

            if x < col_num - 2:
                points.append(main_plot[e, d])
                yx_points.append((e, d))

            if x < col_num - 1:
                points.append(main_plot[e, h])
                yx_points.append((e, h))

        if y < row_num - 2:
            points.append(main_plot[b, x])
            yx_points.append((b, x))
            if x >= 2:
                points.append(main_plot[b, c])
                yx_points.append((b, c))

            if x >= 1:
                points.append(main_plot[b, g])
                yx_points.append((b, g))

            if x < col_num - 2:
                points.append(main_plot[b, d])
                yx_points.append((b, d))

            if x < col_num - 1:
                points.append(main_plot[b, h])
                yx_points.append((b, h))

        if y < row_num - 1:
            points.append(main_plot[f, x])
            yx_points.append((f, x))
            if x >= 2:
                points.append(main_plot[f, c])
                yx_points.append((f, c))

            if x >= 1:
                points.append(main_plot[f, g])
                yx_points.append((f, g))

            if x < col_num - 2:
                points.append(main_plot[f, d])
                yx_points.append((f, d))

            if x < col_num - 1:
                points.append(main_plot[f, h])
                yx_points.append((f, h))

        if x >= 2:
            points.append(main_plot[y, c])
            yx_points.append((y, c))

        if x >= 1:
            points.append(main_plot[y, g])
            yx_points.append((y, g))

        if x < col_num - 2:
            points.append(main_plot[y, d])
            yx_points.append((y, d))

        if x < col_num - 1:
            points.append(main_plot[y, h])
            yx_points.append((y, h))

        return points, yx_points


    def count_list(points):
        test = 0
        if test == 5:
            print("count_list - class Plot - plot_objects.py")

        val_list = []
        amount_list = []

        for x, pon in enumerate(points):

            # count the number of times a pixel appears
            if len(val_list) == 0:
                val_list.append(pon)
                amount_list.append(1)

            else:
                count = 0
                for i in val_list:

                    if i == pon:

                        ind = val_list.index(i)
                        amount_list[ind] += 1

                    else:
                        count += 1

                    if count >= len(val_list):
                        val_list.append(pon)
                        amount_list.append(1)
                        break

        return val_list, amount_list


    def t_w_p_logic(col_num, con_col, val_list, amount_list):
        test = 0
        if test == 5:
            print("t_w_p_logic - class Plot - plot_objects.py")

        test = 0

        if test >= 1:
            print("** t_w_p_logic() console debug **")
            print("col_num: {} ".format(col_num))

        if col_num not in val_list:
            if test == 1:
                print("*** {} not in list".format(col_num))
            return 2
        else:
            ind = val_list.index(con_col)
            con_amount = amount_list[ind]
            ind = val_list.index(col_num)
            col_amount = amount_list[ind]

            if con_amount > col_amount:
                if test >= 1:
                    print("T_W_P Return: 1")
                    print("** end **")
                return 1
            elif con_amount < col_amount:
                if test == 1:
                    print("col_con is the line")
                return 2
            else:
                if test == 1:
                    print("Both are equal")
                return 3


    def print_plot(plot):
        test = 5
        if test == 5:
            print("print_plot - class Plot - plot_objects.py")

        bol = isinstance(plot[0, 0], str)

        if bol:
            pass

        for y, row in enumerate(plot):
            p_row = ""
            for x, point in enumerate(row):

                if bol:
                    if point == "0":
                        p_row = p_row + "."
                    else:
                        p_row = p_row + point
                else:
                    if point == 0:
                        p_row = p_row + "."
                    else:
                        p_row = p_row + str(point)

            print(p_row)


    def print_plot_advanced(plot):
        test = 5
        if test == 5:
            print("print_plot_advanced - class Plot - plot_objects.py")

        bol = isinstance(plot[0, 0], str)

        if bol:
            pass

        for y, row in enumerate(plot):
            p_row = ""
            for x, point in enumerate(row):

                if bol:
                    if point == "0":
                        p_row = p_row + ". "
                    elif point == "2":
                        p_row = p_row + "_ "
                    elif point == "b":
                        p_row = p_row + ", "
                    else:
                        p_row = p_row + point + " "
                else:
                    if point == 0:
                        p_row = p_row + ". "
                    elif point == 2:
                        p_row = p_row + "_ "
                    else:
                        p_row = p_row + str(point) + " "

            print(p_row)



if __name__ == '__main__':
    unittest.main()

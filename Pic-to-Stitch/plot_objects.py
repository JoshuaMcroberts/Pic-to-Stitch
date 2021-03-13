import numpy as np


class Plot:

    def __init__(self, plot_matrix):

        self.matrix = plot_matrix
        self.col_list = []
        self.col_amount = 0
        self.matrix_width = len(self.matrix[0])
        self.matrix_height = len(self.matrix)
        self.col_matrix_list = []

    def set_num_list(self, colour_list):
        self.col_list = colour_list
        self.col_amount = len(self.col_list)

    def set_matrix_w_h(self):
        self.matrix_width = len(self.matrix[0])
        self.matrix_height = len(self.matrix)

    def create_sub_plot(self):

        for i in range(self.col_amount):
            print(i)
            colour = self.col_list[i]
            print(self.col_list)
            p_row = [0] * self.matrix_width
            plot = np.array([p_row] * self.matrix_height)

            for y, row in enumerate(self.matrix):
                for x, point in enumerate(row):

                    if self.matrix[y, x] == i+1:
                        plot[y, x] = i+1

            col_plot = ColourPlot(plot, i+1, colour)
            self.col_matrix_list.append(col_plot)

    def print_col_matrix_list(self):

        if not self.col_matrix_list:
            print("Not Matrix' in list")
        else:
            for i in self.col_matrix_list:
                p_object = i
                plot = p_object.matrix
                ind = self.col_matrix_list.index(i)
                print("Colour: {}".format(ind))
                for y, row in enumerate(plot):
                    p_row = ""
                    for x, point in enumerate(row):

                        if point == 0:
                            p_row = p_row + ". "
                        else:
                            p_row = p_row + str(point) + " "

                    print(p_row)


class ColourPlot(Plot):

    def __init__(self, matrix, colour_number, colour):
        super().__init__(matrix)
        # self.plot_matrix = plot_matrix
        self.col_num = colour_number
        self.ref_plot = self.create_ref_plot(1)
        self.object_count = 0
        self.colour = colour
        self.ob_matrix_list = []

    def create_ref_plot(self, arg):

        self.set_matrix_w_h()
        if arg == 1:
            p_row = ["0"] * self.matrix_width
        elif arg == 2:
            p_row = ["b"] * self.matrix_width
        else:
            p_row = ["0"] * self.matrix_width

        ref_plot = np.array([p_row] * self.matrix_height)

        for y, row in enumerate(self.matrix):
            for x, point in enumerate(row):

                val = self.matrix[y, x]
                if val == self.col_num:
                    val = "a"
                elif val == 0 and arg == 2:
                    val = "b"
                else:
                    val = str(val)
                ref_plot[y, x] = val
        return ref_plot

    def process_colour_plot(self, main_plot):
        ref_plot = self.ref_plot
        plot = self.matrix
        ob_count = self.object_count
        col_num = self.col_num
        col_letter = "a"
        count = 0
        i = 0

        for y, row in enumerate(ref_plot):
            # if i > 4:
            #     break

            for x, point in enumerate(row):

                if point == col_letter:
                    count += 1
                    max_yx, min_yx, ind_list = get_object_outline(main_plot, ref_plot, (y, x), 8, count, col_num)
                    print_plot(ref_plot)
                    print("")
                    reversible_mine_sweeper_fill(main_plot, ref_plot, max_yx, min_yx, count, col_num, 1)
                    print_plot(ref_plot)
                i += 1
        self.ref_plot = ref_plot

    def set_object_count(self):
        plot = self.ref_plot
        num = []
        row_list = []
        for i, row in enumerate(plot):
            for x, point in enumerate(row):
                bol = isinstance(point, str)
                if bol:
                    point = int(point)
                    row_list.append(point)

            val = max(row_list)
            num.append(val)
        val = max(num)
        print("count is : {}".format(val))
        self.object_count = val

    def create_object_sub_plot(self):

        self.set_object_count()

        for i in range(self.object_count):
            print(i+1)
            colour = self.colour

            self.set_matrix_w_h()

            p_row = [0] * self.matrix_width
            plot = np.array([p_row] * self.matrix_height)

            for y, row in enumerate(self.ref_plot):
                for x, point in enumerate(row):

                    if self.ref_plot[y, x] == str(i + 1):
                        plot[y, x] = str(i + 1)
            # print_plot(plot)
            ob_plot = ObjectPlot(plot, i + 1, i + 1, colour)
            self.ob_matrix_list.append(ob_plot)

    def print_ob_matrix_list(self):

        if not self.ob_matrix_list:
            print("Not Matrix' in list")
        else:
            for i in self.ob_matrix_list:
                p_object = i
                plot = p_object.matrix
                ind = self.ob_matrix_list.index(i)
                print("Object: {}".format(ind + 1))
                for y, row in enumerate(plot):
                    p_row = ""
                    for x, point in enumerate(row):

                        if point == 0:
                            p_row = p_row + ". "
                        else:
                            p_row = p_row + str(point) + " "

                    print(p_row)


class ObjectPlot(ColourPlot):

    def __init__(self, matrix, colour_number, object_number, colour):
        super().__init__(matrix, colour_number, colour)
        self.ob_id = object_number
        self.out_ob = 0
        self.in_ob = 2
        self.ob_fill_all = []
        self.ob_outline = []
        self.ob_run_fill = []
        self.colour = colour
        self.ref_plot = self.create_ref_plot(2)
        self.ob_parts_list = []
        self.section_image = int()

    def process_colour_plot(self, main_plot):
        test = 0
        ref_plot = self.ref_plot
        col_num = self.col_num
        col_letter_list = ["b", "a"]
        plot_h = len(ref_plot)
        plot_w = len(ref_plot[0])

        if test == 1:
            print("plot_h: {} plot_w: {}".format(plot_h, plot_w))

        co_or_list = [(0, 0), (0, plot_w - 1), (plot_h - 1, 0), (plot_h - 1, plot_w - 1)]
        l_point = [8, 2, 6, 4]
        val_list = ["0", "2", "1"]

        for i in co_or_list:
            ind = co_or_list.index(i)
            l_p = l_point[ind]
            y, x = i
            point = ref_plot[y, x]
            val = val_list[0]

            if point == col_letter_list[0]:     # Sets the background colour

                max_yx, min_yx, ind_list = get_object_outline(main_plot, ref_plot, (y, x), l_p, val, col_num)
                print_plot(ref_plot)
                print("")
                reversible_mine_sweeper_fill(main_plot, ref_plot, max_yx, min_yx, val, col_num, 2)
                print_plot(ref_plot)

        for y, row in enumerate(ref_plot):
            for x, point in enumerate(row):

                if point == col_letter_list[1]:

                    max_yx, min_yx, ind_list = get_object_outline(main_plot, ref_plot, (y, x), 8, "1", "a")
                    print_plot_advanced(ref_plot)
                    print("")
                    reversible_mine_sweeper_fill(main_plot, ref_plot, max_yx, min_yx, "1", 2, 1)
                    print_plot_advanced(ref_plot)

        for y, row in enumerate(ref_plot):
            for x, point in enumerate(row):

                if point == col_letter_list[0]:

                    max_yx, min_yx, ind_list = get_object_outline(ref_plot, ref_plot, (y, x), 8, "2", 2)
                    print_plot_advanced(ref_plot)
                    print("")
                    reversible_mine_sweeper_fill(ref_plot, ref_plot, max_yx, min_yx, "2", "b", 2)
                    print_plot_advanced(ref_plot)

    def create_pathing_lists(self):
        test = 0
        plot = self.matrix.copy()

        new_plot = plot.copy()
        b_val = 0

        for y, row in enumerate(plot):
            for x, point in enumerate(row):
                if point == 1:
                    out = get_object_outline(plot, new_plot, (y, x), 8, 1, 1)
                    ind_list = out[2]
                    self.ob_outline = ind_list  # Outline co-or list
                    b_val = 1
                    break
            if b_val == 1:
                break

        self.running_stitch_fill()

        self.fill_stitch_fill()

    def process_matrix(self):
        plot = self.matrix

        for y, row in enumerate(plot):
            for x, point in enumerate(row):
                if point != 0:
                    self.matrix[y, x] = 1

    # not used?
    def get_ob_lines(self):

        if not self.ob_parts_list:
            print("not objects in list")

        elif len(self.ob_parts_list) < 2:
            print("not enough data")

        else:
            base_plot = self.ob_parts_list[0]
            ref_plot = self.ob_parts_list[1]
            print("Base")
            print_plot(base_plot)
            for y, row in enumerate(ref_plot):
                for x, point in enumerate(row):
                    if point == "1":
                        base_plot[y, x] = "2"
            return base_plot

    def running_stitch_fill(self):

        plot = self.matrix.copy()   # untouched only for reference
        new_plot = self.matrix.copy()
        b_val = 0
        count = 4

        for y, row in enumerate(plot):
            for x, point in enumerate(row):
                if point == 1:
                    max_yx, min_yx, ind_list = get_object_outline(plot, new_plot, (y, x), 8, count, 1)

                    anw, yx = check_for_number(new_plot, 1)

                    ind_list = get_object_outline_fill(plot, new_plot, yx, 8, count, 1, ind_list)
                    self.ob_run_fill = ind_list
                    b_val = 1
                    break
            if b_val == 1:
                break

    def fill_stitch_fill(self):
        test = 0
        plot = self.matrix.copy()
        print("fill stitch fill")
        print_plot_advanced(plot)
        ref_plot = self.ref_plot.copy()
        min_yx = (0, 0)
        max_yx = (len(plot), len(plot[0]))
        br_val = 0
        ind_list = []
        start_val = 0

        # works
        p_row = ["0"] * len(ref_plot[0])    # create blank polt make template plot
        blank_plot = np.array([p_row] * len(ref_plot))
        template = blank_plot.copy()    

        # works
        for y, row in enumerate(template):  # create skip a column template plot
            for x, point in enumerate(row):
                if (x % 2) == 0:
                    template[y, x] = "2"
        
        if test == 1:   # testing comment for console debug
            print_plot_advanced(template)
            print(" ")
            print_plot_advanced(plot)

        # works
        for y, row in enumerate(plot):  # set outline point in ind_list and get min_x for start point
            for x, point in enumerate(row):

                if point == 1:
                    max_yx, min_yx, ind_list = get_object_outline(plot, ref_plot, (y, x), 8, 3, 1)
                    br_val = 1
                    break

            if br_val == 1:
                break
        if test == 1:
            print("before min_yx: {}".format(min_yx))
            min_y, min_x = min_yx
            print("after min_x: {}".format(min_x))
        else:
            min_y, min_x = min_yx

        # works
        for y, row in enumerate(plot):  # get start point by finding valid point that matches both template and plot
            p_a = row[min_x]
            p_b = row[min_x + 1]
            tem_p_a = template[y, min_x]
            tem_p_b = template[y, min_x + 1]

            if test == 1:

                print("y: {} plot val: {}".format(y, p_a))

            if p_a == 1 and tem_p_a == "2":
                start_val = (y, min_x)
                break
            elif p_b == 1 and tem_p_b == "2":
                start_val = (y, min_x + 1)
                break
            else:
                print("not set")

        if test == 1:
            print(ind_list)

        end_p = ind_list[-1]

        print("Start Val: {}".format(start_val))
        print("end Point: {}".format(end_p))

        if start_val == end_p:
            pass
        else:
            goto, ind_list = move_to(plot, start_val, end_p, 2, 1, ind_list)

        ind_list = get_object_fill_stitch(template, plot, start_val, max_yx, min_yx, ind_list)

        self.ob_fill_all = ind_list
                
    def print_ob_part_list(self):
        if not self.ob_parts_list:
            print("Not Matrix' in list")
        else:
            for i, item in enumerate(self.ob_parts_list):

                print("Item {}".format(i+1))
                print_plot(item)


def stitch_test(plot, ind_list):
    print("Stitch TEST")
    p_row = ["0"] * len(plot[0])
    blank_plot = np.array([p_row] * len(plot))

    for i in ind_list:
        y, x = i

        blank_plot[y, x] = "1"

    print_plot(blank_plot)


def get_object_outline(main_plot, ref_plot, start_yx, start_point, set_to, col_num):
    test = 0

    plot = main_plot
    y, x = start_yx
    l_point = start_point
    ind_list = []
    plot_h = len(ref_plot)
    plot_w = len(ref_plot[0])
    # count = 1
    if test == 2:
        print("COL_NUM: {}".format(col_num))

    bol = isinstance(ref_plot[0, 0], str)

    if bol:
        set_to = str(set_to)

    ref_plot[y, x] = set_to
    ind_list.append((y, x))

    for j in range(len(plot)*len(plot[0])):

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
                        comp = False
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
                        if anw == 2:
                            pass
                        if anw == 3:
                            pass

                    else:
                        if (y - 1, x - 1) == ind_list[0]:
                            break
                        else:
                            comp = True
                            # print("y-1, x+1")
                            # check outline_list
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
                        # print("y-1")

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
                        comp = False
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
                        if anw == 2:
                            pass
                        if anw == 3:
                            pass

                    else:
                        if (y - 1, x + 1) == ind_list[0]:
                            break
                        else:
                            comp = True
                            # print("y-1, x+1")
                            # check outline_list
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
                        comp = True
                        # print("x+1")
                        # check outline_list
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
                        comp = False
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
                        if anw == 2:
                            pass
                        if anw == 3:
                            pass

                    else:
                        if (y + 1, x + 1) == ind_list[0]:
                            break
                        else:
                            comp = True
                            # print("y+1, x+1")
                            # check outline_list
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

                        # print("y+1")
                        # check outline_list
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
                        comp = False
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
                        if anw == 2:
                            pass
                        if anw == 3:
                            pass
                    else:
                        if (y + 1, x - 1) == ind_list[0]:
                            break
                        else:
                            comp = True
                            # print("y+1, x-1")
                            # check outline_list
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
    # print_plot(ref_plot)

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


def get_object_outline_fill(main_plot, ref_plot, start_yx, start_point, set_to, col_num, ind_list):
    test = 0
    ref_plot = ref_plot.copy()
    plot = main_plot.copy()
    y, x = start_yx
    l_point = start_point
    ind_list = ind_list
    print(ind_list)
    plot_h = len(ref_plot)
    plot_w = len(ref_plot[0])
    # count = 1
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

        print("First Set ({},{})".format(y, x))

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

            if l_point != 4:    # check if loop start was set
                l_point = 8     # if not, set to the next position

        if loop > 16:

            if test == 1 or test == 2:
                print("trapped")

            bol, yx = check_for_number(ref_plot, 1)

            if bol:
                yx, ind_list = move_to(plot, yx, ind_list[-1], set_to, 1, ind_list)
                y, x = yx
                print("Move_ Set ({},{})".format(y, x))
                ref_plot[y, x] = set_to
                loop = 0
            else:
                print("Exit")
                ext = 1

        loop += 1   # counts the number of loops without a point being set

    print_plot(ref_plot)

    return ind_list


def get_object_fill_stitch(template, plot, start_yx, max_yx, min_yx, ind_list):
    test = 0

    s_y, s_x = start_yx
    y = s_y
    x = s_x
    direct = 1
    ext = 0
    plot_c = plot.copy()
    max_y, max_x = max_yx
    min_y, min_x = min_yx

    print(ind_list)
    if test == 1 or test == 2:
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
            else:                       # if not set direction var to 2
                direct = 2

        # Right 1
        elif direct == 2:
            if test == 1:
                print("# Right 1")

            a = y + 1
            b = x + 1
            c = y - 1

            # x + 1 is larger than shape
            print(max_x," ", b)
            if b > max_x:
                new_plot = compare_plots(plot_c, 1, template, "2")
                print_plot(new_plot)
                anw, yx = check_for_number(new_plot, "1")

                if anw:
                    yx, ind_list = move_to(plot_c, yx, ind_list[-1], 4, 1, ind_list)
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
                    print_plot(new_plot)
                    anw, yx = check_for_number(new_plot, "1")  # check if any uncompleted parts left

                    if anw:  # if true
                        yx, ind_list = move_to(plot_c, yx, ind_list[-1], 4, 1, ind_list)  # run move_to
                        y, x = yx
                        direct = 1
                    else:
                        ext = 1  # if false, all areas have been visited, exit while loop

                else:

                    y = a
                    x = b
                    ind_list.append((y, x))
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
                    print_plot(new_plot)
                    anw, yx = check_for_number(new_plot, "1")  # check if any uncompleted parts left

                    if anw:  # if true
                        yx, ind_list = move_to(plot_c, yx, ind_list[-1], 4, 1, ind_list)  # run move_to
                        y, x = yx
                        direct = 1
                    else:
                        ext = 1  # if false, all areas have been visited, exit while loop

                else:
                    x = x + 1
                    ind_list.append((y, x))
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
                    print_plot(new_plot)
                    anw, yx = check_for_number(new_plot, "1")  # check if any uncompleted parts left

                    if anw:  # if true
                        yx, ind_list = move_to(plot_c, yx, ind_list[-1], 4, 1, ind_list)  # run move_to
                        y, x = yx
                        direct = 1
                    else:
                        ext = 1  # if false, all areas have been visited, exit while loop

                else:
                    y = c
                    x = b
                    ind_list.append((y, x))
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
                    if test == 2:
                        print("Else  Set: ({},{})". format(y, x))
                else:
                    print("Else  Right 1 move_to")
                    new_plot = compare_plots(plot_c, 1, template, "2")
                    print_plot(new_plot)
                    anw, yx = check_for_number(new_plot, "1")  # check if any uncompleted parts left

                    if anw:  # if true
                        yx, ind_list = move_to(plot_c, yx, ind_list[-1], 4, 1, ind_list)  # run move_to
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
                print_plot(new_plot)
                anw, yx = check_for_number(new_plot, "1")  # check if any uncompleted parts left

                if anw:
                    yx, ind_list = move_to(plot_c, yx, ind_list[-1], 4, 1, ind_list)
                    y, x = yx
                    direct = 1
                else:
                    ext = 1  # if false, all areas have been visited, exit while loop

            # if position 3
            elif y - 1 >= 0 and plot_c[c, b] == 1:
                print(template[y, b])
                if template[c, b] == "1":   # hit already completed section
                    new_plot = compare_plots(plot_c, 1, template, "2")
                    print_plot(new_plot)
                    anw, yx = check_for_number(new_plot, "1")  # check if any uncompleted parts left

                    if anw:     # if true
                        yx, ind_list = move_to(plot_c, yx, ind_list[-1], 4, 1, ind_list)  # run move_to
                        y, x = yx
                        direct = 1
                    else:
                        ext = 1  # if false, all areas have been visited, exit while loop

                else:
                    y = c
                    x = b
                    ind_list.append((y, x))
                    if test == 2:
                        print("Pos 3 Set: ({},{})".format(y, x))

                    j = 0
                    while j != 1:   # to the end of the line

                        if x + 1 < len(template[0]) and template[y, x + 1] == "1":
                            break
                        elif y - 1 >= 0 and plot_c[y - 1, x] != 0:
                            y = y - 1
                            ind_list.append((y, x))
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
                    print_plot(new_plot)
                    anw, yx = check_for_number(new_plot, "1")  # check if any uncompleted parts left

                    if anw:  # if true
                        yx, ind_list = move_to(plot_c, yx, ind_list[-1], 4, 1, ind_list)  # run move_to
                        y, x = yx
                        direct = 1
                    else:
                        ext = 1  # if false, all areas have been visited, exit while loop

                else:
                    x = b
                    ind_list.append((y, x))

                    if test == 2:
                        print("Pos 4 Set: ({},{})".format(y, x))

                    if y - 1 < 0 and template[y, x] == "0":
                        pass
                    elif y - 1 < 0 and template[y, x] == "2":
                        direct = 1
                    elif plot_c[c, x] == 0 and template[y, x] == "2":
                        direct = 1
                    elif template[y, x] == "2":
                        print("error 2 right position 4")
                    elif template[y, x] == "0":
                        pass
                    # look at the nest 2's column

            # if position 5
            elif y + 1 < len(plot_c) and plot_c[a, b] == 1:

                if template[y, b] == "1":  # hit already completed section

                    new_plot = compare_plots(plot_c, 1, template, "2")
                    print_plot(new_plot)
                    anw, yx = check_for_number(new_plot, "1")  # check if any uncompleted parts left

                    if anw:  # if true
                        yx, ind_list = move_to(plot_c, yx, ind_list[-1], 4, 1, ind_list)  # run move_to
                        y, x = yx
                        direct = 1
                    else:
                        ext = 1  # if false, all areas have been visited, exit while loop

                else:
                    y = a
                    x = b
                    ind_list.append((y, x))
                    if test == 2:
                        print("Pos 5  Set: ({},{})".format(y, x))

                    if y + 1 >= len(plot_c):
                        direct = 1
                    elif plot_c[y - 1, x] == 0 and template[y, x] == "2":
                        direct = 1
                    elif template[y, x] == "2":
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
                    if test == 2:
                        print("Else  Set: ({},{})".format(y, x))
                else:
                    print("Else  Right 2 move_to")
                    new_plot = compare_plots(plot_c, 1, template, "2")
                    print_plot(new_plot)
                    anw, yx = check_for_number(new_plot, "1")  # check if any uncompleted parts left

                    if anw:  # if true
                        yx, ind_list = move_to(plot_c, yx, ind_list[-1], 4, 1, ind_list)  # run move_to
                        y, x = yx
                        direct = 1
                    else:
                        ext = 1  # if false, all areas have been visited, exit while loop

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

    s2_yx, ind_list = move_to(plot_c, s2_yx, ind_list[-1], 4, 1, ind_list)
    y, x = s2_yx
    direct = 1
    ext = 0
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
                    yx, ind_list = move_to(plot_no_change, yx, ind_list[-1], 4, 1, ind_list)
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
                if test == 2:
                    print("Pos 5 Set: ({},{})". format(y, x))

                j = 0
                while j != 1:  # to the end of the line

                    if x + 1 < len(plot_c[0]) and plot_c[y, x + 1] != 0:
                        x = x + 1
                        ind_list.append((y, x))
                        plot_c[y, x] = 2
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
                if test == 2:
                    print("Pos 7 Set: ({},{})". format(y, x))

                direct = 3

            else:

                if x - 1 >= 0 and plot_c[y, d] == 2:
                    x = x - 1
                    ind_list.append((y, x))
                    plot_c[y, x] = 2
                    if test == 2:
                        print("Else Set: ({},{})".format(y, x))

                else:
                    anw, yx = check_for_number(plot_c, 1)

                    if anw:
                        y, x = yx
                        plot_c[y, x] = 2
                        yx, ind_list = move_to(plot_no_change, yx, ind_list[-1], 4, 1, ind_list)
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
                    yx, ind_list = move_to(plot_no_change, yx, ind_list[-1], 4, 1, ind_list)
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
                if test == 2:
                    print("Pos 7 Set: ({},{})". format(y, x))

                j = 0
                while j != 1:  # to the end of the line

                    if plot_c[y, x - 1] != 0:
                        x = x - 1
                        ind_list.append((y, x))
                        plot_c[y, x] = 2
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
                if test == 2:
                    print("Pos 5 Set: ({},{})". format(y, x))

                if plot_c[y, x - 1] == 0 or x - 1 < min_x:
                    direct = 1

            else:

                if x + 1 < len(plot_c[0]) and plot_c[y, b] == 2:
                    x = x + 1
                    ind_list.append((y, x))
                    plot_c[y, x] = 2
                    if test == 2:
                        print("Else Set: ({},{})".format(y, x))
                else:
                    anw, yx = check_for_number(plot_c, 1)

                    if anw:
                        y, x = yx
                        plot_c[y, x] = 2
                        yx, ind_list = move_to(plot_no_change, yx, ind_list[-1], 4, 1, ind_list)
                        y, x = yx
                        direct = 1
                    else:
                        ext = 1  # if false, all areas have been visited, exit while loop

    return ind_list


def compare_plots(plot1, val1, plot2, val2):

    p_row = ["0"] * len(plot1[0])  # create blank plot make template plot
    blank_plot = np.array([p_row] * len(plot1))

    for y, row in enumerate(plot1):
        for x, point in enumerate(row):
            if point == val1 and plot2[y, x] == val2:
                blank_plot[y, x] = "1"

    return blank_plot


def move_to(main_plot, goto_yx, start_yx, set_to, look_for, passed_ind_list):
    test = 0
    col_num = look_for  # value 1
    ref_plot = main_plot.copy()
    plot = main_plot.copy()    # untouched plot with just 0's and 1's
    plot_9 = main_plot.copy()
    f_y, f_x = goto_yx
    y, x = start_yx
    og_ind_list = passed_ind_list
    ind_list = []

    print("Move_to \n", og_ind_list)

    one = [1, 8, 2, 7, 3, 6, 4, 5]
    two = [2, 1, 3, 8, 4, 7, 5, 6]
    thr = [3, 2, 4, 1, 5, 8, 6, 7]
    fou = [4, 3, 5, 2, 6, 1, 7, 8]
    fiv = [5, 4, 6, 3, 7, 2, 8, 1]
    six = [6, 5, 7, 4, 8, 3, 1, 2]
    sev = [7, 6, 8, 5, 1, 4, 2, 3]
    eig = [8, 7, 1, 6, 2, 5, 3, 4]
    search_patterns = [one, two, thr, fou, fiv, six, sev, eig]

    ext = 0
    ind = 0
    loop_c = 0

    point_c = next_point(start_yx, goto_yx)
    s_pat = search_patterns[point_c - 1]

    if test == 2:
        print("GoTo: {} Start: {}".format(goto_yx, start_yx))

    bol = isinstance(ref_plot[0, 0], str)

    if bol:
        set_to = str(set_to)

    if start_yx == goto_yx:
        return goto_yx, ind_list

    # ** many already have been set in previous function/method
    plot[y, x] = set_to  # setting start point
    ind_list.append((y, x))  # setting start point in list already in list from previous
    while ext != 1:

        for i in range(1):
            row_num = len(plot)
            cul_num = len(plot[0])
            points = []
            a = y - 1
            b = y + 1
            c = x - 1
            d = x + 1
            if test == 3:
                print("Centre: ({},{})".format(y, x))

            # Position 2
            if y > 0:
                if plot[a, x] == 9:
                    y -= 1  # set y to y - 1

                    if test == 1 or test == 2:  # testing console comments
                        print("P2 9 Set ({},{})".format(y, x))

                    plot[y, x] = set_to  # set point
                    ind_list.append((y, x))  # add point to list
                    cur_yx = (y, x)  # combine current y, x
                    point_c = next_point(cur_yx, goto_yx)  # get next position to check
                    s_pat = search_patterns[point_c - 1]  # change to new search pattern
                    ind = 0
                    break

            # Position 1
                if x > 0:
                    if plot[a, c] == 9:
                        y -= 1  # set y to y - 1
                        x -= 1  # set x to x - 1

                        if test == 1 or test == 2:  # testing console comments
                            print("P1 9 Set ({},{})".format(y, x))

                        ind_list.append((y, x))  # add point to list
                        cur_yx = (y, x)  # combine current y, x
                        point_c = next_point(cur_yx, goto_yx)  # get next position to check
                        s_pat = search_patterns[point_c - 1]  # change to new search pattern
                        ind = 0
                        break

            # Position 3
                if x < cul_num - 1:
                    if plot[a, d] == 9:
                        y -= 1  # set y to y - 1
                        x += 1  # set x to x - 1

                        if test == 1 or test == 2:  # testing console comments
                            print("P3 9 Set ({},{})".format(y, x))

                        ind_list.append((y, x))  # add point to list
                        cur_yx = (y, x)  # combine current y, x
                        point_c = next_point(cur_yx, goto_yx)  # get next position to check
                        s_pat = search_patterns[point_c - 1]  # change to new search pattern
                        ind = 0
                        break

            # Position 6
            if y < row_num - 1:
                if plot[b, x] == 9:
                    y += 1  # set y to y - 1

                    if test == 1 or test == 2:  # testing console comments
                        print("P6 9 Set ({},{})".format(y, x))

                    plot[y, x] = set_to  # set point
                    ind_list.append((y, x))  # add point to list
                    cur_yx = (y, x)  # combine current y, x
                    point_c = next_point(cur_yx, goto_yx)  # get next position to check
                    s_pat = search_patterns[point_c - 1]  # change to new search pattern
                    ind = 0
                    break

            # Position 7
                if x > 0:
                    if plot[b, c] == 9:
                        y += 1  # set y to y + 1
                        x -= 1  # set x to x - 1

                        if test == 1 or test == 2:  # testing console comments
                            print("P7 9 Set ({},{})".format(y, x))

                        plot[y, x] = set_to  # set point
                        ind_list.append((y, x))  # add point to list
                        cur_yx = (y, x)  # combine current y, x
                        point_c = next_point(cur_yx, goto_yx)  # get next position to check
                        print(point_c)
                        s_pat = search_patterns[point_c - 1]  # change to new search pattern
                        ind = 0
                        break
            # Position 5
                if x < cul_num - 1:
                    if plot[b, d] == 9:

                        y += 1  # set y to y + 1
                        x += 1  # set x to x + 1

                        if test == 1 or test == 2:  # testing console comments
                            print("P5 9 Set ({},{})".format(y, x))

                        plot[y, x] = set_to  # set point
                        ind_list.append((y, x))  # add point to list
                        cur_yx = (y, x)  # combine current y, x
                        point_c = next_point(cur_yx, goto_yx)  # get next position to check
                        s_pat = search_patterns[point_c - 1]  # change to new search pattern
                        ind = 0
                        break

            # Position 8
            if x > 0:
                if plot[y, c] == 9:
                    x -= 1  # set x to x - 1

                    if test == 1 or test == 2:  # testing console comments
                        print("P8 9 Set ({},{})".format(y, x))

                    plot[y, x] = set_to  # set point
                    ind_list.append((y, x))  # add point to list
                    cur_yx = (y, x)  # combine current y, x
                    point_c = next_point(cur_yx, goto_yx)  # get next position to check
                    s_pat = search_patterns[point_c - 1]  # change to new search pattern
                    print(point_c-1, "\n", s_pat)
                    ind = 0
                    break

            # Position 4
            if x < cul_num - 1:
                if plot[y, d] == 9:

                    x += 1  # set x to x + 1

                    if test == 1 or test == 2:  # testing console comments
                        print("P4 9 Set ({},{})".format(y, x))

                    plot[y, x] = set_to  # set point
                    ind_list.append((y, x))  # add point to list
                    cur_yx = (y, x)  # combine current y, x
                    point_c = next_point(cur_yx, goto_yx)  # get next position to check
                    s_pat = search_patterns[point_c - 1]  # change to new search pattern
                    ind = 0
                    break

        l_point = s_pat[ind]
        loop = 0

        # One
        if l_point == 1:  # check loop start

            if test == 1:  # testing console comments
                print("# One")

            if y - 1 >= 0 and x - 1 >= 0:  # check if next point is within the plot limits
                n_point = plot[y - 1, x - 1]  # set next point

                if n_point == col_num:  # check against colour_number
                    pon_a = plot[y, x - 1]
                    pon_b = plot[y - 1, x]

                    if pon_a == pon_b and pon_a == set_to:

                        plot_9[y - 1, x - 1] = 9
                        plot = plot_9
                        y, x = start_yx
                        ind_list.clear()

                        # ind_list, yx = back_track(ind_list, plot)  # back_track until a new valid space is found
                        # y, x = yx
                        if test == 2:
                            print("You just crossed a line buddy")
                            print("Restart\nGoTo: {} Start: {}".format(goto_yx, start_yx))

                        point_c = next_point(start_yx, goto_yx)  # get next position to check
                        s_pat = search_patterns[point_c - 1]  # change to new search pattern

                    else:
                        if y - 1 == f_y and x - 1 == f_x:   # check if next point is destination
                            ind_list.append((y - 1, x - 1))

                            del ind_list[0]
                            for i in ind_list:
                                og_ind_list.append(i)

                            if test == 2:
                                print("Move_to Ind: \n", ind_list)
                                print("Move_to End: \n", og_ind_list)
                            return goto_yx, og_ind_list  # if true then break loop and return goto_yx and ind_list

                        else:   # else record valid point
                            y -= 1  # set y to y - 1
                            x -= 1  # set x to x - 1

                            if test == 1 or test == 2:  # testing console comments
                                print("Set ({},{})".format(y, x))

                            plot[y, x] = set_to     # set point
                            ind_list.append((y, x))  # add point to list
                            cur_yx = (y, x)  # combine current y, x
                            point_c = next_point(cur_yx, goto_yx)  # get next position to check
                            s_pat = search_patterns[point_c - 1]  # change to new search pattern
                            ind = 0     # reset search pattern start
                            loop = 1    # set check value

            if loop != 1:  # check if new current point was set
                if ind >= 7:
                    ind = 0
                    loop_c += 1
                else:
                    ind += 1  # if not, set to the next position

        # Two
        elif l_point == 2:  # check loop start

            if test == 1:  # testing console comments
                print("# Two")

            if y - 1 >= 0:  # check if this point is within the plot limits
                n_point = plot[y - 1, x]  # set this point

                if n_point == col_num:  # check against colour_number

                    if y - 1 == f_y and x == f_x:  # check if next point is destination
                        ind_list.append((y - 1, x))

                        del ind_list[0]
                        for i in ind_list:
                            og_ind_list.append(i)

                        if test == 2:
                            print("Move_to Ind: \n", ind_list)
                            print("Move_to End: \n", og_ind_list)
                        return goto_yx, og_ind_list  # if true then break loop and return goto_yx and ind_list

                    else:  # else record valid point

                        y -= 1  # set y to y - 1

                        if test == 1 or test == 2:  # testing console comments
                            print("Set ({},{})".format(y, x))

                        plot[y, x] = set_to     # set point
                        ind_list.append((y, x))  # add point to list
                        cur_yx = (y, x)  # combine current y, x
                        point_c = next_point(cur_yx, goto_yx)  # get next position to check
                        s_pat = search_patterns[point_c - 1]  # change to new search pattern
                        ind = 0  # reset search pattern start
                        loop = 1  # set check value

            if loop != 1:  # check if new current point was set
                if ind >= 7:
                    ind = 0
                    loop_c += 1
                else:
                    ind += 1  # if not, set to the next position

        # Three
        elif l_point == 3:  # check if this point is within the plot limits

            if test == 1:  # set this point
                print("# Three")

            if y - 1 >= 0 and x + 1 < len(plot[0]):  # check if this point is within the plot limits
                n_point = plot[y - 1, x + 1]  # set this point

                if n_point == col_num:  # check against colour_number
                    pon_a = plot[y, x + 1]
                    pon_b = plot[y - 1, x]

                    if pon_a == pon_b and pon_a == set_to:

                        plot_9[y - 1, x + 1] = 9
                        plot = plot_9
                        y, x = start_yx
                        ind_list.clear()

                        # ind_list, yx = back_track(ind_list, plot)  # back_track until a new valid space is found
                        # y, x = yx
                        if test == 2:
                            print("You just crossed a line buddy")
                            print("Restart\nGoTo: {} Start: {}".format(goto_yx, start_yx))
                        point_c = next_point(start_yx, goto_yx)  # get next position to check
                        s_pat = search_patterns[point_c - 1]  # change to new search pattern

                    else:
                        if y - 1 == f_y and x + 1 == f_x:  # check if next point is destination
                            ind_list.append((y - 1, x + 1))

                            del ind_list[0]
                            for i in ind_list:
                                og_ind_list.append(i)

                            if test == 2:
                                print("Move_to Ind: \n", ind_list)
                                print("Move_to End: \n", og_ind_list)
                            return goto_yx, og_ind_list  # if true then break loop and return goto_yx and ind_list

                        else:  # else record valid point
                            y -= 1  # set y to y - 1
                            x += 1  # set x to x + 1

                            if test == 1 or test == 2:  # testing console comments
                                print("Set ({},{})".format(y, x))

                            plot[y, x] = set_to  # set point
                            ind_list.append((y, x))  # add point to list
                            cur_yx = (y, x)  # combine current y, x
                            point_c = next_point(cur_yx, goto_yx)  # get next position to check
                            s_pat = search_patterns[point_c - 1]  # change to new search pattern
                            ind = 0  # reset search pattern start
                            loop = 1  # set check value

            if loop != 1:  # check if new current point was set
                if ind >= 7:
                    ind = 0
                    loop_c += 1
                else:
                    ind += 1  # if not, set to the next position

        # Four
        elif l_point == 4:  # check loop start

            if test == 1:  # testing console comments
                print("# Four")

            if x + 1 < len(plot[0]):  # check if this point is within the plot limits
                n_point = plot[y, x + 1]  # set this point

                if n_point == col_num:  # check against colour_number

                    if y == f_y and x + 1 == f_x:  # check if next point is destination

                        ind_list.append((y, x + 1))

                        del ind_list[0]
                        for i in ind_list:
                            og_ind_list.append(i)

                        if test == 2:
                            print("Move_to Ind: \n", ind_list)
                            print("Move_to End: \n", og_ind_list)
                        return goto_yx, og_ind_list  # if true then break loop and return goto_yx and ind_list

                    else:  # else record valid point

                        x += 1  # set x to x + 1

                        if test == 1 or test == 2:  # testing console comments
                            print("Set ({},{})".format(y, x))

                        plot[y, x] = set_to  # set point
                        ind_list.append((y, x))  # add point to list
                        cur_yx = (y, x)  # combine current y, x

                        point_c = next_point(cur_yx, goto_yx)  # get next position to check
                        s_pat = search_patterns[point_c - 1]  # change to new search pattern
                        ind = 0  # reset search pattern start
                        loop = 1  # set check value

            if loop != 1:  # check if new current point was set
                if ind >= 7:
                    ind = 0
                    loop_c += 1
                else:
                    ind += 1  # if not, set to the next position

        # Five
        elif l_point == 5:  # check loop start

            if test == 1:  # testing console comments
                print("# Five")

            if y + 1 < len(plot) and x + 1 < len(plot[0]):  # check if this point is within the plot limits
                n_point = plot[y + 1, x + 1]  # set this point

                if n_point == col_num:  # check against colour_number
                    pon_a = plot[y, x + 1]
                    pon_b = plot[y + 1, x]

                    if pon_a == pon_b and pon_a == set_to:

                        plot_9[y + 1, x + 1] = 9
                        plot = plot_9
                        y, x = start_yx
                        ind_list.clear()

                        # ind_list, yx = back_track(ind_list, plot)  # back_track until a new valid space is found
                        # y, x = yx
                        if test == 2:
                            print("You just crossed a line buddy")
                            print("Restart\nGoTo: {} Start: {}".format(goto_yx, start_yx))
                        point_c = next_point(start_yx, goto_yx)  # get next position to check
                        s_pat = search_patterns[point_c - 1]  # change to new search pattern

                    else:
                        if y + 1 == f_y and x + 1 == f_x:  # check if next point is destination

                            ind_list.append((y + 1, x + 1))

                            del ind_list[0]
                            for i in ind_list:
                                og_ind_list.append(i)

                            if test == 2:
                                print("Move_to Ind: \n", ind_list)
                                print("Move_to End: \n", og_ind_list)
                            return goto_yx, og_ind_list  # if true then break loop and return goto_yx and ind_list

                        else:  # else record valid point

                            y += 1  # set y to y + 1
                            x += 1  # set x to x + 1

                            if test == 1 or test == 2:  # testing console comments
                                print("Set ({},{})".format(y, x))

                            plot[y, x] = set_to  # set point
                            ind_list.append((y, x))  # add point to list
                            cur_yx = (y, x)  # combine current y, x

                            point_c = next_point(cur_yx, goto_yx)  # get next position to check
                            s_pat = search_patterns[point_c - 1]  # change to new search pattern
                            ind = 0  # reset search pattern start
                            loop = 1  # set check value

            if loop != 1:  # check if new current point was set
                if ind >= 7:
                    ind = 0
                    loop_c += 1
                else:
                    ind += 1  # if not, set to the next position

        # Six
        elif l_point == 6:  # check loop start

            if test == 1:  # testing console comments
                print("# Six")

            if y + 1 < len(plot):  # check if this point is within the plot limits
                n_point = plot[y + 1, x]  # set this point

                if n_point == col_num:  # check against colour_number

                    if y + 1 == f_y and x == f_x:  # check if next point is destination
                        ind_list.append((y + 1, x))

                        del ind_list[0]
                        for i in ind_list:
                            og_ind_list.append(i)

                        if test == 2:
                            print("Move_to Ind: \n", ind_list)
                            print("Move_to End: \n", og_ind_list)
                        return goto_yx, og_ind_list  # if true then break loop and return goto_yx and ind_list

                    else:  # else record valid point

                        y += 1  # set y to y + 1

                        if test == 1 or test == 2:  # testing console comments
                            print("Set ({},{})".format(y, x))

                        plot[y, x] = set_to  # set point
                        ind_list.append((y, x))  # add point to list
                        cur_yx = (y, x)  # combine current y, x
                        point_c = next_point(cur_yx, goto_yx)  # get next position to check
                        s_pat = search_patterns[point_c - 1]  # change to new search pattern
                        ind = 0  # reset search pattern start
                        loop = 1  # set check value

            if loop != 1:  # check if new current point was set
                if ind >= 7:
                    ind = 0
                    loop_c += 1
                else:
                    ind += 1  # if not, set to the next position

        # Seven
        elif l_point == 7:  # check loop start

            if test == 1:  # testing console comments
                print("# Seven")

            if y + 1 < len(plot) and x - 1 >= 0:  # check if this point is within the plot limits
                n_point = plot[y + 1, x - 1]  # set this point

                if n_point == col_num:  # check against colour_number
                    pon_a = plot[y, x - 1]
                    pon_b = plot[y + 1, x]

                    if pon_a == pon_b and pon_a == set_to:

                        plot_9[y + 1, x - 1] = 9
                        plot = plot_9
                        y, x = start_yx
                        ind_list.clear()

                        if test == 2:
                            print("You just crossed a line buddy")
                            print("Restart\nGoTo: {} Start: {}".format(goto_yx, start_yx))
                        # ind_list, yx = back_track(ind_list, plot)  # back_track until a new valid space is found
                        # y, x = yx

                        point_c = next_point(start_yx, goto_yx)  # get next position to check
                        s_pat = search_patterns[point_c - 1]  # change to new search pattern

                    else:
                        if y + 1 == f_y and x - 1 == f_x:  # check if next point is destination

                            ind_list.append((y + 1, x - 1))

                            del ind_list[0]
                            for i in ind_list:
                                og_ind_list.append(i)

                            if test == 2:
                                print("Move_to Ind: \n", ind_list)
                                print("Move_to End: \n", og_ind_list)
                            return goto_yx, og_ind_list  # if true then break loop and return goto_yx and ind_list

                        else:  # else record valid point

                            y += 1  # set y to y + 1
                            x -= 1  # set x to x - 1

                            if test == 1 or test == 2:  # testing console comments
                                print("Set ({},{})".format(y, x))

                            plot[y, x] = set_to  # set point
                            ind_list.append((y, x))  # add point to list
                            cur_yx = (y, x)  # combine current y, x

                            point_c = next_point(cur_yx, goto_yx)  # get next position to check
                            s_pat = search_patterns[point_c - 1]  # change to new search pattern
                            ind = 0  # reset search pattern start
                            loop = 1  # set check value

            if loop != 1:  # check if new current point was set
                if ind >= 7:
                    ind = 0
                    loop_c += 1
                else:
                    ind += 1  # if not, set to the next position

        # Eight
        elif l_point == 8:  # check loop start

            if test == 1:  # testing console comments
                print("# Eight")

            if x - 1 >= 0:  # check if this point is within the plot limits
                n_point = plot[y, x - 1]  # set this point

                if n_point == col_num:  # check against colour_number

                    if y == f_y and x - 1 == f_x:  # check if next point is destination
                        ind_list.append((y, x - 1))

                        del ind_list[0]
                        for i in ind_list:
                            og_ind_list.append(i)

                        if test == 2:
                            print("Move_to Ind: \n", ind_list)
                            print("Move_to End: \n", og_ind_list)
                        return goto_yx, og_ind_list  # if true then break loop and return goto_yx and ind_list

                    else:  # else record valid point

                        x -= 1  # set x to x - 1

                        if test == 1 or test == 2:  # testing console comments
                            print("Set ({},{})".format(y, x))

                        plot[y, x] = set_to  # set point
                        ind_list.append((y, x))  # add point to list
                        cur_yx = (y, x)  # combine current y, x
                        point_c = next_point(cur_yx, goto_yx)  # get next position to check
                        s_pat = search_patterns[point_c - 1]  # change to new search pattern
                        ind = 0  # reset search pattern start
                        loop = 1  # set check value

            if loop != 1:  # check if new current point was set
                if ind >= 7:
                    ind = 0
                    loop_c += 1
                else:
                    ind += 1  # if not, set to the next position

        if loop_c > 1:  # if loop_count is more then 1 move_to is trapped

            if test == 2:   # testing console comments

                print("Move_to trapped\nRun back_track")

            ind_list, yx = back_track(ind_list, plot)   # back_track until a new valid space is found
            y, x = yx

            point_c = next_point(yx, goto_yx)  # get next position to check
            s_pat = search_patterns[point_c - 1]  # change to new search pattern

            loop_c = 0

    del ind_list[0]
    for i in ind_list:
        og_ind_list.append(i)

    print("Move_to Ind: \n", ind_list)
    print("Move_to End: \n", og_ind_list)
    return goto_yx, og_ind_list


def back_track(ind_list, plot):
    length = len(ind_list)
    # if len(ind_list)-1 <= 0:
    #     pass
    # else:
    del ind_list[-1]

    for i in range(length):
        p_y, p_x = ind_list[-1]

        points = get_surrounding_points(plot, plot, p_y, p_x, 1)

        if 1 in points:

            return ind_list, (p_y, p_x)

        else:
            del ind_list[-1]


def next_point(yx_st, yx_fn):
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
        flip = 0
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
                                # print("points List: {}".format(points))
                                if test >= 1:
                                    print("Fill Set({},{})".format(y, x))
                                ref_plot[y, x] = set_to
                                change = 1

        while l_len >= 0:

            x = r_len
            while x >= 0:
                y = l_len

                # print("l_len: {} r_len: {}".format(l_len, x))
                if min_x <= x <= max_x and min_y <= y <= max_y:
                    if plot[y, x] == copy_col_num:

                        if ref_plot[y, x] == col_num:
                            points = get_surrounding_points(plot, ref_plot, y, x, copy_col_num)

                            if set_to not in points:
                                pass
                            else:
                                # print("points List: {}".format(points))
                                if test >= 1:
                                    print("Re Fill ({},{})".format(y, x))
                                ref_plot[y, x] = set_to
                                change = 1

                x -= 1
            l_len -= 1


def check_for_number(plot, num):
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


# not used?
def get_ob_inlines(main_plot, ref_plot):

    # plot_h = len(ref_plot)
    plot_w = len(main_plot[0])
    bol = True
    # check for 2
    b_val = 0
    for y, row in enumerate(main_plot):
        for x, point in enumerate(row):
            if point == "2":
                ref_plot[y, x] = "2"
    print("ref_plot")
    print_plot(ref_plot)
    while bol:

        for y, row in enumerate(ref_plot):
            for x, point in enumerate(row):
                if x + 1 < plot_w - 1:
                    if row[x + 1] == "2":
                        b_val = 1
                        # set inline
                        start_yx = (y, x)
                        max_yx, min_yx, ind_list = get_object_outline(main_plot, ref_plot, start_yx, 4, "3", "1")

                        # set used inside
                        start_yx = (y, x + 1)
                        max_yx, min_yx, ind_list = get_object_outline(main_plot, ref_plot, start_yx, 8, "4", "2")
                        print("")
                        reversible_mine_sweeper_fill(main_plot, ref_plot, max_yx, min_yx, "4", "2", 3)
                        print_plot(ref_plot)

        bol, yx = check_for_number(ref_plot, 2)
    return ref_plot


def print_plot(plot):

    bol = isinstance(plot[0, 0], str)

    if bol:
        pass

    for y, row in enumerate(plot):
        p_row = ""
        for x, point in enumerate(row):

            if bol:
                if point == "0":
                    p_row = p_row + ". "
                else:
                    p_row = p_row + point + " "
            else:
                if point == 0:
                    p_row = p_row + ". "
                else:
                    p_row = p_row + str(point) + " "

        print(p_row)


def print_plot_advanced(plot):

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


def get_surrounding_points(plot, out_plot, y, x, col_num):
    test = 0
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


def valid_position(main_plot, y, x, col_num, con_col):
    test = 0

    if test >= 1:
        print("Valid position check: ({},{})".format(y, x))
        print("col_num Value: {}".format(col_num))

    points, yx_points = get_surrounding_points_5x5(main_plot, y, x)
    val_list, amount_list = count_list(points)
    anw = t_w_p_logic(col_num, con_col, val_list, amount_list)

    return anw


def get_surrounding_points_5x5(main_plot, y, x):
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
    val_list = []
    amount_list = []

    for x, pon in enumerate(points):
        # print("(Y,X): ", y, ",", x)

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
            # print("col_con is the line")
            return 2
        else:
            # print("Both are equal")
            return 3
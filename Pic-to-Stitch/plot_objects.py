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
        self.ob_fill = []
        self.colour = colour
        self.ref_plot = self.create_ref_plot(2)
        self.ob_parts_list = []
        self.section_image = int()

    def process_colour_plot(self, main_plot):
        test = 1
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

            if point == col_letter_list[0]:

                max_yx, min_yx, ind_list = get_object_outline(main_plot, ref_plot, (y, x), l_p, val, col_num)
                print_plot(ref_plot)
                print("")
                reversible_mine_sweeper_fill(main_plot, ref_plot, max_yx, min_yx, val, col_num, 2)
                print_plot(ref_plot)

        for y, row in enumerate(ref_plot):
            for x, point in enumerate(row):

                if point == col_letter_list[1]:

                    max_yx, min_yx, ind_list = get_object_outline(main_plot, ref_plot, (y, x), 8, "1", 2)
                    print_plot_advanced(ref_plot)
                    print("")
                    reversible_mine_sweeper_fill(main_plot, ref_plot, max_yx, min_yx, "1", 2, 1)
                    print_plot_advanced(ref_plot)

        for y, row in enumerate(ref_plot):
            for x, point in enumerate(row):

                if point == col_letter_list[0]:

                    max_yx, min_yx, ind_list = get_object_outline(ref_plot, ref_plot, (y, x), 8, "2", "b")
                    print_plot_advanced(ref_plot)
                    print("")
                    reversible_mine_sweeper_fill(ref_plot, ref_plot, max_yx, min_yx, "2", "b", 2)
                    print_plot_advanced(ref_plot)

    # def stitch_choice(self, ref_plot, image):
    #
    #     for y, row in enumerate(ref_plot):
    #         for x, point in enumerate(row):
    #             if point == "0":
    #
    #                 if x + 1 < len(ref_plot):
    #                     if ref_plot[y, x + 1] == "1":
    #                         # highlight colour
    #                         pass
    #
    #                 if x + 2 < len(ref_plot):
    #                     if ref_plot[y, x + 2] == "1":
    #                         pass
    #
    #                 if x + 3 < len(ref_plot):
    #                     if ref_plot[y, x + 3] == "1":
    #                         pass
    #
    #                 # greyscale
    #                 pass
    #
    #             elif point == "1":
    #                 pass

    def create_detail_sub_plot(self, main_plot):
        test = 1
        ref_plot = self.ref_plot.copy()
        p_row = ["0"] * len(ref_plot[0])
        blank_plot = np.array([p_row] * len(ref_plot))
        plot = blank_plot.copy()
        b_val = 0

        for y, row in enumerate(self.ref_plot):
            for x, point in enumerate(row):
                if point == "1":
                    out = get_object_outline(ref_plot, plot, (y, x), 8, "1", "1")
                    ind_list = out[2]
                    self.ob_outline = ind_list  # Outline coor list
                    b_val = 1
                    break
            if b_val == 1:
                break

        self.ob_parts_list.append(plot)  # Outline Plot
        print_plot_advanced(self.matrix)
        print_plot_advanced(self.ref_plot)
        if test == 1:
            print_plot(plot)

        plot = blank_plot.copy()

        out_plot = get_ob_inlines(ref_plot, plot)
        for y, row in enumerate(plot):
            for x, point in enumerate(row):
                if point == "4":
                    plot[y, x] = "0"
                elif point == "3":
                    plot[y, x] = "1"
        print("Inline")
        print_plot(plot)
        self.ob_parts_list.append(out_plot)             # Inline

        out_plot = self.get_ob_lines()

        self.ob_parts_list.append(out_plot)

        self.ob_parts_list.append(self.matrix)    # full fill

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

    def print_ob_part_list(self):
        if not self.ob_parts_list:
            print("Not Matrix' in list")
        else:
            for i, item in enumerate(self.ob_parts_list):

                print("Item {}".format(i+1))
                print_plot(item)


class StitchObjects:

    def __init__(self, passed_colour, passed_object_id, height, width, stitch_list):
        self.stitch_list = stitch_list
        self.colour = passed_colour
        self.stitch_type = str()
        self.object_outline = []
        self.stitch_count = int()
        self.obj_width = float()
        self.obj_height = float()
        self.max_yx = 0
        self.min_yx = 0
        self.object_id = passed_object_id
        row = [0] * width
        self.plot = np.array([row] * height)


def get_object_outline(main_plot, ref_plot, start_yx, start_point, set_to, col_num):
    test = 1

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

    # if out_plot == 0:
    #     p_row = [0] * self.matrix_width
    #     out_plot = np.array([p_row] * self.matrix_height)

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
                        points, yx_points = get_surrounding_points_5x5_vary(plot, y - 1, x - 1)
                        val_list, amount_list = count_list(points)
                        anw = t_w_p_logic(col_num, pon_a, val_list, amount_list)

                        if anw == 1:
                            y -= 1
                            x -= 1
                            if test == 1:
                                print("Set ({},{})".format(y, x))
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
                            if test == 1:
                                print("Set ({},{})".format(y, x))
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
                        if test == 1:
                            print("Set ({},{})".format(y, x))
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
                        points, yx_points = get_surrounding_points_5x5_vary(plot, y - 1, x + 1)
                        val_list, amount_list = count_list(points)
                        anw = t_w_p_logic(col_num, pon_a, val_list, amount_list)

                        if anw == 1:
                            y -= 1
                            x += 1
                            if test == 1:
                                print("Set ({},{})".format(y, x))
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
                            if test == 1:
                                print("Set ({},{})".format(y, x))
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
                        if test == 1:
                            print("Set ({},{})".format(y, x))
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
                        points, yx_points = get_surrounding_points_5x5_vary(plot, y + 1, x + 1)
                        val_list, amount_list = count_list(points)
                        anw = t_w_p_logic(col_num, pon_a, val_list, amount_list)

                        if anw == 1:
                            y += 1
                            x += 1
                            if test == 1:
                                print("Set ({},{})".format(y, x))
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
                            if test == 1:
                                print("Set ({},{})".format(y, x))
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

                        if test == 1:
                            print("Set ({},{})".format(y, x))
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
                        points, yx_points = get_surrounding_points_5x5_vary(plot, y + 1, x - 1)
                        val_list, amount_list = count_list(points)
                        anw = t_w_p_logic(col_num, pon_a, val_list, amount_list)

                        if anw == 1:
                            y += 1
                            x -= 1
                            if test == 1:
                                print("Set ({},{})".format(y, x))
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
                            if test == 1:
                                print("Set ({},{})".format(y, x))
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
                # print("n_point: {}, col_num: {}".format(n_point,col_num))
                if n_point == col_num:

                    if (y, x - 1) == ind_list[0]:
                        break
                    else:
                        comp = True
                        # print("x-1")
                        # check outline_list
                        x -= 1
                        if test == 1:
                            print("Set ({},{})".format(y, x))
                        ref_plot[y, x] = set_to
                        ind_list.append((y, x))
                        l_point = 4

            if l_point != 4:
                l_point = 8
    print_plot(ref_plot)
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


# NOT USED
def mine_sweeper_fill(main_plot, ref_plot, max_yx, min_yx, count, col_num):
    plot = main_plot
    min_y, min_x = min_yx
    max_y, max_x = max_yx

    bol = isinstance(ref_plot[0, 0], str)

    if bol:
        col_num = "a"
        count = str(count)

    for y, row in enumerate(ref_plot):
        for x, point in enumerate(ref_plot[0]):
            if min_x <= x <= max_x and min_y <= y <= max_y:
                if ref_plot[y, x] == col_num:
                    points = get_surrounding_points(plot, ref_plot, y, x, col_num)

                    if count not in points:
                        pass
                    else:
                        print("({},{})".format(y,x))
                        ref_plot[y, x] = count


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

    bol = isinstance(plot[0, 0], str)
    bol2 = isinstance(num, str)
    if bol and not bol2:
        num = str(num)
    elif not bol and bol2:
        num = int(num)

    for y, row in enumerate(plot):
        for x, point in enumerate(row):
            if point == num:
                return True

    return False


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

        bol = check_for_number(ref_plot, 2)
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

    val_list = []
    if test >= 1:
        print("Valid position check: ({},{})".format(y, x))
        print("col_num Value: {}".format(col_num))
    # try:
    points, yx_points = get_surrounding_points_5x5_vary(main_plot, y, x)
    val_list, amount_list = count_list(points)
    anw = t_w_p_logic(col_num, con_col, val_list, amount_list)
    # except:
    #     # print("******************************************************************************************************")
    #     print("Error Point: ({},{}) cul_num: {}".format(y, x, col_num))
    #     print(val_list)
    #     pass
    # else:

    return anw


# updated in 5x5_vary
def get_surrounding_points_5x5(main_plot, y, x):
    row_num = len(main_plot)
    col_num = len(main_plot[0])
    points = []

    a = y - 2
    b = y + 2
    c = x - 2
    d = x + 2
    e = y - 1
    f = y + 1
    g = x - 1
    h = x + 1

    points.append(main_plot[y, x])

    if y > 1:
        points.append(main_plot[a, x])
        if x > 1:
            points.append(main_plot[a, c])
            points.append(main_plot[a, g])
            points.append(main_plot[e, c])
        if x < col_num - 2:
            points.append(main_plot[a, d])
            points.append(main_plot[a, h])
            points.append(main_plot[e, d])
    if y < row_num - 2:
        points.append(main_plot[b, x])
        if x > 1:
            points.append(main_plot[b, c])
            points.append(main_plot[b, g])
            points.append(main_plot[f, c])
        if x < col_num - 2:
            points.append(main_plot[b, d])
            points.append(main_plot[b, h])
            points.append(main_plot[f, d])
    if x > 0:
        points.append(main_plot[y, c])
    if x < col_num - 2:
        points.append(main_plot[y, d])

    return points


def get_surrounding_points_5x5_vary(main_plot, y, x):
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
    test = 1

    if test >= 1:
        print("** t_w_p_logic() console debug **")
        print("col_num: {} ".format(col_num))

    if col_num not in val_list:
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


# not used
def reverse_plot(plot, flip):

    plot = np.flip(plot)
    # for y, row in enumerate(plot):
    #     print(row)
    #     row = row.reverse()
    #     print(row)
    #     plot[y] = row
    # plot = plot.reverse()

    if flip == 0:
        flip = 1
        print("Reversed")
    elif flip == 1:
        flip = 0
        print("Normal")

    return plot

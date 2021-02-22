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
        self.ref_plot = []
        self.col_num = colour_number
        self.object_count = 0
        self.colour = colour
        self.ob_matrix_list = []

    def create_ref_plot(self):

        self.set_matrix_w_h()

        p_row = ["0"] * self.matrix_width
        self.ref_plot = np.array([p_row] * self.matrix_height)

        for y, row in enumerate(self.matrix):
            for x, point in enumerate(row):

                val = self.matrix[y, x]
                if val == self.col_num:
                    val = "a"
                else:
                    val = str(val)
                self.ref_plot[y, x] = val

    def process_colour_plot(self, main_plot):
        ref_plot = self.ref_plot
        plot = self.matrix
        ob_count = self.object_count
        col_num = self.col_num
        col_letter = "a"
        count = 0
        i = 0

        self.create_ref_plot()

        for y, row in enumerate(ref_plot):
            # if i > 4:
            #     break

            for x, point in enumerate(row):

                if point == col_letter:  # added another var to this
                    count += 1
                    max_yx, min_yx = self.get_object_outline(main_plot, ref_plot, (y, x), 8, count)
                    print_plot(ref_plot)
                    print("")
                    self.reversible_mine_sweeper_fill(main_plot, ref_plot, max_yx, min_yx, count)
                    print_plot(ref_plot)
                i += 1

    def get_object_outline(self, main_plot, ref_plot, start_yx, start_point, count):
        plot = main_plot
        col_num = self.col_num
        y, x = start_yx
        l_point = start_point
        ind_list = []
        # count = 1
        test = 0
        bol = isinstance(ref_plot[0, 0], str)

        if bol:
            count = str(count)

        # if out_plot == 0:
        #     p_row = [0] * self.matrix_width
        #     out_plot = np.array([p_row] * self.matrix_height)

        ref_plot[y, x] = count
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
                            print("can't go equal points pon_a: {} pon_b: {}".format(pon_a, pon_b))
                            points = get_surrounding_points_5x5(plot, y - 1, x - 1)
                            val_list, amount_list = count_list(points)
                            anw = t_w_p_logic(col_num, pon_a, val_list, amount_list)

                            if anw == 1:
                                y -= 1
                                x -= 1
                                print("Set ({},{})".format(y, x))
                                ref_plot[y, x] = count
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
                                print("({},{})".format(y, x))
                                ref_plot[y, x] = count
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
                            comp = True
                            # print("y-1")
                            # check outline_list
                            y -= 1
                            print("({},{})".format(y, x))
                            ref_plot[y, x] = count
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
                            print("can't go")
                            points = get_surrounding_points_5x5(plot, y - 1, x + 1)
                            val_list, amount_list = count_list(points)
                            anw = t_w_p_logic(col_num, pon_a, val_list, amount_list)

                            if anw == 1:
                                y -= 1
                                x += 1
                                print("Set ({},{})".format(y, x))
                                ref_plot[y, x] = count
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
                                print("({},{})".format(y, x))
                                ref_plot[y, x] = count
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
                            print("({},{})".format(y, x))
                            ref_plot[y, x] = count
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
                            print("can't go equal points pon_a: {} pon_b: {}".format(pon_a, pon_b))
                            points = get_surrounding_points_5x5(plot, y + 1, x + 1)
                            val_list, amount_list = count_list(points)
                            anw = t_w_p_logic(col_num, pon_a, val_list, amount_list)

                            if anw == 1:
                                y += 1
                                x += 1
                                print("Set ({},{})".format(y, x))
                                ref_plot[y, x] = count
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
                                print("({},{})".format(y, x))
                                ref_plot[y, x] = count
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

                            print("({},{})".format(y, x))
                            ref_plot[y, x] = count
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
                            print("can't go")
                            points = get_surrounding_points_5x5(plot, y + 1, x - 1)
                            val_list, amount_list = count_list(points)
                            anw = t_w_p_logic(col_num, pon_a, val_list, amount_list)

                            if anw == 1:
                                y += 1
                                x -= 1
                                print("Set ({},{})".format(y, x))
                                ref_plot[y, x] = count
                                ind_list.append((y, x))
                                l_point = 3
                            if anw == 2:
                                pass
                            if anw == 3:
                                pass
                        else:
                            if (y, x - 1) == ind_list[0]:
                                break
                            else:
                                comp = True
                                # print("y+1, x-1")
                                # check outline_list
                                y += 1
                                x -= 1
                                print("({},{})".format(y, x))
                                ref_plot[y, x] = count
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
                            print("({},{})".format(y, x))
                            ref_plot[y, x] = count
                            ind_list.append((y, x))
                            l_point = 4

                if l_point != 4:
                    l_point = 8

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

        max_yx = (max_y, max_x)
        min_yx = (min_y, min_x)

        return max_yx, min_yx

    def mine_sweeper_fill(self, main_plot, ref_plot, max_yx, min_yx, count):
        plot = main_plot
        col_num = self.col_num
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
                        points = get_surrounding_points(plot, ref_plot, y, x)

                        if count not in points:
                            pass
                        else:
                            print("({},{})".format(y,x))
                            ref_plot[y, x] = count

    def reversible_mine_sweeper_fill(self, main_plot, ref_plot, max_yx, min_yx, count):
        plot = main_plot
        col_num = self.col_num
        min_y, min_x = min_yx
        max_y, max_x = max_yx
        flip = 0
        change = 1
        bol = isinstance(ref_plot[0, 0], str)

        if bol:
            col_num = "a"
            count = str(count)

        while change == 1:
            change = 0

            for y, row in enumerate(ref_plot):
                for x, point in enumerate(ref_plot[0]):
                    if min_x <= x <= max_x and min_y <= y <= max_y:
                        if ref_plot[y, x] == col_num:
                            points = get_surrounding_points(plot, ref_plot, y, x)

                            if count not in points:
                                pass
                            else:
                                print("({},{})".format(y, x))
                                ref_plot[y, x] = count
                                change = 1
            if change == 0 and flip == 1:
                reverse_plot(ref_plot, flip)
            if change == 0 and flip == 0:
                pass

    def create_object_plot(self):
        pass


class ObjectPlot(Plot):

    def __init__(self,matrix, object_number, colour):
        super().__init__(matrix)
        self.ob_num = object_number
        self.out_ob = 0
        self.in_ob = 2
        self.ob_fill_all = []
        self.ob_outline = []
        self.ob_fill = []
        self.colour = colour


class StitchObjects:

    def __init__(self, passed_colour, passed_object_id, height, width):
        self.stitch_list = []
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


def get_surrounding_points(plot, out_plot, y, x):
    row_num = len(out_plot)
    col_num = len(out_plot[0])
    points = []
    a = y - 1
    b = y + 1
    c = x - 1
    d = x + 1

    if y > 0:
        p_a = plot[y - 1, x]
        points.append(out_plot[a, x])

        if x > 0:
            p_c = plot[y, x - 1]
            if p_a != p_c:
                points.append(out_plot[a, c])
            elif p_a == p_c:
                anw = get_surrounding_points_5x5(plot, y - 1, x - 1)
                if anw == 1:
                    points.append(out_plot[a, c])

        if x < col_num - 1:
            p_d = plot[y, x + 1]
            if p_a != p_d:
                points.append(out_plot[a, d])
            elif p_a == p_d:
                anw = get_surrounding_points_5x5(plot, y - 1, x + 1)
                if anw == 1:
                    points.append(out_plot[a, d])

    if y < row_num - 1:
        p_b = plot[y + 1, x]
        points.append(out_plot[b, x])
        if x > 0:
            p_c = plot[y, x - 1]
            if p_b != p_c:
                points.append(out_plot[b, c])
            elif p_b == p_c:
                anw = get_surrounding_points_5x5(plot, y + 1, x - 1)
                if anw == 1:
                    points.append(out_plot[b, c])

        if x < col_num - 1:
            p_c = plot[y, x + 1]
            if p_b != p_c:
                points.append(out_plot[b, d])
            elif p_b == p_c:
                anw = get_surrounding_points_5x5(plot, y + 1, x + 1)
                if anw == 1:
                    points.append(out_plot[b, d])

    if x > 0:
        points.append(out_plot[y, c])
    if x < col_num - 1:
        points.append(out_plot[y, d])
    return points


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

    ind = val_list.index(con_col)
    con_amount = amount_list[ind]
    ind = val_list.index(col_num)
    col_amount = amount_list[ind]

    if con_amount > col_amount:
        print("col_num is a line")
        return 1
    elif con_amount < col_amount:
        print("col_con is the line")
        return 2
    else:
        print("Both are equal")
        return 3


def reverse_plot(plot, flip):

    for y, row in enumerate(plot):
        row = reversed(list(row))
        plot[y] = row
    plot = reversed(plot)

    if flip == 0:
        flip = 1
        print("Reversed")
    elif flip == 1:
        flip = 0
        print("Normal")

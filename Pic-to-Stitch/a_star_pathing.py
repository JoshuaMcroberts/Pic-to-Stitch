import numpy as np
import plot_objects as po


class Node:

    def __init__(self):
        self.h = int
        self.g = int
        self.f = 0
        self.l_point = int
        self.co_or = (0, 0)

    def set_co_or(self, val):
        test = 0
        if test == 5:
            print("set_co_or - Node - a_start_pathing.py")
        self.co_or = val

    def set_h(self, val):
        test = 0
        if test == 5:
            print("set_h - Node - a_start_pathing.py")
        self.h = val

    def set_g(self, val):
        test = 0
        if test == 5:
            print("set_g - Node - a_start_pathing.py")
        self.g = val

    def set_f(self, val):
        test = 0
        if test == 5:
            print("set_f - Node - a_start_pathing.py")
        self.f = val

    def set_l_point(self, val):
        test = 0
        if test == 5:
            print("set_l_point - Node - a_start_pathing.py")
        self.l_point = val

    def get_f(self):
        test = 0
        if test == 5:
            print("get_f - Node - a_start_pathing.py")
        return self.f

    def get_h(self):
        test = 0
        if test == 5:
            print("get_h - Node - a_start_pathing.py")
        return self.h

    def get_g(self):
        test = 0
        if test == 5:
            print("get_g - Node - a_start_pathing.py")
        return self.g

    def get_l_point(self):
        test = 0
        if test == 5:
            print("get_l_point - Node - a_start_pathing.py")
        return self.l_point

    def get_co_or(self):
        test = 0
        if test == 5:
            print("get_co_or - Node - a_start_pathing.py")
        return self.co_or

    def printe(self):
        test = 5
        if test == 5:
            print("printe - Node - a_start_pathing.py")
        print("H: {}\nF: {}\nG: {}\nCo-or: {}\nLast Point: {}".format(self.h, self.f, self.g, self.co_or, self.l_point))

    def point_set_print(self):
        test = 5
        if test == 5:
            print("point_set_print - Node - a_start_pathing.py")
        print("Co_or: {} L_p: {}".format(self.co_or, self.l_point))


def move_to_a_star(main_plot, goto_yx, start_yx, passed_ind_list):
    test = 1
    if test == 5:
        print("move_to_a_star - a_start_pathing.py")

    open_list = []
    closed_list = []
    rev_ind_list = []
    num_plot = main_plot.copy()
    node = Node()

    p_row = [node] * len(main_plot[0])  # create an matrix of nodes
    node_plot = np.array([p_row] * len(main_plot))

    if test == 1:
        print("Empty Nodes")
        print_node_plot(node_plot)

    for y, row in enumerate(main_plot):     # set nodes in matrix with yx
        for x, point in enumerate(row):
            node = Node()
            node.set_co_or((y, x))
            node_plot[y, x] = node

    if test == 1:
        print("YX Nodes")
        print_node_plot(node_plot)

    y, x = start_yx

    node = node_plot[y, x]
    set_node(node, node_plot, start_yx, goto_yx, 0, 0)

    open_list.append(node)

    ext = 0
    while ext != 1:

        cur_node = lowest_f(open_list)

        if cur_node == 0:
            break

        open_list.remove(cur_node)
        closed_list.append(cur_node)

        node_yx = cur_node.get_co_or()
        y, x = node_yx
        num_plot[y, x] = 0

        if test == 1:
            print("\nCur_node_yx: {} GoTo_yx: {}".format(node_yx, goto_yx))

        cur_g = cur_node.get_g()

        if node_yx == goto_yx:

            if test == 1:
                print("Exit Loop")
                print("closed")
                print_node_list(closed_list)
                print("\nopen")
                print_node_list(open_list)

            break

        y, x = node_yx
        points = get_surrounding_nodes(num_plot, y, x)

        for j in points:

            y, x, g_step, l_p = j
            g = g_step + cur_g

            node = node_plot[y, x]
            set_node(node, node_plot, (y, x), goto_yx, g, l_p)

            if node in closed_list:
                pass

            elif node in open_list:

                for k in open_list:
                    k_co = k.get_co_or()
                    node_co = node.get_co_or()

                    if k_co == node_co:
                        k_g = k.get_g()
                        node_g = node.get_g()

                        if k_g >= node_g:
                            n_g = node_g
                            k.set_g(n_g)
                            k.set_l_point(node.get_l_point())
                            k_h = k.get_h()
                            f = k_h + n_g
                            k.set_f(f)
            else:
                open_list.append(node)

    cur_node = closed_list[-1]
    cur_co = cur_node.get_co_or()
    rev_ind_list.append(cur_co)

    ext = 0
    while ext != 1:

        for i in closed_list:
            l_p = cur_node.get_l_point()
            i_co = i.get_co_or()
            i_lp = i.get_l_point()

            if l_p == i_co:
                if test == 1:
                    print("\nGoto: {} start:  {}\nCur_node co-or: {} l_p: {}\nLis_node co-or: {} l_p: {}".format(goto_yx, start_yx, cur_co, l_p, i_co, i_lp))
                    print_node_list(closed_list)
                cur_node = i
                cur_co = cur_node.get_co_or()
                rev_ind_list.append(cur_co)
                break
            elif l_p == 0:
                if test == 1:
                    print("Exit Move Return ind_list")

                ext = 1
                break

    rev_ind_list.reverse()
    del rev_ind_list[0]

    for i in rev_ind_list:
        passed_ind_list.append(i)

    return rev_ind_list[-1], passed_ind_list


def set_node(node, plot, start_yx, goto_yx, g, l_p):
    test = 0
    if test == 5:
        print("set_node - a_start_pathing.py")

    if test == 1:
        print("\n[] set_node function")

    rlist = []
    h, rlist = po.find_path(plot, goto_yx, start_yx, rlist)
    node.set_h(h)
    node.set_g(g)
    f = g + h
    node.set_f(f)
    node.set_l_point(l_p)
    if test == 1:
        print("return f: {}\nreturn g: {}\nreturn lp: {}".format(f, g, l_p))


def lowest_f(open_list):
    test = 0
    if test == 5:
        print("lowest_f - a_start_pathing.py")

    if test == 1:
        print("\n[] Search Open List")

    if len(open_list) == 1:
        if test == 1:
            print("Process point")
            open_list[0].point_set_print()
        return open_list[0]

    elif len(open_list) == 0:
        if test == 1:
            print("Open List Empty")
        # return 0

    else:
        cur_node = open_list[0]

        for i in open_list:
            f = i.get_f()
            lower_f = cur_node.get_f()

            if f < lower_f:
                cur_node = i

            elif f == lower_f:
                h = i.get_h()
                cur_node_h = cur_node.get_h()

                if h < cur_node_h:
                    cur_node = i
        if test == 1:
            print("Process point")
            cur_node.point_set_print()
        return cur_node


def get_surrounding_nodes(plot, y, x):
    test = 0
    if test == 5:
        print("get_surrounding_nodes - a_start_pathing.py")

    if test == 2:
        print("\n[] get_surrounding_nodes function")

    row_num = len(plot)
    cul_num = len(plot[0])
    points = []
    a = y - 1
    b = y + 1
    c = x - 1
    d = x + 1

    if test == 1:
        print("Centre: ({},{})".format(y, x))

    if y > 0:
        p_a = plot[a, x]
        if p_a != 0:
            points.append((a, x, 10, (y, x)))
            if test == 1:
                print(" Sur_2: ({},{})".format(a, x))

        if x > 0:
            p_c = plot[a, c]
            if p_c != 0:
                points.append((a, c, 14, (y, x)))
                if test == 1:
                    print(" Sur_1: ({},{})".format(a, c))

        if x < cul_num - 1:
            p_d = plot[a, d]
            if p_d != 0:
                points.append((a, d, 14, (y, x)))
                if test == 1:
                    print(" Sur_3: ({},{})".format(a, d))

    if y < row_num - 1:
        p_b = plot[b, x]
        if p_b != 0:
            points.append((b, x, 10, (y, x)))
            if test == 1:
                print(" Sur_6: ({},{})".format(b, x))

        if x > 0:
            p_c = plot[b, c]
            if p_c != 0:
                points.append((b, c, 14, (y, x)))
                if test == 1:
                    print(" Sur_7: ({},{})".format(b, c))

        if x < cul_num - 1:
            p_c = plot[b, d]
            if p_c != 0:
                points.append((b, d, 14, (y, x)))
                if test == 1:
                    print(" Sur_5: ({},{})".format(b, d))

    if x > 0:
        p_c = plot[y, c]
        if p_c != 0:
            points.append((y, c, 10, (y, x)))
            if test == 1:
                print(" Sur_8: ({},{})".format(y, c))

    if x < cul_num - 1:
        p_d = plot[y, d]
        if p_d != 0:
            points.append((y, d, 10, (y, x)))
            if test == 1:
                print(" Sur_4: ({},{})".format(y, d))

    return points


def print_node_plot(node_plot):
    test = 0
    if test == 5:
        print("print_node_plot - a_start_pathing.py")

        print("\n[] print_node_plot function")

        print_val = " \n"
        for y, row in enumerate(node_plot):

            for x, node in enumerate(row):
                co = node.get_co_or()
                print_val = print_val + str(co) + " "
            print_val = print_val + "\n"
        print(print_val)


def print_node_list(node_list):
    test = 0
    if test == 5:
        print("print_node_list - a_start_pathing.py")

        print("\n[] print_list_plot function")
        print_val = " \n"

        for x, node in enumerate(node_list):
            co = node.get_co_or()
            lp = node.get_l_point()
            print_val = print_val + str(co) + " " + str(lp) + "\n"

        print(print_val)


import numpy as np
from pic_to_stitch import plot_objects as po


class Node:

    def __init__(self):
        self.h = int()
        self.g = int()
        self.f = int()
        self.l_point = int()
        self.co_or = tuple()

    def set_co_or(self, val):
        self.co_or = val

    def set_h(self, val):
        self.h = val

    def set_g(self, val):
        self.g = val

    def set_f(self, val):
        self.f = val

    def set_l_point(self, val):
        self.l_point = val

    def get_f(self):
        return self.f

    def get_h(self):
        return self.h

    def get_g(self):
        return self.g

    def get_l_point(self):
        return self.l_point

    def get_co_or(self):
        return self.co_or

    # console testing method - Displays node attribute values
    def print_node(self):
        test = 5
        if test == 5:
            print("print_node - Node - a_start_pathing.py")
        print("H: {}\nF: {}\nG: {}\nCo-or: {}\nLast Point: {}".format(self.h, self.f, self.g, self.co_or, self.l_point))

    # console testing method - Displays current point and last point
    def point_set_print(self):
        test = 5
        if test == 5:
            print("point_set_print - Node - a_start_pathing.py")
        print("Co_or: {} L_p: {}".format(self.co_or, self.l_point))


# create a jump_co_or_list between 2 point on a plot - a* pathing with the most efficient path between 'A' and 'B'
def move_to_a_star(main, main_plot, goto_yx, start_yx, passed_ind_list):
    test = 0

    # console testing comment
    if test == 5:
        print("move_to_a_star - a_start_pathing.py")

    # progress bar update
    if main is not None:
        msg_count = 0
        msg = "Moving... (Points Processed: " + str(msg_count) + ")"
        main.bar_update_message(msg)
    # end

    open_list = []
    closed_list = []
    rev_ind_list = []
    num_plot = main_plot.copy()
    node = Node()

    p_row = [node] * len(main_plot[0])  # create an matrix of nodes the same size as main_plot matrix
    node_plot = np.array([p_row] * len(main_plot))

    # console testing comment
    if test == 1:
        print("Empty Nodes")
        print_node_plot(node_plot)

    # for each row in main_plot
    for y, row in enumerate(main_plot):
        # for each point in row
        for x, point in enumerate(row):
            node = Node()                   # create node object
            node.set_co_or((y, x))          # set node co_or matrix with yx
            node_plot[y, x] = node          # put new node in node_plot[y, x]

    # console testing comment
    if test == 1:
        print("YX Nodes")
        print_node_plot(node_plot)

    y, x = start_yx                                     # get y and x from start_yx

    node = node_plot[y, x]                              # get start node using y x
    set_node(node, node_plot, start_yx, goto_yx, 0, 0)  # set node attributes

    open_list.append(node)                              # append node to open_list

    ext = 0                         # set exit to 0

    # while exit is not equal to 1
    while ext != 1:

        # progress bar update
        if main is not None:
            msg_count += 1
            if msg_count % 10 == 0:
                msg = "Moving... (Points Processed: " + str(msg_count) + ")"
                main.bar_update_message(msg)
        # end

        # return the node with the lowest f value in list
        cur_node = lowest_f(open_list)

        if cur_node == 0:               # if current node is equal to 0
            break                       # break - reached end point

        open_list.remove(cur_node)      # remove current node from open list - list of potential valid moves
        closed_list.append(cur_node)    # append current node to closed list - list of already visited nodes

        node_yx = cur_node.get_co_or()  # get node y, x
        y, x = node_yx
        num_plot[y, x] = 0              # replace node object with 0 - now not a valid move when looked at

        # console testing comment
        if test == 1:
            print("\nCur_node_yx: {} GoTo_yx: {}".format(node_yx, goto_yx))

        cur_g = cur_node.get_g()    # get current node g value - g value is the calculated distance from the start point

        if node_yx == goto_yx:      # if node yx is equal to the end point yx

            #  console testing comment
            if test == 1:
                print("Exit Loop")
                print("closed")
                print_node_list(closed_list)
                print("\nopen")
                print_node_list(open_list)

            break                   # break - reached end point

        y, x = node_yx              # set y, x using node_yx

        # return a list of valid point that surround current point
        points = get_surrounding_nodes(num_plot, y, x)

        # for each point in points
        for j in points:

            y, x, g_step, l_p = j       # get attribute values
            g = g_step + cur_g          # create point g by adding current point g to g_step

            node = node_plot[y, x]      # get node object from node matrix

            # set node attributes
            set_node(node, node_plot, (y, x), goto_yx, g, l_p)

            if node in closed_list:     # if node is in closed list...
                pass                        # do nothing - already visited

            elif node in open_list:     # else if node is in open list...

                # for each k node in open list
                for k in open_list:
                    k_co = k.get_co_or()            # get k node co-ordinates
                    node_co = node.get_co_or()      # get node co-ordinates

                    if k_co == node_co:     # if k node co-ordinates equal node co-ordinates...- find node in open list
                        k_g = k.get_g()         # get k node g value
                        node_g = node.get_g()   # get node g value

                        if k_g >= node_g:       # if k node g is equal or more than node g...- check distance from start
                            n_g = node_g
                            k.set_g(n_g)            # set k node g using node g
                            k.set_l_point(node.get_l_point())   # set k node last point as node last point
                            k_h = k.get_h()         # get k node h
                            f = k_h + n_g           # create f value
                            k.set_f(f)              # set k node f value

            else:                       # else if node is not in open list or closed list...
                open_list.append(node)      # append node to closed list

    cur_node = closed_list[-1]      # set last in closed list to current node
    cur_co = cur_node.get_co_or()   # get current nodes co-ordinate
    rev_ind_list.append(cur_co)     # append co-ordinates to reverse index list - used to map path travelled

    ext = 0     # reset exit to 0

    # while exit is not equal to 1
    while ext != 1:

        # for each i node in closed list
        for i in closed_list:
            l_p = cur_node.get_l_point()        # get current node last point
            i_co = i.get_co_or()                # get i node co-ordinates
            i_lp = i.get_l_point()              # get i node last point

            if l_p == i_co:         # if current node last point is equal to i node co-ordinates...

                # console testing comment
                if test == 1:
                    print("\nGoto: {} start:  {}\nCur_node co-or: {} l_p: {}\nLis_node co-or: {} l_p: {}".format(goto_yx, start_yx, cur_co, l_p, i_co, i_lp))
                    print_node_list(closed_list)

                cur_node = i                    # set current node equal to i node
                cur_co = cur_node.get_co_or()   # get current node co-ordinates
                rev_ind_list.append(cur_co)     # append co-ordinates to reverse index list
                break                           # break for loop

            elif l_p == 0:          # else if current node last point equals 0...

                # console testing comment
                if test == 1:
                    print("Exit Move Return ind_list")

                ext = 1             # set exit to 1 - will exit while loop
                break               # break for loop

    rev_ind_list.reverse()          # reverse, reverse index list to get a start to end path
    del rev_ind_list[0]             # delete first value of reversed reverse index list

    # for each tuple in reverse index list
    for i in rev_ind_list:
        passed_ind_list.append(i)       # append tuple to passed index list

    return rev_ind_list[-1], passed_ind_list    # return last point , return passed index list


def set_node(node, plot, start_yx, goto_yx, g, l_p):
    test = 0

    # console testing comment
    if test == 5:
        print("set_node - a_start_pathing.py")
    elif test == 1:
        print("\n[] set_node function")

    rlist = []

    # returns most efficient path to end point without looking at obstacles, calculates h value - distance to end point
    h, rlist = po.find_path(plot, goto_yx, start_yx, rlist)
    node.set_h(h)           # set node h value
    node.set_g(g)           # set node g value
    f = g + h               # create f value
    node.set_f(f)           # set node f value
    node.set_l_point(l_p)   # set node last point

    # console testing comment
    if test == 1:
        print("return f: {}\nreturn g: {}\nreturn lp: {}".format(f, g, l_p))


def lowest_f(open_list):
    test = 0

    # console testing comment
    if test == 5:
        print("lowest_f - a_start_pathing.py")
    elif test == 1:
        print("\n[] Search Open List")

    if len(open_list) == 1:     # if length of open list is 1...

        # console testing comment
        if test == 1:
            print("Process point")
            open_list[0].point_set_print()

        return open_list[0]         # return first position of open list

    elif len(open_list) == 0:   # else if length of open list is 0...

        # console testing comment
        if test == 1:
            print("Open List Empty")
        pass                        # do nothing

    else:                       # else if length of open list is greater than 1...

        cur_node = open_list[0]     # set current node set first position of open list

        # for each i node in open list
        for i in open_list:
            f = i.get_f()               # get f value
            lower_f = cur_node.get_f()  # get current node f value

            if f < lower_f:         # if i node f value is less than current node f value...
                cur_node = i            # set i node to current node - i node becomes new lowest value node

            elif f == lower_f:      # else if current node f value and i node f value are equal...
                h = i.get_h()                   # get  i node h value
                cur_node_h = cur_node.get_h()   # get current node h value

                if h < cur_node_h:  # if i node h value is less than current node h value...
                    cur_node = i         # set i node to current node - i node new lowest even though f values are same

        # console testing comment
        if test == 1:
            print("Process point")
            cur_node.point_set_print()
        return cur_node     # return current node - for loop only ends after all in open list have been checked


# returns list of nodes surrounding the y, x values given
def get_surrounding_nodes(plot, y, x):
    test = 0

    # console testing comment
    if test == 5:
        print("get_surrounding_nodes - a_start_pathing.py")
    elif test == 2:
        print("\n[] get_surrounding_nodes function")
    elif test == 1:
        print("Centre: ({},{})".format(y, x))

    row_num = len(plot)         # set row number
    cul_num = len(plot[0])      # set column number
    points = []                 # create points list
    a = y - 1                   # set a
    b = y + 1                   # set b
    c = x - 1                   # set c
    d = x + 1                   # set d

    if y > 0:                   # if y is greater than 0... - value y - 1 can be set
        p_a = plot[a, x]            # get node at y - 1, x

        if p_a != 0:                # if node not equal to 0...
            points.append((a, x, 10, (y, x)))       # append y - 1, x, cardinal step value, and current y,x as tuple

            # console testing comment
            if test == 1:
                print(" Sur_2: ({},{})".format(a, x))

        if x > 0:               # if x is greater then 0... - value x - 1 can be set
            p_c = plot[a, c]        # get node at y -1, x - 1

            if p_c != 0:            # if node is not equal to 0...
                points.append((a, c, 14, (y, x)))   # append y - 1, x - 1, diagonal step value and current y,x as tuple

                # console testing comment
                if test == 1:
                    print(" Sur_1: ({},{})".format(a, c))

        if x < cul_num - 1:     # if x is less than column length - 1... - value x + 1 can be set
            p_d = plot[a, d]        # get node at y - 1, x + 1

            if p_d != 0:            # if node is not equal to 0...
                points.append((a, d, 14, (y, x)))   # append y - 1, x + 1, diagonal step value and current y,x as tuple

                # console testing comment
                if test == 1:
                    print(" Sur_3: ({},{})".format(a, d))

    if y < row_num - 1:         # if y is less than row length - 1... - value y + 1 can be set
        p_b = plot[b, x]            # get node at y - 1, x + 1

        if p_b != 0:                # if node is not equal to 0...
            points.append((b, x, 10, (y, x)))       # append y + 1, x, vertical step value and current y,x as tuple

            # console testing comment
            if test == 1:
                print(" Sur_6: ({},{})".format(b, x))

        if x > 0:               # if x is greater then 0... - value x - 1 can be set
            p_c = plot[b, c]        # get node at y + 1, x - 1

            if p_c != 0:            # if node is not equal to 0...
                points.append((b, c, 14, (y, x)))   # append y + 1, x - 1, diagonal step value and current y,x as tuple

                # console testing comment
                if test == 1:
                    print(" Sur_7: ({},{})".format(b, c))

        if x < cul_num - 1:         # if x is less than column length - 1... - value x + 1 can be set
            p_c = plot[b, d]            # get node at y + 1, x + 1

            if p_c != 0:                # if node is not equal to 0...
                points.append((b, d, 14, (y, x)))   # append y + 1, x + 1, diagonal step value and current y,x as tuple

                # console testing comment
                if test == 1:
                    print(" Sur_5: ({},{})".format(b, d))

    if x > 0:                       # if x is greater then 0... - value x - 1 can be set
        p_c = plot[y, c]                # get node at y, x - 1

        if p_c != 0:                    # if node is not equal to 0...
            points.append((y, c, 10, (y, x)))   # append y, x - 1, diagonal step value and current y,x as tuple

            # console testing comment
            if test == 1:
                print(" Sur_8: ({},{})".format(y, c))

    if x < cul_num - 1:             # if x is less than column length - 1... - value x + 1 can be set
        p_d = plot[y, d]                # get node at y, x + 1

        if p_d != 0:                    # if node is not equal to 0...
            points.append((y, d, 10, (y, x)))   # append y, x + 1, diagonal step value and current y,x as tuple

            # console testing comment
            if test == 1:
                print(" Sur_4: ({},{})".format(y, d))

    return points


# console testing function - Displays full node plot as co-ordinates tuples
def print_node_plot(node_plot):
    test = 5
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


# console testing method - Displays list of nodes as list of node co-ordinates tuples
def print_node_list(node_list):
    test = 5
    if test == 5:
        print("print_node_list - a_start_pathing.py")

        print("\n[] print_list_plot function")
        print_val = " \n"

        for x, node in enumerate(node_list):
            co = node.get_co_or()
            lp = node.get_l_point()
            print_val = print_val + str(co) + " " + str(lp) + "\n"

        print(print_val)


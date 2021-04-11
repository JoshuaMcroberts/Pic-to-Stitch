import numpy as np
from pic_to_stitch import a_star_pathing as asp


class Plot:

    def __init__(self):

        self.matrix = []
        self.col_list = []
        self.col_amount = int()
        self.matrix_width = int()
        self.matrix_height = int()
        self.col_matrix_list = []

    def set_matrix(self, matrix):
        self.matrix = matrix

    def set_col_list(self, col_list):
        self.col_list = col_list

    def set_col_amount(self, col_amount):
        self.col_amount = col_amount

    def set_matrix_width(self, width):
        self.matrix_width = width

    def set_matrix_height(self, height):
        self.matrix_height = height

    def set_col_matrix_list(self, col_matrix_list):
        self.col_matrix_list = col_matrix_list

    def get_matrix(self):
        return self.matrix

    def get_col_list(self):
        return self.col_list

    def get_col_amount(self):
        return self.col_amount

    def get_matrix_width(self):
        return self.matrix_width

    def get_matrix_height(self):
        return self.matrix_height

    def get_col_matrix_list(self):
        return self.col_matrix_list

    # method used to set plot_objects attributes
    def create_matrix_object(self, matrix, colour_list):
        self.set_matrix(matrix)
        self.set_matrix_width(len(matrix[0]))
        self.set_matrix_height(len(matrix))
        self.set_col_list(colour_list)
        self.set_col_amount(len(colour_list))

    # create individual colour_objects based off the plot_object
    def create_sub_plot(self, main):
        test = 0

        # console testing comment
        if test == 5:
            print("create_sub_plot - class Plot - plot_objects.py")

        # progress bar creation
        if main is not None:
            message = "Starting Object Creation..."
            main.bar("Object Creation", message, 10, 0)
            main.bar_update_message(message)
            msg_count = 1
        # end

        # for each i in range colour amount
        for i in range(self.col_amount):

            colour = self.col_list[i]       # set colour from col_list

            # console testing comment
            if test == 1:
                print(i)
                print(self.col_list)

            p_row = [0] * self.matrix_width                 # create blank p_row list
            plot = np.array([p_row] * self.matrix_height)   # create blank plot matrix using p_row list

            # for each row in matrix
            for y, row in enumerate(self.matrix):
                # for each point in row
                for x, point in enumerate(row):

                    if point == i + 1:      # if point value is equal to i (current number) + 1...
                        plot[y, x] = i + 1  # set blank plot[y, x] to current number + 1

            # create colour_object
            col_plot = ColourPlot()
            col_plot.create_colour_plot(plot, i+1, colour)  # set colour plots attributes
            self.col_matrix_list.append(col_plot)           # append colour_object to col_matrix_list

            # progress bar update
            if main is not None:
                msg = "Colour Plot " + str(msg_count) + " Created..."
                main.bar_update_message(msg)
                msg_count += 1
            # end

    def print_col_matrix_list(self):
        test = 5

        # console testing comment
        if test == 5:
            print("print_col_matrix_list - class Plot - plot_objects.py")

        if not self.col_matrix_list:    # if col_matrix_list if empty...

            # console testing comment
            print("Not Matrix' in list")

        else:                           # else if col_matrix_list is not empty...

            # for each object in col_matrix_list
            for i in self.col_matrix_list:
                p_object = i
                plot = p_object.matrix
                ind = self.col_matrix_list.index(i)

                # console testing comment
                print("Colour: {}".format(ind))

                # for each row in plot
                for y, row in enumerate(plot):
                    p_row = ""                          # set print row to string

                    # for each point in row
                    for x, point in enumerate(row):

                        if point == 0:                  # if point is equal to 0
                            p_row += ". "               # add '. ' to print row
                            # (0 is the null value, other values now more easily read in console debugging)

                        else:                           # else if point is not equal to 0
                            p_row += str(point) + " "   # add point value to print row followed by a space

                    print(p_row)    # print row list


class ColourPlot(Plot):

    def __init__(self):
        super().__init__()
        self.col_num = int()
        self.ref_plot = []
        self.object_count = int()
        self.colour = tuple()
        self.ob_matrix_list = []

    def set_col_num(self, col_num):
        self.col_num = col_num

    def set_ref_plot(self, ref_plot):
        self.ref_plot = ref_plot

    def set_object_count(self, object_count):
        self.object_count = object_count

    def set_colour(self, colour):
        self.colour = colour

    def set_ob_matrix_list(self, matrix_list):
        self.ob_matrix_list = matrix_list

    def get_col_num(self):
        return self.col_num

    def get_ref_plot(self):
        return self.ref_plot

    def get_object_count(self):
        return self.object_count

    def get_colour(self):
        return self.colour

    def get_ob_matrix_list(self):
        return self.ob_matrix_list

    # create ColourPlot variables using matrix, colour number and colour
    def create_colour_plot(self, matrix, colour_number, colour):

        self.set_matrix(matrix)                 # set matrix
        self.set_col_num(colour_number)         # set colour number
        ref_plot = self.create_ref_plot(0)      # create ref_plot
        self.set_ref_plot(ref_plot)             # set ref_plot
        self.set_object_count(0)                 # set object count
        self.set_colour(colour)                 # set colour
        self.set_ob_matrix_list([])             # set object matrix list

    # create a reference plot using one argument
    def create_ref_plot(self, arg):
        test = 0
        # console testing comment
        if test == 5:
            print("create_ref_plot - class ColourPlot - plot_objects.py")

        if arg == 1:      # if arg is equal to 1...
            p_row = ["b"] * len(self.matrix[0])    # create rows with string 'b' value
        else:             # else if arg is not equal to 1...
            p_row = ["0"] * len(self.matrix[0])        # create rows with string '0' value

        ref_plot = np.array([p_row] * len(self.matrix))   # create numpy array using rows

        # for each row in matrix
        for y, row in enumerate(self.matrix):

            # for each value in row
            for x, val in enumerate(row):

                if val == self.col_num:         # if value is equal to colour number...
                    val = "a"                       # set value to string 'a'
                elif val == 0 and arg == 1:     # else if value is equal to 0 and arg is equal to 1...
                    val = "b"                       # set value to string 'b'
                else:                           # else if value is not colour number and not 0...
                    val = str(val)                  # set value equal to string value

                ref_plot[y, x] = val            # set reference plot (y,x) equal to value
        return ref_plot

    # finds unset valid shape, gets the outline of the shape, fills in the shape and updates the ref_plot
    def process_colour_plot(self, main, col_count, main_plot):
        test = 0

        # console testing comment
        if test == 5:
            print("process_colour_plot - class ColourPlot - plot_objects.py")

        ref_plot = self.ref_plot    # get reference plot
        col_num = self.col_num      # get colour number
        col_letter = "a"
        count = 0

        msg_count = 1

        # for each row in reference plot
        for y, row in enumerate(ref_plot):

            # for each point in row
            for x, point in enumerate(row):

                if point == col_letter:     # if the point is equal to the colour letter

                    # progress bar update
                    if main is not None:
                        msg = "Colour Plot " + str(col_count) + " - Processing Section " + str(msg_count) + "..."
                        main.bar_update_message(msg)
                        main.bar_update_progress(msg_count, 0.3, 0)
                    # end

                    count += 1

                    # function finds and marks out the outline of an object, returns list of points on outline
                    max_yx, min_yx, ind_list = get_object_outline(main_plot, ref_plot, (y, x), 8, count, col_num)

                    # console testing comment
                    if test == 1:
                        print_plot(ref_plot)
                        print("")

                    # function uses the outline created by get_object_outline to fill the interior of the shape
                    ref_plot = reversible_mine_sweeper_fill(main_plot, ref_plot, max_yx, min_yx, count, col_num, 1)

                    # console testing comment
                    if test == 1:
                        print_plot(ref_plot)
                    msg_count += 1

        self.ref_plot = ref_plot

    # create value for object count
    def create_object_count(self):
        test = 0

        # console testing comment
        if test == 5:
            print("set_object_count - class ColourPlot - plot_objects.py")

        plot = self.ref_plot
        num = []
        row_list = []
        # for each row in plot
        for y, row in enumerate(plot):

            # for each point in row
            for x, point in enumerate(row):
                bol = isinstance(point, str)    # check if point is a string
                if bol:     # if bol is true...
                    point = int(point)      # make point an int
                    row_list.append(point)  # append point to row list

            val = max(row_list)     # get max value from row list
            num.append(val)         # append value to num list
        val = max(num)              # get max value from num list

        # console testing comment
        if test == 1:
            print("count is : {}".format(val))

        return val

    # separates different object of the same colour into a plot by themselves
    def create_object_sub_plot(self):
        test = 0

        # console testing comment
        if test == 5:
            print("create_object_sub_plot - class ColourPlot - plot_objects.py")

        # create object count value
        object_count = self.create_object_count()
        self.set_object_count(object_count)         # set object count value

        ref_plot = self.get_ref_plot()              # get ref_plot

        # for each in range object count
        for i in range(self.object_count):

            # console testing comment
            if test == 1:
                print(i+1)

            colour = self.get_colour()              # get colour

            p_row = [0] * len(ref_plot[0])              # create blank list
            plot = np.array([p_row] * len(ref_plot))    # create blank array with blank lists

            # loop through ref_plot
            for y, row in enumerate(ref_plot):
                for x, point in enumerate(row):

                    if point == str(i + 1):     # if point is equal to object number...
                        plot[y, x] = str(i + 1)     # set plot[y,x] to object number

            # console testing comment
            if test == 1:
                print_plot(plot)

            ob_plot = ObjectPlot()                                  # create new object plot
            ob_plot.create_object_plot(plot, i + 1, i + 1, colour)  # set object plot attributes
            self.ob_matrix_list.append(ob_plot)                     # appending object plot to ob_matrix_list

    # method used for console testing
    def print_ob_matrix_list(self):
        test = 1
        if test == 5:
            print("print_ob_matrix_list - class ColourPlot - plot_objects.py")

        if not self.ob_matrix_list:
            if test == 1:
                print("No Matrix in list")
        else:
            for i in self.ob_matrix_list:
                p_object = i
                plot = p_object.matrix
                ind = self.ob_matrix_list.index(i)
                if test == 1:
                    print("Object: {}".format(ind + 1))
                for y, row in enumerate(plot):
                    p_row = ""
                    for x, point in enumerate(row):

                        if point == 0:
                            p_row = p_row + ". "
                        else:
                            p_row = p_row + str(point) + " "

                    if test == 1:
                        print(p_row)


class ObjectPlot(ColourPlot):

    def __init__(self):
        super().__init__()
        self.ob_id = int()
        self.colour = tuple()
        self.ref_plot = []
        self.section_image = int()
        self.stitch_type = str()
        self.stitch_len = int()
        self.stitch_list = []

    def set_ob_id(self, ob_id):
        self.ob_id = ob_id

    def set_colour(self, colour):
        self.colour = colour

    def set_ref_plot(self, ref_plot):
        self.ref_plot = ref_plot

    def set_section_image(self, section_image):
        self.section_image = section_image

    def set_stitch_type(self, stitch_type):
        self.stitch_type = stitch_type

    def set_stitch_len(self, stitch_len):
        self.stitch_len = stitch_len

    def set_stitch_list(self, stitch_list):
        self.stitch_list = stitch_list

    def get_ob_id(self):
        return self.ob_id

    def get_colour(self):
        return self.colour

    def get_ref_plot(self):
        return self.ref_plot

    def get_section_image(self):
        return self.section_image

    def get_stitch_type(self):
        return self.stitch_type

    def get_stitch_len(self):
        return self.stitch_len

    def get_stitch_list(self):
        return self.stitch_list

    # sets attribute values for the object class
    def create_object_plot(self, matrix, colour_number, object_number, colour):
        self.set_matrix(matrix)             # set matrix
        self.set_ob_id(object_number)       # set object id
        self.set_col_num(colour_number)     # set colour number
        self.set_colour(colour)             # set colour
        self.set_ref_plot(self.create_ref_plot(1))  # set reference plot using inherited method from colour plot class

    # set values in object matrix to 1 leave at 0
    def process_matrix(self):
        test = 0

        # console testing comment
        if test == 5:
            print("process_matrix - class ObjectPlot - plot_objects.py")

        plot = self.matrix                  # get matrix

        # for each row in plot
        for y, row in enumerate(plot):
            # for each point in row
            for x, point in enumerate(row):
                if point != 0:              # if point is not equal to 0
                    self.matrix[y, x] = 1       # set matrix[y, x] to 1

    # sets stitch list to a list of co-ordinates that outline the object
    def outline_running_stitch(self):
        test = 0

        # console testing comment
        if test == 5:
            print("outline_running_stitch - class ObjectPlot - plot_objects.py")

        plot = self.matrix.copy()       # get copy of matrix
        new_plot = plot.copy()          # make copy of copy
        b_val = 0                       # set break value to 0

        # loop through each position in plot matrix
        for y, row in enumerate(plot):
            for x, point in enumerate(row):

                if point == 1:          # if point is 1...
                    # returns a list if points that make up the object outline as well as the max y,x and min y,x
                    out = get_object_outline(plot, new_plot, (y, x), 8, 1, 1)
                    ind_list = out[2]               # get list from output
                    ind_list += ind_list[0:2]       # add the first 2 stitches to the end of the list to close the gap
                    self.stitch_list = ind_list     # set object stitch_list using the output co-or list
                    b_val = 1                       # set break value to 1
                    break                           # break second loop
            if b_val == 1:  # if break value is equal to 1...
                break           # break first loop

    # sets stitch list to a list of co-ordinates that outline and circle the object until all points have been visited
    def running_stitch_fill(self, main):
        test = 0

        # console testing comment
        if test == 5:
            print("running_stitch_fill - class ObjectPlot - plot_objects.py")

        plot = self.matrix.copy()               # get copy of matrix
        new_plot = self.matrix.copy()           # get copy of copy
        b_val = 0                               # set break value to 0
        count = 4                               # set count to 4

        # loop through plot matrix
        for y, row in enumerate(plot):
            for x, point in enumerate(row):

                if point == 1:  # if point is equal to 1...

                    # returns a list if points that make up the object outline as well as the max y,x and min y,x
                    max_yx, min_yx, ind_list = get_object_outline(plot, new_plot, (y, x), 8, count, 1)

                    # checks for any valid point in point, returns the top left most if available
                    anw, yx = check_for_number(new_plot, 1)

                    # variant on of the get_object_outline function expect this keeps circling until object is filled
                    ind_list = get_object_outline_fill(main, plot, new_plot, yx, 8, count, 1, ind_list)

                    self.stitch_list = ind_list     # set stitch list
                    b_val = 1                       # set break value
                    break                           # break second loop

            if b_val == 1:  # if break value is equal to 1...
                break           # break first loop

    # sets stitch list to a list generated by a fill pattern - vertical and horizontal stitch sets combined into one
    def fill_stitch_fill(self, main):
        test = 0
        # console testing comment
        if test == 5:
            print("fill_stitch_fill - class ObjectPlot - plot_objects.py")

        plot = self.matrix.copy()           # get matrix copy

        # console testing comment
        if test == 1:
            print("fill stitch fill")
            print_plot_advanced(plot)

        ref_plot = self.ref_plot.copy()     # get copy of reference plot
        min_yx = (0, 0)                     # set min y,x to the lowest
        max_yx = (len(plot), len(plot[0]))  # set max y,x to the highest
        br_val = 0                          # set break value to 0
        ind_list = []                       # create int_list
        end_at = 0                          # set end_at value to 0

        p_row = ["0"] * len(ref_plot[0])    # create blank plot to make template plot
        blank_plot = np.array([p_row] * len(ref_plot))
        template = blank_plot.copy()    

        # loop through template plot - create skip a column template plot
        for y, row in enumerate(template):
            for x, point in enumerate(row):
                if (x % 2) == 0:            # if x divided by 2 has no remainder...- every other column
                    template[y, x] = "2"        # set template[y, x] equal to 2

        # console testing comment
        if test == 1:
            print_plot_advanced(template)
            print(" ")
            print_plot_advanced(plot)

        # loop through plot - set outline point in ind_list and get min_x for start point
        for y, row in enumerate(plot):
            for x, point in enumerate(row):

                if point == 1:  # if point is equal to 1...

                    # get object outline starting at point
                    max_yx, min_yx, ind_list = get_object_outline(plot, ref_plot, (y, x), 8, 3, 1)
                    br_val = 1      # set break value to 1
                    break           # break second loop

            if br_val == 1:     # if break value is equal to 1...
                break               # break first loop

        min_y, min_x = min_yx   # get minimum y value and minimum x value from min_yx

        # console testing comment
        if test == 1:
            print("before min_yx: {}".format(min_yx))
            print("after min_x: {}".format(min_x))

        # loop through plot rows - get start point by finding valid point that matches both template and plot
        for y, row in enumerate(plot):
            p_a = row[min_x]
            p_b = row[min_x + 1]
            tem_p_a = template[y, min_x]
            tem_p_b = template[y, min_x + 1]

            # console testing comment
            if test == 1:
                print("y: {} plot val: {}".format(y, p_a))

            if p_a == 1 and tem_p_a == "2":     # if point a is equal to 1 and template point a is equal to 2...
                end_at = (y, min_x)                 # set end_at value
                break
            elif p_b == 1 and tem_p_b == "2":   # if point b is equal to 1 and template point b is equal to 2...
                end_at = (y, min_x + 1)             # set end_at value
                break
            else:                               # else if point a and b are not 1 and template a and b are not 2...
                # console testing comment
                if test == 1:
                    print("not set")

        start_at = ind_list[-1]     # set start at point

        # console testing comment
        if test == 1:
            print(ind_list)
            print("Start Val: {}".format(end_at))
            print("end Point: {}".format(start_at))

        if end_at == start_at:      # if end at point and start at point are equal...
            pass
        else:                       # else if end at point and start at point are not equal...

            # creates list of point between 2 given points - list between end of outline and start of full fill
            goto, ind_list = asp.move_to_a_star(main, plot, end_at, start_at, ind_list)

        # creates a list of points that systematically visits and records each valid point in the object
        ind_list = get_object_fill_stitch(main, template, plot, end_at, max_yx, min_yx, ind_list)

        self.stitch_list = ind_list     # set stitch list


# create a list of points that are on the outer edge of the object
def get_object_outline(main_plot, ref_plot, start_yx, start_point, set_to, col_num):
    test = 0

    # console testing comment
    if test == 5:
        print("get_object_outline - plot_objects.py")
    elif test == 2:
        print("COL_NUM: {}".format(col_num))

    plot = main_plot            # set passed plot as plot
    y, x = start_yx             # set y and x from start_yx
    l_point = start_point       # set last point from passed start point
    ind_list = []               # create index list
    plot_h = len(ref_plot)      # set plot height
    plot_w = len(ref_plot[0])   # set plot width

    bol = isinstance(ref_plot[0, 0], str)   # check if reference plot is made of string characters

    if bol:     # if reference plot is made of string character...
        set_to = str(set_to)    # set set_to as a string variable

    ref_plot[y, x] = set_to     # set start point in the plot
    ind_list.append((y, x))     # append start point to index list

    count = 0                   # set count to 0
    ext = 0                     # set ext to 0
    while ext != 1:             # while loop using ext variable

        # One - Top Left
        if l_point == 8:        # if previous point was position 8...

            # console testing comment
            if test == 1:
                print("# One")

            if y - 1 >= 0 and x - 1 >= 0:   # if potential point will be within the plot...
                n_point = plot[y - 1, x - 1]    # set new point with the plot points value

                if n_point == col_num:          # if new points value is the same as the colour number...
                    pon_a = plot[y, x - 1]          # get point a - Left of current point, Below new point
                    pon_b = plot[y - 1, x]          # get point b - Above current point, Right of new point

                    if pon_a == pon_b:  # if point a and b are the same...- testing to see if new point is a valid move

                        # console testing comment
                        if test == 2:
                            print("1 can't go equal points pon_a: {} pon_b: {}".format(pon_a, pon_b))

                        # if a and b are the same they could be part of a line
                        # if the line cuts off new point from current point then new point is not valid
                        # on the other hand if new point an current point are the line,
                        # they could be cutting off point a and b making new point a valid move

                        # get points in a 5x5 grid surrounding new point - returns list of values & list of co_ordinates
                        points, yx_points = get_surrounding_points_5x5(plot, y - 1, x - 1)

                        # counts how many time each value appears in value list - return values and amounts
                        val_list, amount_list = count_list(points)

                        # determines whether new point is a valid move or not
                        anw = t_w_p_logic(col_num, pon_a, val_list, amount_list)

                        if anw == 1:    # if answer is equal to 1...- new point is a valid move

                            # set new point section
                            y -= 1  # set new y
                            x -= 1  # set new x

                            ref_plot[y, x] = set_to     # set point in reference plot to set_to value
                            ind_list.append((y, x))     # append point y,x to  index list
                            l_point = 5                 # set last point to 5 - Bottom Right - direction travelled from

                            # console testing comment
                            if test == 1 or test == 2:
                                print("Che 1 Set ({},{})".format(y, x))

                    else:               # else if a and b are not equal...
                        if (y - 1, x - 1) == ind_list[0]:   # if new point equals start point...
                            break                               # break while loop

                        else:                               # else if new point is not start point...

                            # set new point section
                            y -= 1  # set new y
                            x -= 1  # set new x

                            ref_plot[y, x] = set_to  # set point in reference plot to set_to value
                            ind_list.append((y, x))  # append point y,x to  index list
                            l_point = 5  # set last point to 5 - Bottom Right - direction travelled from

                            # console testing comment
                            if test == 1 or test == 2:
                                print("Pos 1 Set ({},{})".format(y, x))

            if l_point != 5:    # if last point is not 5... - if the  new point was not set and instead skipped...
                l_point = 1         # set last point to 1 - the next point in a clockwise direction - Top

        # Two - Top
        elif l_point == 1:  # if previous point was position 1...

            # console testing comment
            if test == 1:
                print("# Two")

            if y - 1 >= 0:  # if potential point will be within the plot...
                n_point = plot[y - 1, x]    # set new point with the plot points value

                if n_point == col_num:  # if new points value is the same as the colour number...

                    if (y - 1, x) == ind_list[0]:   # if new point equals start point...
                        break                           # break while loop
                    else:   # else if new point is not start point...

                        # set new point section
                        y -= 1                      # set new y
                        ref_plot[y, x] = set_to     # set point in reference plot to set_to value
                        ind_list.append((y, x))     # append point y,x to  index list
                        l_point = 6                 # set last point to 6 - Bottom - direction travelled from

                        # console testing comment
                        if test == 1 or test == 2:
                            print("Pos 2 Set ({},{})".format(y, x))

            if l_point != 6:    # if last point is not 6... - if the  new point was not set and instead skipped...
                l_point = 2          # set last point to 2 - the next point in a clockwise direction - Top Right

        # Three - Top Right
        elif l_point == 2:  # if previous point was position 2...

            # console testing comment
            if test == 1:
                print("# Three")

            if y - 1 >= 0 and x + 1 < len(plot[0]):     # if potential point will be within the plot...
                n_point = plot[y - 1, x + 1]                # set new point with the plot points value

                if n_point == col_num:      # if new points value is the same as the colour number...
                    pon_a = plot[y, x + 1]      # get point a - Right of current point, Below new point
                    pon_b = plot[y - 1, x]      # get point b - Above current point, Left of new point

                    if pon_a == pon_b:  # if point a and b are the same...- testing to see if new point is a valid move

                        # console testing comment
                        if test == 1 or test == 2:
                            print("3 can't go")

                        # if a and b are the same they could be part of a line
                        # if the line cuts off new point from current point then new point is not valid
                        # on the other hand if new point an current point are the line,
                        # they could be cutting off point a and b making new point a valid move

                        # get points in a 5x5 grid surrounding new point - returns list of values & list of co_ordinates
                        points, yx_points = get_surrounding_points_5x5(plot, y - 1, x + 1)

                        # counts how many time each value appears in value list - return values and amounts
                        val_list, amount_list = count_list(points)

                        # determines whether new point is a valid move or not
                        anw = t_w_p_logic(col_num, pon_a, val_list, amount_list)

                        if anw == 1:    # if answer is equal to 1...- new point is a valid move

                            # set new point section
                            y -= 1  # set new y
                            x += 1  # set new x

                            ref_plot[y, x] = set_to     # set point in reference plot to set_to value
                            ind_list.append((y, x))     # append point y,x to  index list
                            l_point = 7                 # set last point to 7 - Bottom Left - direction travelled from

                            if test == 1 or test == 2:  # testing console comments
                                print("Che 3 Set ({},{})".format(y, x))

                    else:   # else if a and b are not equal...
                        if (y - 1, x + 1) == ind_list[0]:   # if new point equals start point...
                            break                               # break while loop

                        else:                               # else if new point is not start point...

                            # set new point section
                            y -= 1  # set new y
                            x += 1  # set new x

                            ref_plot[y, x] = set_to     # set point in reference plot to set_to value
                            ind_list.append((y, x))     # append point y,x to  index list
                            l_point = 7                 # set last point to 7 - Bottom Left - direction travelled from

                            # console testing comment
                            if test == 1 or test == 2:
                                print("Pos 3 Set ({},{})".format(y, x))

            if l_point != 7:    # if last point is not 7... - if the  new point was not set and instead skipped...
                l_point = 3         # set last point to 3 - the next point in a clockwise direction - Right

        # Four - Right
        elif l_point == 3:  # if previous point was position 3...

            # console testing comment
            if test == 1:
                print("# Four")

            if x + 1 < len(plot[0]):        # if potential point will be within the plot...
                n_point = plot[y, x + 1]        # set new point with the plot points value

                if n_point == col_num:      # if new points value is the same as the colour number...

                    if (y, x + 1) == ind_list[0]:   # if new point equals start point...
                        break                           # break while loop

                    else:                           # else if new point is not start point...

                        # set new point section
                        x += 1                      # set new x
                        ref_plot[y, x] = set_to     # set point in reference plot to set_to value
                        ind_list.append((y, x))     # append point y,x to  index list
                        l_point = 8                 # set last point to 8 - Left - direction travelled from

                        # console testing comment
                        if test == 1 or test == 2:
                            print("Pos 4 Set ({},{})".format(y, x))

            if l_point != 8:    # if last point is not 8... - if the  new point was not set and instead skipped...
                l_point = 4         # set last point to 4 - the next point in a clockwise direction - Bottom Right

        # Five - Bottom Right
        elif l_point == 4:  # if previous point was position 4...

            # console testing comment
            if test == 1:
                print("# Five")

            if y + 1 < len(plot) and x + 1 < len(plot[0]):  # if potential point will be within the plot...
                n_point = plot[y + 1, x + 1]                    # set new point with the plot points value

                if n_point == col_num:      # if new points value is the same as the colour number...
                    pon_a = plot[y, x + 1]      # get point a - Right of current point, Above new point
                    pon_b = plot[y + 1, x]      # get point b - Below current point, Left of new point

                    if pon_a == pon_b:  # if point a and b are the same...- testing to see if new point is a valid move

                        # console testing comment
                        if test == 1 or test == 2:
                            print("5 can't go equal points pon_a: {} pon_b: {}".format(pon_a, pon_b))

                        # get points in a 5x5 grid surrounding new point - returns list of values & list of co_ordinates
                        points, yx_points = get_surrounding_points_5x5(plot, y + 1, x + 1)

                        # counts how many time each value appears in value list - return values and amounts
                        val_list, amount_list = count_list(points)

                        # determines whether new point is a valid move or not
                        anw = t_w_p_logic(col_num, pon_a, val_list, amount_list)

                        if anw == 1:    # if answer is equal to 1...- new point is a valid move

                            # set new point section
                            y += 1                      # set new y
                            x += 1                      # set new x
                            ref_plot[y, x] = set_to     # set point in reference plot to set_to value
                            ind_list.append((y, x))     # append point y,x to  index list
                            l_point = 1                 # set last point to 1 - Top Left - direction travelled from

                            # console testing comment
                            if test == 1 or test == 2:
                                print("Che 5 Set ({},{})".format(y, x))

                    else:               # else if a and b are not equal...
                        if (y + 1, x + 1) == ind_list[0]:   # if new point equals start point...
                            break                               # break while loop

                        else:           # else if a and b are not equal...

                            # set new point section
                            y += 1                      # set new y
                            x += 1                      # set new x
                            ref_plot[y, x] = set_to     # set point in reference plot to set_to value
                            ind_list.append((y, x))     # append point y,x to  index list
                            l_point = 1                 # set last point to 1 - Top Left - direction travelled from

                            if test == 1 or test == 2:  # testing console comments
                                print("Pos 5 Set ({},{})".format(y, x))
            if l_point != 1:    # if last point is not 1... - if the  new point was not set and instead skipped...
                l_point = 5         # set last point to 5 - the next point in a clockwise direction - Bottom

        # Six - Bottom
        elif l_point == 5:  # if previous point was position 5...

            # console testing comment
            if test == 1:
                print("# Six")

            if y + 1 < len(plot):           # if potential point will be within the plot...
                n_point = plot[y + 1, x]        # set new point with the plot points value

                if n_point == col_num:          # if new points value is the same as the colour number...

                    if (y + 1, x) == ind_list[0]:   # if new point equals start point...
                        break                           # break while loop
                    else:                       # else if new point is not start point...

                        # set new point section
                        y += 1                      # set new y
                        ref_plot[y, x] = set_to     # set point in reference plot to set_to value
                        ind_list.append((y, x))     # append point y,x to  index list
                        l_point = 2                 # set last point to 2 - Top - direction travelled from

                        # console testing comment
                        if test == 1 or test == 2:
                            print("Pos 6 Set ({},{})".format(y, x))

            if l_point != 2:    # if last point is not 2... - if the  new point was not set and instead skipped...
                l_point = 6         # set last point to 6 - the next point in a clockwise direction - Bottom Left

        # Seven - Bottom Left
        elif l_point == 6:  # if previous point was position 6...

            # console testing comment
            if test == 1:
                print("# Seven")

            if y + 1 < len(plot) and x - 1 >= 0:    # if potential point will be within the plot...
                n_point = plot[y + 1, x - 1]            # set new point with the plot points value

                if n_point == col_num:      # if new points value is the same as the colour number...
                    pon_a = plot[y, x - 1]      # get point a - Left of current point, Above new point
                    pon_b = plot[y + 1, x]      # get point b - Below current point, Right of new point

                    if pon_a == pon_b:  # if point a and b are the same...- testing to see if new point is a valid move

                        # console testing comment
                        if test == 1 or test == 2:
                            print("7 can't go")

                        # if a and b are the same they could be part of a line
                        # if the line cuts off new point from current point then new point is not valid
                        # on the other hand if new point an current point are the line,
                        # they could be cutting off point a and b making new point a valid move

                        # get points in a 5x5 grid surrounding new point - returns list of values & list of co_ordinates
                        points, yx_points = get_surrounding_points_5x5(plot, y + 1, x - 1)

                        # counts how many time each value appears in value list - return values and amounts
                        val_list, amount_list = count_list(points)

                        # determines whether new point is a valid move or not
                        anw = t_w_p_logic(col_num, pon_a, val_list, amount_list)

                        if anw == 1:    # if answer is equal to 1...- new point is a valid move

                            # set new point section
                            y += 1                      # set new y
                            x -= 1                      # set new x
                            ref_plot[y, x] = set_to     # set point in reference plot to set_to value
                            ind_list.append((y, x))     # append point y,x to  index list
                            l_point = 3                 # set last point to 3 - Top Right - direction travelled from

                            # console testing comment
                            if test == 1 or test == 2:
                                print("Che 7 Set ({},{})".format(y, x))

                    else:   # else if a and b are not equal...
                        if (y + 1, x - 1) == ind_list[0]:   # if new point equals start point...
                            break                               # break while loop

                        else:                               # else if new point is not start point...

                            # set new point section
                            y += 1                      # set new y
                            x -= 1                      # set new x
                            ref_plot[y, x] = set_to     # set point in reference plot to set_to value
                            ind_list.append((y, x))     # append point y,x to  index list
                            l_point = 3                 # set last point to 3 - Top Right - direction travelled from

                            # console testing comment
                            if test == 1 or test == 2:
                                print("Pos 7 Set ({},{})".format(y, x))

            if l_point != 3:    # if last point is not 3... - if the  new point was not set and instead skipped...
                l_point = 7         # set last point to 7 - the next point in a clockwise direction - Bottom Left

        # Eight - Left
        elif l_point == 7:  # if previous point was position 7...

            # console test comment
            if test == 1:
                print("# Eight")

            if x - 1 >= 0:                  # if potential point will be within the plot...
                n_point = plot[y, x - 1]        # set new point with the plot points value

                if n_point == col_num:          # if new points value is the same as the colour number...

                    if (y, x - 1) == ind_list[0]:   # if new point equals start point...
                        break                           # break while loop

                    else:                           # else if new point is not start point...

                        # set new point section
                        x -= 1                      # set new x
                        ref_plot[y, x] = set_to     # set point in reference plot to set_to value
                        ind_list.append((y, x))     # append point y,x to  index list
                        l_point = 4                 # set last point to 4 - Right - direction travelled from

                        # console testing comment
                        if test == 1 or test == 2:
                            print("Pos 8 Set ({},{})".format(y, x))

            if l_point != 4:    # if last point is not 4... - if the new point was not set and instead skipped...
                l_point = 8         # set last point to 8 - the next point in a clockwise direction - Top Left

        # infinite loop exit
        if count > len(main_plot)*len(main_plot[0])*10:
            ext = 1
        count += 1

    max_y = 0       # set max y to lowest value
    min_y = plot_h  # set min y to highest value
    max_x = 0       # set max x to lowest value
    min_x = plot_w  # set min x to highest value

    # loop index list - set maximum y,x and minimum y,x
    for k in ind_list:
        y, x = k        # y, x set from co-ordinate

        if max_y < y:   # if the new y value is larger than the current max y...
            max_y = y       # set new y as max y
        if max_x < x:   # if the new x value is larger than the current max x...
            max_x = x       # set new x as max x
        if min_y > y:   # if the new y value is smaller than the current min y...
            min_y = y       # set new y as min y
        if min_x > x:   # if the new x value is smaller than the current min x...
            min_x = x       # set new x a s min x

    # console testing comment
    if test == "mxy":
        print("{} < y > {} {} < x > {}".format(min_y, max_y, min_x, max_x))
        print(ind_list)

    max_yx = (max_y, max_x)     # create max_yx using maximum y value and maximum x value
    min_yx = (min_y, min_x)     # create max_yx using minimum y value and minimum x value

    return max_yx, min_yx, ind_list


def get_object_outline_fill(main, main_plot, ref_plot, start_yx, start_point, set_to, col_num, ind_list):
    test = 0

    # console testing comment
    if test == 5:
        print("get_object_outline_fill - plot_objects.py")

    msg_count = 0

    # progress bar update
    if main is not None:
        msg = "Getting Running Fill...(Points Set: " + str(msg_count) + ")"
        main.bar_update_message(msg)
    # end

    ref_plot = ref_plot.copy()      # get reference plot copy
    plot = main_plot.copy()         # get main plot copy
    y, x = start_yx                 # set y and x using start_yx
    l_point = start_point           # set last point using stat point
    ind_list = ind_list             # pass index list

    # console testing comment
    if test == 1:
        print(ind_list)

    # console testing comment
    if test == 2:
        print("COL_NUM: {}".format(col_num))

    bol = isinstance(ref_plot[0, 0], str)   # check if reference plot is made up of string characters

    if bol:                 # if reference plot is made of string character...
        set_to = str(set_to)    # make set_to a string variable

    if ref_plot[y, x] == 1:     # if reference plot
        ref_plot[y, x] = set_to     # setting start point
        ind_list.append((y, x))     # setting start point in list

        # console testing comment
        if test == 1:
            print("First Set ({},{})".format(y, x))

    # console testing comment
    if test == 1:
        print("plot")
        print_plot(plot)
        print("ref")
        print_plot(ref_plot)

    ext = 0  # set ext value to 0
    loop = 0  # set loop value to 0
    while ext != 1:

        # One - Top Left
        if l_point == 8:    # check loop start

            # console testing comment
            if test == 1:
                print("# One")

            if y - 1 >= 0 and x - 1 >= 0:       # check if this point is within the plot limits
                n_point = ref_plot[y - 1, x - 1]    # set new point

                if n_point == col_num:       # check against colour_number

                    # set new point section
                    y -= 1                      # set y to y - 1
                    x -= 1                      # set x to x - 1
                    ref_plot[y, x] = set_to     # set point
                    ind_list.append((y, x))     # add point to list
                    loop = 0                    # reset loop check value
                    l_point = 5                 # set loop start for next point

                    # console testing comment
                    if test == 1 or test == 2:
                        print("Pos 1 Set ({},{})".format(y, x))
                    msg_count += 1

            if l_point != 5:    # check if loop start was set
                l_point = 1     # if not, set to the next position

        # Two - Top
        elif l_point == 1:  # check loop start
            if test == 1:   # testing console comments
                print("# Two")

            if y - 1 >= 0:  # check if this point is within the plot limits
                n_point = ref_plot[y - 1, x]    # set new point

                if n_point == col_num:  # check against colour_number

                    # set new point section
                    y -= 1                      # set y to y - 1
                    ref_plot[y, x] = set_to     # set point
                    ind_list.append((y, x))     # add point to list
                    loop = 0                    # reset loop check value
                    l_point = 6                 # set loop start for next point

                    # console testing comment
                    if test == 1 or test == 2:
                        print("Pos 2 Set ({},{})".format(y, x))
                    msg_count += 1

            if l_point != 6:    # check if loop start was set
                l_point = 2     # if not, set to the next position

        # Three - Top Right
        elif l_point == 2:  # check if this point is within the plot limits
            if test == 1:   # set this point
                print("# Three")

            if y - 1 >= 0 and x + 1 < len(plot[0]):     # check if this point is within the plot limits
                n_point = ref_plot[y - 1, x + 1]    # set new point

                if n_point == col_num:      # check against colour_number

                    # set new point section
                    y -= 1                      # set y to y - 1
                    x += 1                      # set x to x + 1
                    ref_plot[y, x] = set_to     # set point
                    ind_list.append((y, x))     # add point to list
                    loop = 0                    # reset loop check value
                    l_point = 7                 # set loop start for next point

                    # console testing comment
                    if test == 1 or test == 2:
                        print("Pos 3 Set ({},{})".format(y, x))
                    msg_count += 1

            if l_point != 7:    # check if loop start was set
                l_point = 3     # if not, set to the next position

        # Four - Right
        elif l_point == 3:  # check loop start
            if test == 1:   # testing console comments
                print("# Four")

            if x + 1 < len(plot[0]):        # check if this point is within the plot limits
                n_point = ref_plot[y, x + 1]    # set this point

                if n_point == col_num:  # check against colour_number

                    # set new point section
                    x += 1                      # set x to x + 1
                    ref_plot[y, x] = set_to     # set point
                    ind_list.append((y, x))     # add point to list
                    loop = 0                    # reset loop check value
                    l_point = 8                 # set loop start for next point

                    if test == 1 or test == 2:   # testing console comments
                        print("Pos 4 Set ({},{})".format(y, x))
                    msg_count += 1

            if l_point != 8:    # check if loop start was set
                l_point = 4     # if not, set to the next position

        # Five - Bottom Right
        elif l_point == 4:  # check loop start
            if test == 1:   # testing console comments
                print("# Five")

            if y + 1 < len(plot) and x + 1 < len(plot[0]):  # check if this point is within the plot limits
                n_point = ref_plot[y + 1, x + 1]    # set this point

                if n_point == col_num:      # check against colour_number

                    # set new point section
                    y += 1                      # set y to y + 1
                    x += 1                      # set x to x + 1
                    ref_plot[y, x] = set_to     # set point
                    ind_list.append((y, x))     # add point to list
                    loop = 0                    # reset loop check value
                    l_point = 1                 # set loop start for next point

                    if test == 1 or test == 2:   # testing console comments
                        print("Pos 5 Set ({},{})".format(y, x))
                    msg_count +=1

            if l_point != 1:    # check if loop start was set
                l_point = 5     # if not, set to the next position

        # Six - Bottom
        elif l_point == 5:  # check loop start
            if test == 1:   # testing console comments
                print("# Six")

            if y + 1 < len(plot):    # check if this point is within the plot limits
                n_point = ref_plot[y + 1, x]    # set this point

                if n_point == col_num:  # check against colour_number

                    # set new point section
                    y += 1                      # set y to y + 1
                    ref_plot[y, x] = set_to     # set point
                    ind_list.append((y, x))     # add point to list
                    loop = 0                    # reset loop check value
                    l_point = 2                 # set loop start for next point

                    if test == 1 or test == 2:   # testing console comments
                        print("Pos 6 Set ({},{})".format(y, x))
                    msg_count += 1

            if l_point != 2:    # check if loop start was set
                l_point = 6     # if not, set to the next position

        # Seven - Bottom Left
        elif l_point == 6:  # check loop start
            if test == 1:   # testing console comments
                print("# Seven")

            if y + 1 < len(plot) and x - 1 >= 0:    # check if this point is within the plot limits
                n_point = ref_plot[y + 1, x - 1]     # set this point

                if n_point == col_num:      # check against colour_number

                    # set new point section
                    y += 1                      # set y to y + 1
                    x -= 1                      # set x to x - 1
                    ref_plot[y, x] = set_to     # set point
                    ind_list.append((y, x))     # add point to list
                    loop = 0                    # reset loop check value
                    l_point = 3                 # set loop start for next point

                    # console testing comment
                    if test == 1 or test == 2:
                        print("POS 7 Set ({},{})".format(y, x))
                    msg_count += 1

            if l_point != 3:    # check if loop start was set
                l_point = 7     # if not, set to the next position

        # Eight - Left
        elif l_point == 7:  # check loop start
            if test == 1:   # testing console comments
                print("# Eight")

            if x - 1 >= 0:  # check if this point is within the plot limits
                n_point = ref_plot[y, x - 1]    # set this point

                if n_point == col_num:  # check against colour_number

                    # set new point section
                    x -= 1                      # set x to x - 1
                    ref_plot[y, x] = set_to     # set point
                    ind_list.append((y, x))     # add point to list
                    loop = 0                    # reset loop check value
                    l_point = 4                 # set loop start for next point

                    # console testing comment
                    if test == 1 or test == 2:
                        print("Pos 8 Set ({},{})".format(y, x))

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

        if loop > 16:   # infinite loop exit - if loops through all positions twice

            # console testing comment
            if test == 1 or test == 2:
                print("trapped")

            # checks if there are valid numbers left in plot - returns boolean and Top Left most valid point
            bol, yx = check_for_number(ref_plot, 1)

            if bol:     # if boolean is true...

                # return list of points between start point and go to point
                yx, ind_list = asp.move_to_a_star(main, plot, yx, ind_list[-1], ind_list)

                y, x = yx   # get y, x from yx

                # console test comment
                if test == 1:
                    print("OF Move_to Set ({},{})".format(y, x))

                ref_plot[y, x] = set_to     # set new point on reference plot
                loop = 0                    # set loop to 0

            else:       # else if boolean is false...

                # console testing comment
                if test == 1:
                    print("Exit")

                ext = 1     # set ext value

        loop += 1   # counts the number of loops without a point being set

    # console test comment
    if test == 1:
        print_plot(ref_plot)

    return ind_list


def get_object_fill_stitch(main, template, plot, start_yx, max_yx, min_yx, ind_list):
    test = 0

    # console test comment
    if test == 5:
        print("get_object_fill_stitch - plot_objects.py")

    msg_count = 0   # set message count to 0

    # progress bar update
    if main is not None:

        msg = "Getting Fill Base...(Points Set: " + str(msg_count) + ")"
        main.bar_update_message(msg)
    # end

    s_y, s_x = start_yx     # set start y and start x using start yx
    y = s_y                 # set y using start y
    x = s_x                 # set x using start x
    direct = 1              # set starting direction as 1
    ext = 0                 # set ext value as 0
    plot_c = plot.copy()    # get copy of plot
    max_y, max_x = max_yx   # set maximum y and maximum x using max yx
    min_y, min_x = min_yx   # set minimum y and minimum x using min yx

    # console testing comment
    if test == 1 or test == 2:
        print(ind_list)
        print("Fill Part 1")

    while ext != 1:     # vertical spaced stitches

        template[y, x] = "1"    # set current point in template to string 1

        # Down Direction - Move down until end of object is reached
        if direct == 1:     # if direction is equal to 1

            # console testing comment
            if test == 1:
                print("# Down")

            a = y + 1        # set a

            if y + 1 < len(plot_c) and plot_c[a, x] == 1:       # if down is a valid move
                y = a                                               # set new y
                template[y, x] = "1"                                # set current point in template
                ind_list.append((y, x))                             # add co-or to list

                # console test comment
                if test == 2:
                    print("D Set: ({},{})". format(y, x))

                msg_count += 1

            else:                                               # else if not set direction var to 2
                direct = 2

        # Right 1 Direction - Move right one space until next valid template point is reached
        elif direct == 2:   # if direction is equal to 2

            # console testing comment
            if test == 1:
                print("# Right 1")

            a = y + 1       # set a
            b = x + 1       # set b
            c = y - 1       # set c

            # console testing comment
            if test == 1:
                print(max_x, " ", b)

            if b > max_x:       # if b is greater than the maximum edge value...

                # compare template plot and plot
                new_plot = compare_plots(plot_c, 1, template, "2")

                # console test comment
                if test == 2:
                    print_plot(new_plot)

                # check for valid points left in new_plot
                anw, yx = check_for_number(new_plot, "1")

                if anw:     # if answer is true...

                    # create a list of co-ordinates from start point to go to point
                    yx, ind_list = asp.move_to_a_star(main, plot_c, yx, ind_list[-1], ind_list)  # run move_to

                    y, x = yx       # set y and x using yx
                    direct = 1      # set direction to 1

                else:
                    ext = 1  # if false, all areas have been visited, exit while loop

            # if position 5 - Bottom Right in relation to current x, y
            elif y + 1 < len(plot_c) and plot_c[a, b] == 1:

                # console testing comment
                if test == 1:
                    print("Pos 5")

                if template[a, b] == "1":  # hit already completed section
                    new_plot = compare_plots(plot_c, 1, template, "2")

                    # console testing comment
                    if test == 2:
                        print_plot(new_plot)

                    anw, yx = check_for_number(new_plot, "1")  # check if any uncompleted parts left

                    if anw:  # if true
                        yx, ind_list = asp.move_to_a_star(main, plot_c, yx, ind_list[-1], ind_list)  # run move_to
                        y, x = yx
                        direct = 1
                    else:
                        ext = 1  # if false, all areas have been visited, exit while loop

                else:                       # else section point

                    y = a                       # set new y
                    x = b                       # set new x
                    ind_list.append((y, x))     # append co-ordinates to index list

                    msg_count += 1

                    # console testing comment
                    if test == 2:
                        print("Pos 5 Set: ({},{})".format(y, x))

                    j = 0
                    while j != 1:   # to the end of the line

                        if x + 1 < len(template[0]) and template[y, x + 1] == "1":  # if x + 1 is within plot and is 1
                            break       # end of the line reached

                        elif y + 1 < len(plot_c) and plot_c[y + 1, x] != 0:     # if y + 1 is within plot and is not 0
                            y = y + 1                   # set new y
                            ind_list.append((y, x))     # append co-ordinates to index list

                            # console testing comment
                            if test == 2:
                                print("Por 5 Set: ({},{})".format(y, x))

                            msg_count += 1

                        else:
                            j = 1

                        if y + 1 >= len(plot_c):
                            direct = 3
                        elif plot_c[y + 1, x] == 0 and template[y + 1, x] == "2":
                            direct = 3

                    # look at the next 2's column

            # if position 4 - Right in relation to current x, y
            elif plot_c[y, b] == 1:

                # console testing comment
                if test == 1:
                    print("Pos 4")

                if template[y, b] == "1":  # hit already completed section
                    new_plot = compare_plots(plot_c, 1, template, "2")

                    # console testing comment
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
                    x = x + 1                   # set new x
                    ind_list.append((y, x))     # append y,x to index list

                    msg_count += 1

                    # console testing comment
                    if test == 2:
                        print("Pos 4 Set: ({},{})".format(y, x))

                    # redo or move on - if current point in template is not 2, redo step. If it is 2 change direction
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

            # if position 3 - Top Right in relation to current x, y
            elif y - 1 >= 0 and plot_c[c, b] == 1:

                # console testing comment
                if test == 1:
                    print("Pos 3")

                if template[c, b] == "1":  # hit already completed section
                    new_plot = compare_plots(plot_c, 1, template, "2")

                    # console testing comment
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
                    y = c                       # set new y
                    x = b                       # set ne x
                    ind_list.append((y, x))     # append y,x to index list

                    msg_count += 1

                    # console testing comment
                    if test == 2:
                        print("Pos 3 Set: ({},{})".format(y, x))

                    # redo or move on - if current point in template is not 2, redo step. If it is 2 change direction
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
                # console testing comment
                if test == 1:
                    print("Else")

                if y - 1 >= 0 and plot_c[y-1, x] == 1:

                    y = y - 1                   # set new y
                    ind_list.append((y, x))     # append y,x to index list

                    msg_count += 1

                    # console testing comment
                    if test == 2:
                        print("Else  Set: ({},{})". format(y, x))

                else:
                    # console testing comment

                    if test == 2:
                        print("Else Right 1 move_to")
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

    # console testing comment
    if test == 5:
        print("compare_plots - plot_objects.py")

    p_row = ["0"] * len(plot1[0])  # create blank plot make template plot
    blank_plot = np.array([p_row] * len(plot1))

    # loop through plot1
    for y, row in enumerate(plot1):
        for x, point in enumerate(row):
            if point == val1 and plot2[y, x] == val2:   # if plot1 and plot2 point are equal to their values...
                blank_plot[y, x] = "1"                      # set blank plot

    return blank_plot


def find_path(main_plot, goto_yx, start_yx, ind_list):
    test = 0

    # console testing comment
    if test == 5:
        print("find_path - plot_objects.py")

    f_y, f_x = goto_yx  # get finish y and finish x from go to yx
    y, x = start_yx     # get y and x from start yx
    col_num = 1

    p_row = [1] * len(main_plot[0])  # create blank plot make template plot
    plot = np.array([p_row] * len(main_plot))

    if test == 1 or test == 2 or test == 3:
        print("test in find_path")
        asp.print_node_plot(main_plot)
        print_plot(plot)

    ext = 0

    h = 0
    l_point = next_point(start_yx, goto_yx)  # run next point to get the next potential position

    # console testing comment
    if test == 2 or test == 3:
        print("Start: {} GoTo: {}".format(start_yx, goto_yx))

    if start_yx == goto_yx:
        return h, ind_list

    while ext != 1:

        # One - Top Left
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

        # Two - Top
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

        # Three - Top Right
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

        # Four - Right
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

        # Five - Bottom Right
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

        # Six - Bottom
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

        # Seven - Bottom Left
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

        # Eight - Left
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

    # console testing comment
    if test == 5:
        print("next_point - plot_objects.py")

    start_p = 1     # set start point

    c_y, c_x = yx_st    # set current y and current x from start yx
    f_y, f_x = yx_fn    # set finish y and finish x from finish yx

    sum_y = f_y - c_y   # get difference between current y and finish y
    sum_x = f_x - c_x   # get difference between current x and finish x

    if sum_y < 0:           # if sum y is less than 0... - negative y value

        if sum_x < 0:           # if sum x is less than 0... - negative x value
            start_p = 1             # set start point as 1 - Position 1 - Top Left

        elif sum_x > 0:         # else if sum x is greater than 0... - positive x value
            start_p = 3             # set start point to 3 - Position 3 - Top Right

        else:                   # else if sum x is 0... - current x value
            start_p = 2             # set start point to 2 - Position 2 - Top

    elif sum_y > 0:         # else if sum y is greater than 0... - positive y value

        if sum_x < 0:           # if sum x is less than 0... - negative x value
            start_p = 7             # set start point to 7 - Position 7 - Bottom Left

        elif sum_x > 0:         # else if sum x is greater than 0... - positive x value
            start_p = 5             # set start point to 5 - Position 5 - Bottom Right

        else:                   # else if sum x is 0... - current x value
            start_p = 6             # set start point to 6 - Position 6 - Bottom

    elif sum_y == 0:        # else if sum y is 0... - current y value

        if sum_x < 0:           # if sum x is less than 0... - negative x value
            start_p = 8             # set start point to 8 - Position 8 - Left

        elif sum_x > 0:         # else if sum x is greater than 0... - positive x value
            start_p = 4             # set start point to 4 - Position 4 - Right

    return start_p


def reversible_mine_sweeper_fill(main_plot, ref_plot, max_yx, min_yx, set_to, col_num, arg):
    test = 0

    # console testing comment
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

    # console testing comment
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

                                # console testing comment
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
    return ref_plot


def check_for_number(plot, num):
    test = 0

    # console testing comment
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

    # console testing comment
    if test == 5:
        print("valid_position - class Plot - plot_objects.py")
    elif test == 1:
        print("Valid position check: ({},{})".format(y, x))
        print("col_num Value: {}".format(col_num))

    # gets surrounding points in 5x5 grid and returns list
    points, yx_points = get_surrounding_points_5x5(main_plot, y, x)

    # counts amount unique colours in list, counts how many time each colour appears in the list
    val_list, amount_list = count_list(points)

    # works out if the current colour is part of a line or part of a solid shape.
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

    # console testing comment
    if test == 1:
        print("Centre: ({},{})".format(y, x))

    if y > 0:
        p_a = plot[y - 1, x]
        points.append(out_plot[a, x])

        # console testing comment
        if test == 1:
            print(" Sur_2: ({},{})".format(a, x))

        if x > 0:
            p_c = plot[y, x - 1]
            if p_a != p_c:
                points.append(out_plot[a, c])

                # console testing comment
                if test == 1:
                    print(" Sur_1: ({},{})".format(a, c))

            elif p_a == p_c and p_a != col_num:  # and out_plot[a, c] == out_plot[y, x]:
                anw = valid_position(plot, y - 1, x - 1, col_num, p_a)
                if anw == 1:
                    points.append(out_plot[a, c])

                    # console testing comment
                    if test == 1:
                        print(" Sur_1: ({},{})".format(a, c))

                else:

                    # console testing comment
                    if test == 1:
                        print("({},{}) not valid".format(a, c))
            elif p_a == p_c and p_a == col_num:
                points.append(out_plot[a, c])

        if x < cul_num - 1:
            p_d = plot[y, x + 1]
            if p_a != p_d:
                points.append(out_plot[a, d])

                # console testing comment
                if test == 1:
                    print(" Sur_3: ({},{})".format(a, d))

            elif p_a == p_d and p_a != col_num:  # and out_plot[a, d] == out_plot[y, x]:
                anw = valid_position(plot, y - 1, x + 1, col_num, p_a)
                if anw == 1:
                    points.append(out_plot[a, d])

                    # console testing comment
                    if test == 1:
                        print(" Sur_3: ({},{})".format(a, d))
                else:
                    # console testing comment
                    if test == 1:
                        print("({},{}) not valid".format(a, d))
            elif p_a == p_d and p_a == col_num:
                points.append(out_plot[a, d])

    if y < row_num - 1:
        p_b = plot[y + 1, x]
        points.append(out_plot[b, x])

        # console testing comment
        if test == 1:
            print(" Sur_6: ({},{})".format(b, x))

        if x > 0:
            p_c = plot[y, x - 1]
            if p_b != p_c:
                points.append(out_plot[b, c])

                # console testing comment
                if test == 1:
                    print(" Sur_7: ({},{})".format(b, c))

            elif p_b == p_c and p_b != col_num:  # and out_plot[b, c] == out_plot[y, x]:
                anw = valid_position(plot, y + 1, x - 1, col_num, p_b)
                if anw == 1:
                    points.append(out_plot[b, c])

                    # console testing comment
                    if test == 1:
                        print(" Sur_7: ({},{})".format(b, c))
                else:
                    # console testing comment
                    if test == 1:
                        print("({},{}) not valid".format(b, c))
            elif p_b == p_c and p_b == col_num:
                points.append(out_plot[b, c])

        if x < cul_num - 1:
            p_c = plot[y, x + 1]
            if p_b != p_c:
                points.append(out_plot[b, d])

                # console testing comment
                if test == 1:
                    print(" Sur_5: ({},{})".format(b, d))

            elif p_b == p_c and p_b != col_num:  # and out_plot[b, d] == out_plot[y, x]:
                anw = valid_position(plot, y + 1, x + 1, col_num, p_b)
                if anw == 1:
                    points.append(out_plot[b, d])

                    # console testing comment
                    if test == 1:
                        print(" Sur_5: ({},{})".format(b, d))
                else:
                    # console testing comment
                    if test == 1:
                        print("({},{}) not valid".format(b, d))
            elif p_b == p_c and p_b == col_num:
                points.append(out_plot[b, d])

    if x > 0:
        points.append(out_plot[y, c])

        # console testing comment
        if test == 1:
            print(" Sur_8: ({},{})".format(y, c))

    if x < cul_num - 1:
        points.append(out_plot[y, d])

        # console testing comment
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

    # console testing comment
    if test == 5:
        print("t_w_p_logic - class Plot - plot_objects.py")
    elif test == 1:
        print("** t_w_p_logic() console debug **")
        print("col_num: {} ".format(col_num))

    if col_num not in val_list:

        # console testing comment
        if test == 1:
            print("*** {} not in list".format(col_num))
        return 2
    else:
        ind = val_list.index(con_col)
        con_amount = amount_list[ind]
        ind = val_list.index(col_num)
        col_amount = amount_list[ind]

        if con_amount > col_amount:

            # console testing comment
            if test == 1:
                print("T_W_P Return: 1")
                print("** end **")

            return 1

        elif con_amount < col_amount:

            # console testing comment
            if test == 1:
                print("con_col is the line")

            return 2

        else:

            # console testing comment
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


# do not delete
def move_to(main_plot, goto_yx, start_yx, set_to, look_for, passed_ind_list):
    test = 5
    if test == 5:
        print("move_to - plot_objects.py")
    test = 2
    col_num = look_for  # value 1
    ref_plot = main_plot.copy()
    plot = main_plot.copy()    # untouched plot with just 0's and 1's
    plot_9 = main_plot.copy()
    bl_plot = main_plot.copy()
    f_y, f_x = goto_yx
    y, x = start_yx
    og_ind_list = passed_ind_list
    ind_list = []
    check = 0

    if test == 1 or test == 2 or test ==3:
        print("Move_to \n", og_ind_list)
        print_plot(main_plot)
        print_plot(plot)

    one = [1, 8, 2, 7, 3, 6, 4, 5]
    two = [2, 1, 3, 8, 4, 7, 5, 6]
    thr = [3, 2, 4, 1, 5, 8, 6, 7]
    fou = [4, 3, 5, 2, 6, 1, 7, 8]
    fiv = [5, 4, 6, 3, 7, 2, 8, 1]
    six = [6, 5, 7, 4, 8, 3, 1, 2]
    sev = [7, 6, 8, 5, 1, 4, 2, 3]
    eig = [8, 7, 1, 6, 2, 5, 4, 3]
    search_patterns = [one, two, thr, fou, fiv, six, sev, eig]

    ext = 0
    ind = 0
    loop_c = 0

    point_c = next_point(start_yx, goto_yx)
    s_pat = search_patterns[point_c - 1]

    if test == 2 or test == 3:
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

                        if test == 2:
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
                    if test == 2:
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
                # print("1: {}, cur: {}".format(n_point, col_num))
                if n_point == col_num:  # check against colour_number
                    pon_a = plot[y, x - 1]
                    pon_b = plot[y - 1, x]

                    if pon_a == pon_b and pon_a == set_to:

                        # plot_9[y - 1, x - 1] = 9
                        plot_9[y, x] = 0

                        if test == 2:
                            print("Set 0:({},{}) Set 9: ({},{})".format(y, x, y - 1, x - 1))
                            print_plot(plot_9)
                            print_plot(plot)

                        plot = plot_9.copy()
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

                        # plot_9[y - 1, x + 1] = 9
                        plot_9[y, x] = 0

                        if test == 2:
                            print("Set 0:({},{}) Set 9: ({},{})".format(y, x, y - 1, x + 1))
                            print_plot(plot_9)
                            print_plot(plot)

                        plot = plot_9.copy()

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

                        plot_9[y, x] = 0

                        if test == 2:
                            print("Set 0:({},{}) Set 9: ({},{})".format(y, x, y + 1, x + 1))
                            print_plot(plot_9)
                            print_plot(plot)

                        plot = plot_9.copy()
                        y, x = start_yx
                        ind_list.clear()

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

                        plot_9[y, x] = 0

                        if test == 2:
                            print("Set 0:({},{}) Set 9: ({},{})".format(y, x, y + 1, x - 1))
                            print_plot(plot_9)
                            print_plot(plot)

                        plot = plot_9.copy()
                        y, x = start_yx
                        ind_list.clear()

                        if test == 2:
                            print("You just crossed a line buddy")
                            print("Restart\nGoTo: {} Start: {}".format(goto_yx, start_yx))

                        point_c = next_point(start_yx, goto_yx)  # get next position to check
                        s_pat = search_patterns[point_c - 1]  # change to new search pattern
                        ind = 0  # reset search pattern start

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

        # Nine
        elif l_point == 9:

            # check += 1

            if check == 2:

                if test == 1:
                    print("# Nine")

                bl_plot[y, x] = 9

                if test == 2:
                    print_plot(bl_plot)
                    print("0 at ({},{})".format(y, x))

                plot = bl_plot.copy()
                y, x = start_yx
                bl_plot[y, x] = set_to

                if test == 2:
                    print("4 at ({},{})".format(y, x))

                ind_list.clear()

                if test == 2:
                    print("Restart 9\nGoTo: {} Start: {}".format(goto_yx, start_yx))

                point_c = next_point(start_yx, goto_yx)  # get next position to check
                if test == 2:
                    print("Point_C: {}".format(point_c))
                    print_plot(plot)

                s_pat = search_patterns[point_c - 1]  # change to new search pattern
                ind = 0  # reset search pattern start
                check = 0

            else:
                point_c = next_point(start_yx, goto_yx)  # get next position to check

                if point_c == 1:
                    point_c = 5
                elif point_c == 2:
                    point_c = 6
                elif point_c == 3:
                    point_c = 7
                elif point_c == 4:
                    point_c = 8
                elif point_c == 5:
                    point_c = 1
                elif point_c == 6:
                    point_c = 2
                elif point_c == 7:
                    point_c = 3
                elif point_c == 8:
                    point_c = 4

                s_pat = search_patterns[point_c - 1]  # change to new search pattern
                ind = 0  # reset search pattern start

        if loop_c > 1:  # if loop_count is more then 1 move_to is trapped

            if test == 2:   # testing console comments
                print("Move_to trapped\nRun back_track")
                print(ind_list)

            ind_list, yx = back_track(ind_list, plot)   # back_track until a new valid space is found
            y, x = yx

            point_c = next_point(yx, goto_yx)  # get next position to check
            s_pat = search_patterns[point_c - 1]  # change to new search pattern

            loop_c = 0

    del ind_list[0]
    for i in ind_list:
        og_ind_list.append(i)
    if test == 2 or test == 3:
        print("Move_to Ind: \n", ind_list)
        print("Move_to End: \n", og_ind_list)

    return goto_yx, og_ind_list


# do not delete
def back_track(ind_list, plot):
    test = 5
    if test == 5:
        print("back_track - plot_objects.py")
    test = 0
    length = len(ind_list)

    del ind_list[-1]

    for i in range(length):
        p_y, p_x = ind_list[-1]

        points = get_surrounding_points(plot, plot, p_y, p_x, 1)

        if 1 in points:

            return ind_list, (p_y, p_x)

        else:
            if test == 1:
                print(" Delete Point: ({},{})".format(p_y, p_x))
            del ind_list[-1]
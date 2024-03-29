import datetime
import plot_objects as po

mata_file = object


class MataObject:

    def __init__(self):
        test = 0
        if test == 5:
            print("class MataObjects - mata_objects.py")

        self.stitch_objects = []                                # set
        self.colour_change = int()                              # set
        self.offset = int()                                     # set
        self.flags = 20                                         # set
        date_now = datetime.datetime.now()
        self.date = str(date_now.strftime("%Y%m%d"))            # set
        self.time = str(date_now.strftime("%H%M%S")) + "00"     # set
        self.thread_count = int()                               # set
        self.stitch_count = int()                               # set by method
        self.hoop_code = int()                                  # set
        self.extent_1 = []                                      # set
        self.extent_2 = [-1, -1, -1, -1]                        # set
        self.extent_3 = [-1, -1, -1, -1]                        # set
        self.extent_4 = [-1, -1, -1, -1]                        # set
        self.extent_5 = [-1, -1, -1, -1]                        # set
        self.stitch_lists = []                                  # set
        self.emb_stitch_lists = []                              # set by method
        self.jump_to_lists = []                                 # set
        self.emb_jump_to_lists = []                             # set by method
        self.matrix = []                                        # set

    def set_stitch_objects(self, stitch_objects):
        self.stitch_objects = stitch_objects

    def set_colour_change(self, colour_change_list):
        self.colour_change = colour_change_list

    def set_offset(self, offset):
        self.offset = offset

    def set_flags(self, flag):
        self.flags = flag

    def set_date(self, date):
        self.date = date

    def set_time(self, time):
        self.time = time

    def set_thread_count(self, thread_count):
        self.thread_count = thread_count

    def set_stitch_count(self, stitch_count):
        self.stitch_count = stitch_count

    def set_hoop_code(self, hoop_code):
        self.hoop_code = hoop_code

    def set_extent_1(self, extent_1):
        self.extent_1 = extent_1

    def set_extent_2(self, extent_2):
        self.extent_2 = extent_2

    def set_extent_3(self, extent_3):
        self.extent_3 = extent_3

    def set_extent_4(self, extent_4):
        self.extent_4 = extent_4

    def set_extent_5(self, extent_5):
        self.extent_5 = extent_5

    def set_stitch_lists(self, stitch_lists):
        self.stitch_lists = stitch_lists

    def set_emb_stitch_lists(self, emb_stitch_lists):
        self.emb_stitch_lists = emb_stitch_lists

    def set_jump_to_lists(self, jump_to_lists):
        self.jump_to_lists = jump_to_lists

    def set_emb_jump_to_lists(self, emb_jump_to_lists):
        self.emb_jump_to_lists = emb_jump_to_lists

    def set_matrix(self, matrix):
        self.matrix = matrix

    def get_stitch_objects(self):
        return self.stitch_objects

    def get_colour_change(self):
        return self.colour_change

    def get_offset(self):
        return self.offset

    def get_flags(self):
        return self.flags

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time

    def get_thread_count(self):
        return self.thread_count

    def get_stitch_count(self):
        return self.stitch_count

    def get_hoop_code(self):
        return self.hoop_code

    def get_extent_1(self):
        return self.extent_1

    def get_extent_2(self):
        return self.extent_2

    def get_extent_3(self):
        return self.extent_3

    def get_extent_4(self):
        return self.extent_4

    def get_extent_5(self):
        return self.extent_5

    def get_stitch_lists(self):
        return self.stitch_lists

    def get_emb_stitch_lists(self):
        return self.emb_stitch_lists

    def get_jump_to_lists(self):
        return self.jump_to_lists

    def get_emb_jump_to_lists(self):
        return self.emb_jump_to_lists

    def get_matrix(self):
        return self.matrix


# create offset value from pre-defined header size and colour_change list
def create_offset(colour_change):
    # 116 bytes is the set file header size with 8 bytes for each colour change after that
    return 116 + 8 * len(colour_change)


# create thread count from colour_change list
def create_thread_count(colour_change):
    return len(colour_change)


# Takes in the stitch list and matrix to create co-ordinates between the end of one stitch list
# and the start of the next stitch_list
def create_jump_to_lists(matrix, stitch_lists):
    test = 0
    # console testing statement
    if test == 5:
        print("create_jump_to_lists - class MataObjects - mata_objects.py")
    width = len(matrix[0])
    height = len(matrix)

    jump_to_lists = []

    # first jump_list starts in a centred location
    start_y = round(height / 2)     # center y
    start_x = round(width / 2)      # center x
    start_yx = (start_y, start_x)

    # connecting end of each stitch list to the start of the following stitch list
    for i in stitch_lists:
        index_list = []
        goto_yx = i[0]

        # path finding from end start_yx to goto_yx
        h, index_list = po.find_path(matrix, goto_yx, start_yx, index_list)

        index_list.append(i[0])             # adding goto_yx to the end of the list
        index_list.insert(0, start_yx)      # inserting start_yx to the beginning of the list
        start_yx = i[-1]                    # setting new start_yx

        jump_to_lists.append(index_list)    # adding new jump_list to list

        # console testing statement
        if test == 1:
            print("\nJump   list: {}".format(index_list))
            print("stitch list: ")
            for each in i:
                print(each)

    return jump_to_lists


# Takes in stitch_lists and formats them form python absolute position yx to embroidery relative position xy
def create_emb_lists(stitch_lists, matrix):
    test = 0
    # console testing comment
    if test == 5:
        print("process_stitch_lists - class MataObjects - mata_objects.py")

    emb_stitch_lists = []

    # for each list in stitch_lists
    for i, st_list in enumerate(stitch_lists):

        # for each stitch in st_list invert y value
        for ind, yx in enumerate(st_list):
            y_max = len(matrix) - 1                 # set max y value
            cur_y, cur_x = yx                       # get current y value
            st_list[ind] = (y_max - cur_y, cur_x)   # invert y value and set y, x

        l_p = st_list[0]    # set last point as first point in st_list
        emb_list = []

        # for each stitch in st_list work out its value based off the last stitch
        for j in st_list:
            cur_y, cur_x = j        # set current y, x
            l_y, l_x = l_p          # set last point y, x
            y_val = cur_y - l_y     # get travel value from last y to current y - max value 1, min value -1
            x_val = cur_x - l_x     # get travel value from last x to current x - max value 1, min value -1
            l_p = j                 # set current point to last point

            emb_list.append((x_val, y_val))     # append new xy to list - very important, yx flipped to xy

        # console testing comment
        if test == 1:
            print("Step 1 Stitches: ")
            for each in emb_list:
                print(each)

        emb_stitch_lists.append(emb_list)       # append emb_list to emb_stitch_lists

    return emb_stitch_lists


# Gets matrix from first stitch_object - matrix used for its dimensions only
def create_matrix(stitch_objects):
    stitch_ob = stitch_objects[0]       # get stitch_object
    matrix = stitch_ob.get_matrix()     # get matrix from stitch object
    return matrix


# Creates stitch count int using the length of the emb_jump lists and the emb_stitch lists
def create_stitch_count(emb_jump, emb_stitch):
    test = 0

    # console testing comment
    if test == 5:
        print("set_stitch_count - class MataObjects - mata_objects.py")
    stitches = 0

    for i in emb_stitch:
        stitches += len(i)  # adding len of each emb stitch list to total

    for i in emb_jump:
        stitches += len(i)  # adding len of each emb jump list to total

    return stitches


# Creates a list of all colour changes using the colour information from each stitch object
def create_colour_change_list(stitch_objects):
    test = 0

    # console testing comment
    if test == 5:
        print("set_colour_change_list - class MataObjects - mata_objects.py")
    colour_change = []

    # for each object in stitch_objects
    for stitch_ob in stitch_objects:
        colour = stitch_ob.get_colour()     # get colour
        colour_change.append(colour)        # append colour to colour_change list
    return colour_change


# Create list of each objects stitch lists
def create_stitch_lists(stitch_objects):
    test = 0

    # console testing comment
    if test == 5:
        print("set_stitch_lists - class MataObjects - mata_objects.py")

    stitch_lists = []

    # for each object in stitch_objects
    for stitch_ob in stitch_objects:
        s_list = stitch_ob.get_stitch_list()    # get stitch list
        stitch_lists.append(s_list)             # append stitch list to stitch_lists

    return stitch_lists


# Create the mata_object that will be used to gather all necessary info for file writting
def create_mata_object(stitch_objects, hoop_code):
    test = 0

    # console testing comment
    if test == 5:
        print("create_mata_object - mata_objects.py")

    global mata_file            # set mata_file variable level equal to outer scope
    # create mata_object
    mata_file = MataObject()

    # set stitch_objects to passed stitch_objects list
    mata_file.set_stitch_objects(stitch_objects)

    # creating and setting colour_change_list using stitch_objects list
    cc_list = create_colour_change_list(stitch_objects)
    mata_file.set_colour_change(cc_list)

    # creating and setting offset using colour_change_list
    offset = create_offset(cc_list)
    mata_file.set_offset(offset)

    # creating and setting the thread_count using the colour_change_list
    thread_count = create_thread_count(cc_list)
    mata_file.set_thread_count(thread_count)

    # setting the hoop_code with the passed hoop_code variable
    mata_file.set_hoop_code(hoop_code)

    # creating and setting matrix using the stitch_objects list
    matrix = create_matrix(stitch_objects)
    mata_file.set_matrix(matrix)

    # creating and setting stitch_lists using the stitch_objects list
    stitch_lists = create_stitch_lists(stitch_objects)
    mata_file.set_stitch_lists(stitch_lists)

    # creating and setting jump_to_lists using matrix and stitch_lists lists
    jump_lists = create_jump_to_lists(matrix, stitch_lists)
    mata_file.set_jump_to_lists(jump_lists)

    # creating, processing and setting emb_jump_to_lists using jump_lists, matrix and stitch_objects
    emb_j_lists = create_emb_lists(jump_lists, matrix)
    emb_j_lists = process_stitch_lists(emb_j_lists, stitch_objects, 0)
    mata_file.set_emb_jump_to_lists(emb_j_lists)

    # creating, processing and setting emb_stitch_to_lists using stitch_lists, matrix and stitch_objects
    emb_s_lists = create_emb_lists(stitch_lists, matrix)
    emb_s_lists = process_stitch_lists(emb_s_lists, stitch_objects, 1)
    mata_file.set_emb_stitch_lists(emb_s_lists)

    # creating and setting stitch_count using emb_j_lists and emb_s_lists
    stitch_count = create_stitch_count(emb_j_lists, emb_s_lists)
    mata_file.set_stitch_count(stitch_count)

    # creating and setting extent_1 using matrix
    extent_1 = create_extent(matrix)
    mata_file.set_extent_1(extent_1)


# create the 4 extent measurements to be stored in extent_1
def create_extent(matrix):
    test = 0

    # console testing comment
    if test == 5:
        print("set_extent - class MataObjects - mata_objects.py")
    v = round(len(matrix) / 2)      # get matrix height and divide by 2 to get vertical extents
    h = round(len(matrix[0]) / 2)   # get matrix width and divide by 2 to get horizontal extents
    extent_1 = [h, v, h, v]         # set extents in list format [Left, Top, Right, Bottom]

    return extent_1


# processes emb_lists by combining stitches of the same direction up until a max length
def process_stitch_lists(stitch_lists, stitch_objects, mode):

    emb_processed_lists = []

    # for each s_list in stitch_lists
    for i, s_list in enumerate(stitch_lists):

        if mode == 1:
            max_len = stitch_objects[i].get_stitch_len()    # if mode is 1 set max_len to stitch_ob max length
        else:
            max_len = 126                                   # else set max length to 126 (the maximum jump possible)

        # carries out the process of combining stitches using s_list and max_len
        emb_list = combine_stitches(s_list, max_len)

        emb_processed_lists.append(emb_list)    # append output list to emb_processed_lists

    return emb_processed_lists


# creates a list of stitches that have all the stitch in the same direction combined in max_len intervals
def combine_stitches(stitch_list, max_len):
    test = 0

    # console testing comment
    if test == 5:
        print("process_stitch_list - mata_objects.py")

    emb_stitches = []
    stitch = []

    # for each current point in stitch_list
    for ind, cur_p in enumerate(stitch_list):

        if len(stitch) == 0:    # if stitch is empty...
            last_p = cur_p      # set last pont == to current point

        # console testing comment
        if test == 1:
            print("Last: {} Cur: {} Ind: {} Len: {}".format(last_p, cur_p, ind, len(stitch_list) - 1))

        if last_p == cur_p:     # if last point == current point...

            if len(stitch) >= max_len / 3:  # if stitch is greater than or equal to max length divided by 3...

                # carry out the add section
                s_x = 0
                s_y = 0

                # for each co-ordinate in stitch
                for i in stitch:
                    x, y = i        # get co-ordinate x and y
                    s_x += x        # add co-ordinate x to total x
                    s_y += y        # add co-ordinate y to total y
                s_x = s_x * 3       # multiply total x by 3 - measurement ratio of 1 pixel is equal to 0.3mm
                s_y = s_y * 3       # multiply total y by 3 - measurement ratio of 1 pixel is equal to 0.3mm

                # console testing comment
                if test == 1:
                    print("M Stitch Set: {} Stitch: {}".format((s_x, s_y), stitch))

                emb_stitches.append((s_x, s_y))     # append total x and total y tot emb_stitches
                stitch.clear()                      # clear stitch
                stitch.append(cur_p)                # append current point to stitch
                last_p = cur_p                      # set last point as current point

            else:                       # else if stitch length is not great then max divided by 3...
                stitch.append(cur_p)    # add current point to stitch

        elif last_p != cur_p:   # else if last point is not equal to current point...
            # carry out the add section
            s_x = 0
            s_y = 0

            # for each co-ordinate in stitch
            for i in stitch:
                x, y = i  # get co-ordinate x and y
                s_x += x  # add co-ordinate x to total x
                s_y += y  # add co-ordinate y to total y
            s_x = s_x * 3  # multiply total x by 3 - measurement ratio of 1 pixel is equal to 0.3mm
            s_y = s_y * 3  # multiply total y by 3 - measurement ratio of 1 pixel is equal to 0.3mm

            # console testing comment
            if test == 1:
                print("N Stitch Set: {} Stitch: {}".format((s_x, s_y), stitch))

            emb_stitches.append((s_x, s_y))  # append total x and total y tot emb_stitches
            stitch.clear()  # clear stitch
            stitch.append(cur_p)  # append current point to stitch
            last_p = cur_p

        if ind >= len(stitch_list) - 1 and stitch: # if current point is the last in stitch_list and stitch is not empty...
            # carry out the add section
            s_x = 0
            s_y = 0

            # for each co-ordinate in stitch
            for i in stitch:
                x, y = i  # get co-ordinate x and y
                s_x += x  # add co-ordinate x to total x
                s_y += y  # add co-ordinate y to total y
            s_x = s_x * 3  # multiply total x by 3 - measurement ratio of 1 pixel is equal to 0.3mm
            s_y = s_y * 3  # multiply total y by 3 - measurement ratio of 1 pixel is equal to 0.3mm

            # console testing comment
            if test == 1:
                print("L Stitch Set: {} Stitch: {}".format((s_x, s_y), stitch))

            emb_stitches.append((s_x, s_y))     # append total x and total y tot emb_stitches

    # console testing comment
    if test == 1:
        print("End Last: {} Cur: {} Stitch: {}".format(last_p, cur_p, stitch))

    return emb_stitches


def print_mata_info():
    test = 5
    if test == 5:
        print("print_mata_info - mata_objects.py")
    offset = mata_file.offset
    flag = mata_file.flags
    date = mata_file.date
    time = mata_file.time
    thread_count = mata_file.thread_count
    stitch_count = mata_file.stitch_count
    hoop_code = mata_file.hoop_code
    extent1 = mata_file.extent1
    extent2 = mata_file.extent2
    extent3 = mata_file.extent3
    extent4 = mata_file.extent4
    extent5 = mata_file.extent5
    colour_change = mata_file.colour_change
    jump_to_lists = mata_file.emb_jump_to_lists
    stitch_lists = mata_file.emb_stitch_lists
    print("\n\nMata_file Data:\n")
    print("Offset: {}".format(offset))
    print("Flags: {}".format(flag))
    print("Date: {}".format(date))
    print("Time: {}".format(time))
    print("Thread_count: {}".format(thread_count))
    print("Stitch_count: {}".format(stitch_count))
    print("Hoop_code: {}".format(hoop_code))
    ext_print = "Extent 1:\n"
    for i in extent1:
        ext_print += str(i) + " "
    ext_print += "\n"
    print(ext_print)
    ext_print = "Extent 2:\n"
    for i in extent2:
        ext_print += str(i) + " "
    ext_print += "\n"
    print(ext_print)
    ext_print = "Extent 3:\n"
    for i in extent3:
        ext_print += str(i) + " "
    ext_print += "\n"
    print(ext_print)
    ext_print = "Extent 4:\n"
    for i in extent4:
        ext_print += str(i) + " "
    ext_print += "\n"
    print(ext_print)
    ext_print = "Extent 5:\n"
    for i in extent5:
        ext_print += str(i) + " "
    ext_print += "\n"
    print(ext_print)

    col_change = "Colour_changes:\n "
    for i, colour in enumerate(colour_change):
        col_change += str(colour) + " "
    print(col_change)

    for i, j_list in enumerate(jump_to_lists):
        s_list = stitch_lists[i]

        print("Jump List {}:\n  {}".format(i, j_list))
        print("Stitch List {}:\n  {}".format(i, s_list))



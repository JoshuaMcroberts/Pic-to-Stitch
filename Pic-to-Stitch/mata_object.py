import datetime
import plot_objects as po
import stitch_objects as so

mata_file = object


class MataObject:

    def __init__(self, stitch_objects, hoop_code):

        self.stitch_objects = stitch_objects                # set
        self.colour_change = self.set_colour_change_list()  # set
        self.offset = 116 + 8 * len(self.colour_change)     # set
        self.flags = 20                                     # set
        date_now = datetime.datetime.now()
        self.date = str(date_now.strftime("%Y%m%d"))        # set
        self.time = str(date_now.strftime("%H%M%S")) + "00" # set
        self.thread_count = len(self.colour_change)         # set
        self.stitch_count = int()                           # set by method
        self.hoop_code = hoop_code                          # set
        self.extent1 = []                                   # set
        self.extent2 = [-1, -1, -1, -1]                     # set
        self.extent3 = [-1, -1, -1, -1]                     # set
        self.extent4 = [-1, -1, -1, -1]                     # set
        self.extent5 = [-1, -1, -1, -1]                     # set
        self.stitch_lists = self.set_stitch_lists()         # set
        self.emb_stitch_lists = []                          # set by method
        self.jump_to_lists = []                             # set
        self.emb_jump_to_lists = []                         # set by method
        self.matrix = stitch_objects[0].matrix              # set
        self.set_extent()

    def set_stitch_lists(self):
        stitch_lists = []
        for stitch_ob in self.stitch_objects:
            s_list = stitch_ob.get_stitch_list()
            stitch_lists.append(s_list)
        return stitch_lists

    def set_colour_change_list(self):
        colour_change = []
        for stitch_ob in self.stitch_objects:
            colour = stitch_ob.get_colour()
            colour_change.append(colour)
        return colour_change

    def set_stitch_count(self):     # set after both emb lists
        stitches = 0
        for i in self.emb_stitch_lists:
            stitches += len(i)

        for i in self.emb_jump_to_lists:
            stitches += len(i)

        self.stitch_count = stitches

    def set_extent(self):

        v = round(len(self.matrix) / 2)
        h = round(len(self.matrix[0]) / 2)
        self.extent1 = [h, v, h, v]

    def process_stitch_lists(self):

        for i, st_list in enumerate(self.stitch_lists):

            for ind, yx in enumerate(st_list):
                y_max = len(self.matrix) - 1
                cur_y, cur_x = yx
                st_list[ind] = (y_max - cur_y, cur_x)

            l_p = st_list[0]
            emb_stitch_list = []

            for j in st_list:   # vals of 0 1 -1
                cur_y, cur_x = j
                l_y, l_x = l_p
                y_val = cur_y - l_y
                x_val = cur_x - l_x
                l_p = j
                emb_stitch_list.append((x_val, y_val))   # very important, yx flipped to xy
            # process stitches - max stitch value
            print("Step 1 Stitches: ")
            for each in emb_stitch_list:
                print(each)
            s_list = process_stitch_list(emb_stitch_list, self.stitch_objects[i].stitch_len)
            self.emb_stitch_lists.append(s_list)

    def create_jump_to_lists(self):
        test = 1
        width = len(self.matrix[0])
        height = len(self.matrix)

        start_y = round(height / 2)
        start_x = round(width / 2)
        start_yx = (start_y, start_x)

        for i in self.stitch_lists:     # connecting centre to stitch list start and ends to starts
            index_list = []
            goto_yx = i[0]
            # print(i)
            # print("goto: {} start: {}".format(goto_yx, start_yx))
            h, index_list = po.find_path(self.matrix, goto_yx, start_yx, index_list)
            index_list.append(i[0])
            index_list.insert(0, start_yx)
            start_yx = i[-1]

            self.jump_to_lists.append(index_list)
            if test == 1:
                print("\nJump   list: {}".format(index_list))
                # print("stitch list: {}".format(i))
                print("stitch list: ")
                for each in i:
                    print(each)

        for jump_to_list in self.jump_to_lists:

            for ind, yx in enumerate(jump_to_list):
                y_max = len(self.matrix) - 1
                cur_y, cur_x = yx
                jump_to_list[ind] = (y_max - cur_y, cur_x)

            emb_jump_to_list = []
            l_p = jump_to_list[0]
            for yx in jump_to_list:
                cur_y, cur_x = yx
                l_y, l_x = l_p
                y_val = cur_y - l_y
                x_val = cur_x - l_x
                l_p = yx
                emb_jump_to_list.append((x_val, y_val))  # very important, yx flipped to xy

            j_list = process_stitch_list(emb_jump_to_list, 126)
            # del j_list[0]
            # j_list = emb_jump_to_list
            self.emb_jump_to_lists.append(j_list)


def create_mata_object(stitch_objects, hoop_code):
    global mata_file
    mata_file = MataObject(stitch_objects, hoop_code)
    mata_file.create_jump_to_lists()
    mata_file.process_stitch_lists()
    mata_file.set_stitch_count()


def process_stitch_list(stitch_list, max_len):
    test = 0
    # last_p = stitch_list[0]
    emb_stitches = []
    stitch = []
    for ind, cur_p in enumerate(stitch_list):

        if len(stitch) == 0:
            last_p = cur_p

        if test == 1:
            print("Last: {} Cur: {} Ind: {} Len: {}".format(last_p, cur_p, ind, len(stitch_list) - 1))

        if last_p == cur_p:

            if len(stitch) >= max_len / 3:
                # add section
                s_x = 0
                s_y = 0
                for i in stitch:
                    x, y = i
                    s_x += x
                    s_y += y
                s_x = s_x * 3
                s_y = s_y * 3
                if test == 1:
                    print("M Stitch Set: {} Stitch: {}".format((s_x, s_y), stitch))
                emb_stitches.append((s_x, s_y))
                stitch.clear()
                stitch.append(cur_p)
                last_p = cur_p

            else:
                stitch.append(cur_p)    # add to stitch

        elif last_p != cur_p:
            # add section
            s_x = 0
            s_y = 0
            for i in stitch:
                x, y = i
                s_x += x
                s_y += y
            s_x = s_x * 3
            s_y = s_y * 3
            if test == 1:
                print("N Stitch Set: {} Stitch: {}".format((s_x, s_y), stitch))
            emb_stitches.append((s_x, s_y))
            stitch.clear()
            stitch.append(cur_p)
            last_p = cur_p

        if ind >= len(stitch_list) - 1 and stitch:
            # add section
            s_x = 0
            s_y = 0
            for i in stitch:
                x, y = i
                s_x += x
                s_y += y
            s_x = s_x * 3
            s_y = s_y * 3
            if test == 1:
                print("L Stitch Set: {} Stitch: {}".format((s_x, s_y), stitch))
            emb_stitches.append((s_x, s_y))

    if test == 1:

        print("End Last: {} Cur: {} Stitch: {}".format(last_p, cur_p, stitch))
    return emb_stitches


def print_mata_info():
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

    # sit = [(0, 1), (0, 1), (0, 1), (0, -1), (0, -1), (0, -1), (0, 1), (0, -1), (0, 1), (0, -1), (0, -1), (0, -1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1)]
    # print(process_stitch_list(sit, 3))

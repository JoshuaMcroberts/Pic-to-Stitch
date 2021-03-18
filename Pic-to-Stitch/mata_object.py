import datetime
import plot_objects as po
import stitch_objects as so


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
        self.stitch_count = int()                           # set - after both emb lists
        self.hoop_code = hoop_code                          # set
        self.extent1 = []                                   # set
        self.extent2 = [-1, -1, -1, -1]                     # set
        self.extent3 = [-1, -1, -1, -1]                     # set
        self.extent4 = [-1, -1, -1, -1]                     # set
        self.extent5 = [-1, -1, -1, -1]                     # set
        self.stitch_lists = self.set_stitch_lists()         # set
        self.emb_stitch_lists = []                          # need to set
        self.jump_to_lists = []                             # set
        self.emb_jump_to_lists = []                         # need to set
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
        self.stitch_count = len(self.emb_stitch_lists) + len(self.emb_jump_to_lists)

    def set_extent(self):

        v = round(len(self.matrix) % 2)
        h = round(len(self.matrix[0]) % 2)
        self.extent1 = [h, v, h, v]

    def process_stitch_lists(self):

        for st_list in self.stitch_lists:

            l_p = st_list[0]
            emb_stitch_list = []

            for i in st_list:   # vals of 0 1 -1
                cur_y, cur_x = i
                l_y, l_x = l_p
                y_val = cur_y - l_y
                x_val = cur_x - l_x
                l_p = i
                emb_stitch_list.append((x_val, y_val))   # very important, yx flipped to xy
            # process stitches - max stitch value
            # self.emb_stitch_lists.append(emb_stitch_list)

    def create_jump_to_lists(self):
        width = len(self.matrix[0])
        height = len(self.matrix)

        start_y = round(height % 2)
        start_x = round(width % 2)
        start_yx = (start_y, start_x)
        ind_list = []
        for i in self.stitch_lists:
            goto_yx = i[0]
            print(i)
            print("goto: {}".format(goto_yx))
            h, ind_list = po.find_path(self.matrix, goto_yx, start_yx, ind_list)
            start_yx = i[-1]
            self.jump_to_lists.append(ind_list)

        emb_jump_to_list = []
        for jump_to_list in self.jump_to_lists:
            l_p = jump_to_list[0]
            for yx in jump_to_list:
                cur_y, cur_x = yx
                l_y, l_x = l_p
                y_val = cur_y - l_y
                x_val = cur_x - l_x
                l_p = yx
                emb_jump_to_list.append((x_val, y_val))  # very important, yx flipped to xy
            # process stitches - max stitch value
            # self.emb_jump_to_lists.append(emb_jump_to_list)


def create_mata_object(stitch_objects, hoop_code):

    mata_file = MataObject(stitch_objects, hoop_code)
    mata_file.process_stitch_lists()
    mata_file.create_jump_to_lists()

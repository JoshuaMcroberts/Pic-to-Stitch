import numpy as np
import plot_objects as po

janome_colour_list = [(0, 0, 0), (240, 240, 240), (255, 255, 23), (255, 102, 0), (47, 89, 51), (35, 115, 54),
                      (101, 194, 200), (171, 90, 150), (246, 105, 160), (255, 0, 0),
                      (156, 100, 69), (11, 47, 132), (228, 195, 93), (72, 26, 5),
                      (172, 156, 199), (253, 245, 181), (249, 153, 183), (250, 179, 129),
                      (215, 189, 164), (151, 5, 51), (160, 184, 204), (127, 194, 28),
                      (229, 229, 229), (136, 155, 155), (152, 214, 189), (178, 225, 227),
                      (152, 243, 254), (112, 169, 226), (29, 84, 120), (7, 22, 80),
                      (255, 187, 187), (255, 96, 72), (255, 90, 39), (226, 161, 136),
                      (181, 148, 116), (245, 219, 139), (255, 204, 0), (255, 189, 227),
                      (195, 0, 126), (168, 0, 67), (84, 5, 113), (255, 9, 39),
                      (198, 238, 203), (96, 133, 65), (96, 148, 24), (6, 72, 13),
                      (91, 210, 181), (76, 181, 143), (4, 145, 123), (89, 91, 97),
                      (255, 255, 220), (230, 101, 30), (230, 150, 90), (240, 156, 150),
                      (167, 108, 61), (180, 90, 48), (110, 57, 55), (92, 38, 37),
                      (98, 49, 189), (20, 50, 156), (22, 95, 167), (196, 227, 157),
                      (253, 51, 163), (238, 113, 175), (132, 49, 84), (163, 145, 102),
                      (12, 137, 24), (247, 242, 151), (204, 153, 0), (199, 151, 50),
                      (255, 157, 0), (255, 186, 94), (252, 241, 33), (255, 71, 32),
                      (0, 181, 82), (2, 87, 181), (208, 186, 176), (227, 190, 129)]


class StitchObject:

    def __init__(self, passed_colour, stitch_list, max_stitch_len, matrix, hoop_code):  # hoop_code my not be needed
        self.stitch_list = stitch_list
        self.jump_to_list = []
        self.emb_stitch_list = []
        self.emb_jump_to_list = []
        self.colour = passed_colour
        self.stitch_type = str()
        self.stitch_count = int()
        self.stitch_len = max_stitch_len
        p_row = [1] * len(matrix[0])  # create blank plot make template plot
        blank_plot = np.array([p_row] * len(matrix))
        self.matrix = blank_plot
        self.set_colour()
        self.hoop_code = hoop_code

    def get_stitch_list(self):
        return self.stitch_list

    def set_colour(self):
        colour_tup = self.colour

        if colour_tup in janome_colour_list:
            colour_num = janome_colour_list.index(colour_tup)
            colour_num += 1
            self.colour = colour_num

    def get_colour(self):
        return self.colour

    def process_stitch_list(self):

        l_p = self.stitch_list[0]
        for i in self.stitch_list:
            cur_y, cur_x = i
            l_y, l_x = l_p
            y_val = cur_y - l_y
            x_val = cur_x - l_x
            l_p = i
            self.emb_stitch_list.append((x_val, y_val))   # very important, yx flipped to xy
        print(self.emb_stitch_list)


def create_stitch_objects(objects):
    test = 0
    stitch_ob_list = []

    for ob in objects:
        ob_colour = ob.get_ob_colour()
        # ob_id = ob.get_ob_id()
        ob_stitch_list = ob.get_stitch_list()
        ob_stitch_len = ob.get_stitch_len()
        ob_matrix = ob.get_ob_matrix()

        stitch_ob = StitchObject(ob_colour, ob_stitch_list, ob_stitch_len, ob_matrix)
        stitch_ob.process_stitch_list()

        stitch_ob_list.append(stitch_ob)
    return stitch_ob_list


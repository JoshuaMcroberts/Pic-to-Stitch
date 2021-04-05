import numpy as np


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

    def __init__(self):
        self.stitch_list = []
        self.colour = int()
        self.stitch_type = str()
        self.stitch_len = int()
        self.matrix = []

    def set_stitch_list(self, stitch_list):
        self.stitch_list = stitch_list

    def set_colour(self, colour):
        self.colour = colour

    def set_stitch_type(self, stitch_type):
        self.stitch_type = stitch_type

    def set_stitch_len(self, stitch_len):
        self.stitch_len = stitch_len

    def set_matrix(self, matrix):
        self.matrix = matrix

    def get_stitch_list(self):
        return self.stitch_list

    def get_colour(self):
        return self.colour

    def get_stitch_type(self):
        return self.stitch_type

    def get_stitch_len(self):
        return self.stitch_len

    def get_matrix(self):
        return self.matrix


# creates matrix based of the dimensions of the matrix past
def create_matrix(matrix):
    p_row = [1] * len(matrix[0])                    # set row length
    blank_plot = np.array([p_row] * len(matrix))    # set number of rows
    return blank_plot


# create Janome colour code using Janome rgb colour list
def create_colour(colour):
    test = 0

    # console testing comment
    if test == 5:
        print("set_colour - StitchObject - stitch_objects.py")

    global janome_colour_list
    colour_tup = colour

    # for each colour in janome_colour_list
    for i, col in enumerate(janome_colour_list):

        # console testing comment
        if test == 1:
            print(colour_tup, " ", col)

        # pixel colour compare structure
        if colour_tup[0] == col[0]:             # if both red values are equal...
            if colour_tup[1] == col[1]:         # if both green values are equal...
                if colour_tup[2] == col[2]:     # if both blue values are equal...
                    colour_num = i + 1          # set colour_num to current index + 1

                    # console testing comment
                    if test == 1:
                        print("Set Colour to num {}".format(colour_num))
                    return colour_num
    return False


# create stitch objects using objects list
def create_stitch_objects(objects):
    test = 0

    # console testing comment
    if test == 5:
        print("create_stitch_objects - stitch_objects.py")

    stitch_ob_list = []

    # for each object in objects list
    for ob in objects:
        ob_colour = ob.get_colour()          # get object colour
        ob_stitch_list = ob.get_stitch_list()   # get object stitch_list
        ob_stitch_len = ob.get_stitch_len()     # get object stitch_len
        ob_matrix = ob.get_matrix()          # get object matrix

        # create new stitch object
        stitch_ob = StitchObject()
        stitch_ob.set_stitch_list(ob_stitch_list)   # set stitch object stitch_list
        stitch_ob.set_stitch_len(ob_stitch_len)     # set stitch object stitch_len

        matrix = create_matrix(ob_matrix)           # create matrix using object matrix
        stitch_ob.set_matrix(matrix)                # set stitch object matrix

        colour = create_colour(ob_colour)           # create colour using object colour
        stitch_ob.set_colour(colour)                # set stitch object colour

        stitch_ob_list.append(stitch_ob)            # append stitch object to stitch_ob-list

    return stitch_ob_list


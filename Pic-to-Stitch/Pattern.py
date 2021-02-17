import numpy as np


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

import numpy as np



class StitchObject:

    def __init__(self, passed_colour, passed_object_id, stitch_list):
        self.stitch_list = stitch_list
        self.colour = passed_colour
        self.stitch_type = str()
        self.stitch_count = int()
        self.obj_width = int()      # not needed
        self.obj_height = int()     # not needed
        self.max_yx = 0     # not needed
        self.min_yx = 0     # not needed
        self.object_id = passed_object_id
        # row = [0] * width    # not needed
        # self.plot = np.array([row] * height)    # not needed


def create_stitch_objects(objects):
    test = 0
    stitch_ob_list = []

    for ob in objects:
        ob_colour = ob.get_colour()
        ob_id = ob.get_od_id()
        ob_stitch_list = ob.get_stitch_list()

        stitch_ob = StitchObject(ob_colour, ob_id, ob_stitch_list)
        stitch_ob_list.append(stitch_ob)

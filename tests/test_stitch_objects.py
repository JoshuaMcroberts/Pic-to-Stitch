import unittest
import numpy as np
import sys
sys.path.append('../pic_to_stitch/')

from pic_to_stitch import stitch_objects as so
from pic_to_stitch import plot_objects as po


class TestStitchObjects(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        self.stitch_ob = so.StitchObject()
        self.stitch_ob.stitch_list = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 6), (5, 7), (6, 7)]
        self.stitch_ob.colour = 32
        self.stitch_ob.stitch_type = "Outline Stitch"
        self.stitch_ob.stitch_len = 33
        row = [1] * 10
        self.stitch_ob.matrix = np.array([row] * 10)

    def tearDown(self):
        pass

    def test_set_stitch_list(self):
        stitch_list = [(2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]
        self.stitch_ob.set_stitch_list(stitch_list)
        self.assertEqual([(2, 3), (3, 4), (4, 5), (5, 6), (6, 7)], self.stitch_ob.stitch_list)

    def test_set_colour(self):
        self.stitch_ob.set_colour(43)
        self.assertEqual(43, self.stitch_ob.colour)

    def test_set_stitch_type(self):
        self.stitch_ob.set_stitch_type("Fill Stitch")
        self.assertEqual("Fill Stitch", self.stitch_ob.stitch_type)

    def test_set_stitch_len(self):
        self.stitch_ob.set_stitch_len(12)
        self.assertEqual(12, self.stitch_ob.stitch_len)

    def test_set_matrix(self):
        row = [0] * 10
        matrix = np.array([row] * 10)
        test_matrix = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        self.stitch_ob.set_matrix(matrix)
        for y, row in enumerate(self.stitch_ob.matrix):
            for x, point in enumerate(row):
                self.assertEqual(test_matrix[y, x], point)

    def test_get_stitch_list(self):
        result = self.stitch_ob.get_stitch_list()
        self.assertEqual([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 6), (5, 7), (6, 7)], result)

    def test_get_colour(self):
        colour = self.stitch_ob.get_colour()
        self.assertEqual(32, colour)

    def test_get_stitch_type(self):
        result = self.stitch_ob.get_stitch_type()
        self.assertEqual("Outline Stitch", result)

    def test_get_stitch_len(self):
        result = self.stitch_ob.get_stitch_len()
        self.assertEqual(33, result)

    def test_get_matrix(self):
        test_matrix = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

        result = self.stitch_ob.get_matrix()
        for y, row in enumerate(result):
            for x, point in enumerate(row):
                self.assertEqual(test_matrix[y, x], point)

    def test_create_matrix(self):
        row = [0] * 10
        matrix = np.array([row] * 10)
        result = so.create_matrix(matrix)

        for y, row in enumerate(result):
            for x, point in enumerate(row):
                self.assertEqual(1, point)

    def test_create_colour(self):
        colour_1 = so.create_colour((112, 169, 226))
        colour_2 = so.create_colour((227, 190, 129))
        colour_3 = so.create_colour((91, 210, 181))
        colour_4 = so.create_colour((237, 190, 19))

        self.assertEqual(28, colour_1)
        self.assertEqual(78, colour_2)
        self.assertEqual(47, colour_3)
        self.assertFalse(colour_4)

    def test_create_stitch_objects(self):
        ob_list = []
        jan_col = [(245, 219, 139), (11, 47, 132), (255, 186, 94)]
        for i in range(3):
            row = [0] * 10
            matrix = np.array([row] * 10)

            ob = po.ObjectPlot()
            ob.set_stitch_list([(0, 0), (0, 1), (1, 2), (2, 2)])
            if i == 0:
                ob.set_stitch_len(5)
            else:
                ob.set_stitch_len(10 * i)
            ob.set_matrix(matrix)
            ob.set_colour(jan_col[i])

            ob_list.append(ob)

        test_matrix = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

        test_ob_1 = so.StitchObject()
        test_ob_1.matrix = test_matrix
        test_ob_1.stitch_list = [(0, 0), (0, 1), (1, 2), (2, 2)]
        test_ob_1.stitch_len = 5
        test_ob_1.colour = 36

        test_ob_2 = so.StitchObject()
        test_ob_2.matrix = test_matrix
        test_ob_2.stitch_list = [(0, 0), (0, 1), (1, 2), (2, 2)]
        test_ob_2.stitch_len = 10
        test_ob_2.colour = 12

        test_ob_3 = so.StitchObject()
        test_ob_3.matrix = test_matrix
        test_ob_3.stitch_list = [(0, 0), (0, 1), (1, 2), (2, 2)]
        test_ob_3.stitch_len = 20
        test_ob_3.colour = 72

        test_list = [test_ob_1, test_ob_2, test_ob_3]

        stitch_ob_list = so.create_stitch_objects(ob_list)

        for i, ob in enumerate(test_list):
            self.assertEqual(ob.stitch_list, stitch_ob_list[i].stitch_list)
            self.assertEqual(ob.stitch_len, stitch_ob_list[i].stitch_len)
            self.assertEqual(ob.colour, stitch_ob_list[i].colour)

            for y, row in enumerate(ob.matrix):
                for x, point in enumerate(row):
                    self.assertEqual(point, stitch_ob_list[i].matrix[y, x])


if __name__ == '__main__':
    unittest.main()


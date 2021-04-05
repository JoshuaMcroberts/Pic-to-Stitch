import unittest
from unittest.mock import Mock
import numpy as np
import sys

sys.path.append('../pic_to_stitch/')

from pic_to_stitch import plot_objects as po


class TestPlotObjectsColourClass(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        self.object_ob = po.ObjectPlot()
        row = [0] * 10
        matrix = np.array([row] * 10)
        self.object_ob.matrix = matrix
        self.object_ob.ob_id = 1
        self.object_ob.colour = (23, 212, 43)
        self.object_ob.ref_plot = matrix

    def tearDown(self):
        pass

    def test_set_ob_id(self):
        self.object_ob.set_ob_id(1)
        self.assertEqual(1, self.object_ob.ob_id)

    def test_set_colour(self):
        self.object_ob.set_colour((255, 255, 255))
        self.assertEqual((255, 255, 255), self.object_ob.colour)

    def test_set_ref_plot(self):
        test_ref_plot = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 2, 2, 2, 0, 0],
                                  [0, 0, 0, 0, 0, 2, 2, 2, 0, 0],
                                  [0, 0, 0, 0, 0, 2, 2, 2, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

        test_plot = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 2, 2, 2, 0, 0],
                     [0, 0, 0, 0, 0, 2, 2, 2, 0, 0],
                     [0, 0, 0, 0, 0, 2, 2, 2, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.object_ob.set_ref_plot(test_ref_plot)

        for y, row in enumerate(test_plot):
            for x, point in enumerate(row):
                self.assertEqual(point, self.object_ob.ref_plot[y, x])

    def test_set_section_image(self):
        self.object_ob.set_section_image("boop")
        self.assertEqual("boop", self.object_ob.section_image)

    def test_set_stitch_type(self):
        self.object_ob.set_stitch_type("boop")
        self.assertEqual("boop", self.object_ob.stitch_type)

    def test_set_stitch_len(self):
        self.object_ob.set_stitch_len(1)
        self.assertEqual(1, self.object_ob.stitch_len)

    def test_set_stitch_list(self):
        stitch = [(2, 3), (3, 4), (4, 5), (5, 5), (5, 6)]
        self.object_ob.set_stitch_list(stitch)
        self.assertEqual([(2, 3), (3, 4), (4, 5), (5, 5), (5, 6)], self.object_ob.stitch_list)

    def test_get_ob_id(self):
        ob_id = self.object_ob.get_ob_id()
        self.assertEqual(1, ob_id)

    def test_get_colour(self):
        colour = self.object_ob.get_colour()
        self.assertEqual((23, 212, 43), colour)

    def test_get_ref_plot(self):
        ref_plot = self.object_ob.get_ref_plot()
        test_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        for y, row in enumerate(test_matrix):
            for x, point in enumerate(row):
                self.assertEqual(point, ref_plot[y, x])

    def test_get_section_image(self):
        self.object_ob.section_image = "theres"
        image = self.object_ob.get_section_image()
        self.assertEqual("theres", image)

    def test_get_stitch_type(self):
        self.object_ob.stitch_type = "outline"
        s_type = self.object_ob.get_stitch_type()
        self.assertEqual("outline", s_type)

    def test_get_stitch_len(self):
        self.object_ob.stitch_len = 4
        s_len = self.object_ob.get_stitch_len()
        self.assertEqual(4, s_len)

    def test_get_stitch_list(self):
        self.object_ob.stitch_list = [(2, 3), (3, 4), (4, 5), (5, 5), (5, 6)]
        s_list = self.object_ob.get_stitch_list()
        self.assertEqual([(2, 3), (3, 4), (4, 5), (5, 5), (5, 6)], s_list)

    def test_create_object_plot(self):
        ob = po.ObjectPlot()

        test_matrix = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                                [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                                [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                                [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

        test_ref_plot = np.array([['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
                                  ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
                                  ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
                                  ['b', 'b', 'b', 'a', 'a', 'a', 'a', 'b', 'b', 'b'],
                                  ['b', 'b', 'b', 'a', 'a', 'a', 'a', 'b', 'b', 'b'],
                                  ['b', 'b', 'b', 'a', 'a', 'a', 'a', 'b', 'b', 'b'],
                                  ['b', 'b', 'b', 'a', 'a', 'a', 'a', 'b', 'b', 'b'],
                                  ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
                                  ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
                                  ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']])

        ob.create_object_plot(test_matrix, 1, 1, (255, 0, 0))

        for y, row in enumerate(test_matrix):
            for x, point in enumerate(row):

                self.assertEqual(point, ob.matrix[y, x])

        for y, row in enumerate(test_ref_plot):
            for x, point in enumerate(row):
                self.assertEqual(point, ob.ref_plot[y, x])

        self.assertEqual((255, 0, 0), ob.colour)
        self.assertEqual(1, ob.ob_id)
        self.assertEqual(1, ob.col_num)

    def test_process_matrix(self):
        matrix = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 2, 2, 2, 2, 0, 0, 0],
                           [0, 0, 0, 2, 2, 2, 2, 0, 0, 0],
                           [0, 0, 0, 2, 2, 2, 2, 0, 0, 0],
                           [0, 0, 0, 2, 2, 2, 2, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

        test_matrix = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                                [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                                [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                                [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        self.object_ob.matrix = matrix

        self.object_ob.process_matrix()

        for y, row in enumerate(test_matrix):
            for x, point in enumerate(row):
                self.assertEqual(point, self.object_ob.matrix[y, x])

    def test_outline_running_stitch(self):
        test_matrix = np.array([[0, 0, 0, 0, 0],
                                [0, 1, 1, 1, 0],
                                [0, 1, 1, 1, 0],
                                [0, 1, 1, 1, 0],
                                [0, 0, 0, 0, 0]])

        test_list = [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (2, 1), (1, 1), (1, 2)]

        self.object_ob.matrix = test_matrix
        self.object_ob.outline_running_stitch()
        self.assertEqual(test_list, self.object_ob.stitch_list)

    def test_running_stitch_fill(self):
        test_matrix = np.array([[0, 0, 0, 0, 0, 0],
                                [0, 1, 1, 1, 1, 0],
                                [0, 1, 1, 1, 1, 0],
                                [0, 1, 1, 1, 1, 0],
                                [0, 1, 1, 1, 1, 0],
                                [0, 0, 0, 0, 0, 0]])

        test_list = [(1, 1), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4),
                     (4, 3), (4, 2), (4, 1), (3, 1), (2, 1), (2, 2), (2, 3), (3, 3), (3, 2)]

        self.object_ob.matrix = test_matrix
        self.object_ob.running_stitch_fill(None)
        self.assertEqual(test_list, self.object_ob.stitch_list)

    def test_fill_stitch_fill(self):
        test_matrix = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

        test_list = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8),
                     (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8),
                     (8, 7), (8, 6), (8, 5), (8, 4), (8, 3), (8, 2), (8, 1),
                     (7, 1), (6, 1), (5, 1), (4, 1), (3, 1), (2, 1),

                     (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2),
                     (8, 3),
                     (8, 4), (7, 4), (6, 4), (5, 4), (4, 4), (3, 4), (2, 4), (1, 4),
                     (1, 5),
                     (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6),
                     (8, 7),
                     (8, 8), (7, 8), (6, 8), (5, 8), (4, 8), (3, 8), (2, 8), (1, 8),

                     (1, 7), (1, 6), (1, 5), (1, 4), (1, 3), (1, 2),

                     (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8),
                     (2, 8), (2, 7), (2, 6), (2, 5), (2, 4), (2, 3), (2, 2), (2, 1),
                     (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8),
                     (4, 8), (4, 7), (4, 6), (4, 5), (4, 4), (4, 3), (4, 2), (4, 1),
                     (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8),
                     (6, 8), (6, 7), (6, 6), (6, 5), (6, 4), (6, 3), (6, 2), (6, 1),
                     (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8),
                     (8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (8, 3), (8, 2), (8, 1)]

        self.object_ob.matrix = test_matrix
        self.object_ob.fill_stitch_fill(None)
        self.assertEqual(test_list, self.object_ob.stitch_list)


if __name__ == '__main__':
    unittest.main()

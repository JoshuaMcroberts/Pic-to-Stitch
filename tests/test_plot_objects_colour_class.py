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
        self.colour_ob = po.ColourPlot()
        row = [0] * 10
        matrix = np.array([row] * 10)
        self.colour_ob.matrix = matrix
        self.colour_ob.col_num = 1
        self.colour_ob.ref_plot = matrix
        self.colour_ob.object_count = 4
        self.colour_ob.colour = (23, 212, 43)
        self.colour_ob.ob_matrix_list = [1, 2, 3, 4, 5]

    def tearDown(self):
        pass

    def test_ColourPlot__init__(self):
        plot = po.ColourPlot()
        self.assertFalse(plot.matrix)
        self.assertFalse(plot.col_num)
        self.assertFalse(plot.ref_plot)
        self.assertFalse(plot.object_count)
        self.assertFalse(plot.colour)
        self.assertFalse(plot.ob_matrix_list)

    def test_set_matrix(self):
        test_matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        row = [1] * 10
        matrix = np.array([row] * 10)

        self.colour_ob.set_matrix(matrix)
        for y, row in enumerate(test_matrix):
            for x, point in enumerate(row):
                self.assertEqual(point, self.colour_ob.matrix[y, x])

    def test_set_col_num(self):
        self.colour_ob.set_col_num(12)
        self.assertEqual(12, self.colour_ob.col_num)

    def test_set_ref_plot(self):
        test_matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        row = [1] * 10
        matrix = np.array([row] * 10)

        self.colour_ob.set_ref_plot(matrix)
        for y, row in enumerate(test_matrix):
            for x, point in enumerate(row):
                self.assertEqual(point, self.colour_ob.ref_plot[y, x])

    def test_set_object_count(self):
        self.colour_ob.set_object_count(10)
        self.assertEqual(10, self.colour_ob.object_count)

    def test_set_colour(self):
        self.colour_ob.set_colour((10, 234, 0))
        self.assertEqual((10, 234, 0), self.colour_ob.colour)

    def test_set_ob_matrix_list(self):
        self.colour_ob.set_ob_matrix_list(["a", "b", "c", "d"])
        self.assertEqual(["a", "b", "c", "d"], self.colour_ob.ob_matrix_list)

    def test_get_matrix(self):
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
        matrix = self.colour_ob.get_matrix()
        for y, row in enumerate(test_matrix):
            for x, point in enumerate(row):
                self.assertEqual(point, matrix[y, x])

    def test_get_col_num(self):
        col_num = self.colour_ob.get_col_num()
        self.assertEqual(1, col_num)

    def test_get_ref_plot(self):
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
        ref_plot = self.colour_ob.get_ref_plot()
        for y, row in enumerate(test_matrix):
            for x, point in enumerate(row):
                self.assertEqual(point, ref_plot[y, x])

    def test_get_object_count(self):
        object_count = self.colour_ob.get_object_count()
        self.assertEqual(4, object_count)

    def test_get_colour(self):
        colour = self.colour_ob.get_colour()
        self.assertEqual((23,212, 43), colour)

    def test_get_ob_matrix_list(self):
        ob_matrix_list = self.colour_ob.get_ob_matrix_list()
        self.assertEqual([1, 2, 3, 4, 5], ob_matrix_list)

    def test_create_colour_plot(self):
        test_matrix = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                                [1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
                                [1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
                                [1, 2, 3, 4, 3, 4, 4, 3, 2, 1],
                                [1, 2, 3, 4, 2, 1, 4, 3, 2, 1],
                                [1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
                                [1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
                                [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

        test_ref_plot = np.array([['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
                                  ['1', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', '1'],
                                  ['1', 'a', '3', '3', '3', '3', '3', '3', 'a', '1'],
                                  ['1', 'a', '3', '4', '4', '4', '4', '3', 'a', '1'],
                                  ['1', 'a', '3', '4', '3', '4', '4', '3', 'a', '1'],
                                  ['1', 'a', '3', '4', 'a', '1', '4', '3', 'a', '1'],
                                  ['1', 'a', '3', '4', '4', '4', '4', '3', 'a', '1'],
                                  ['1', 'a', '3', '3', '3', '3', '3', '3', 'a', '1'],
                                  ['1', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', '1'],
                                  ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']])

        self.colour_ob.create_colour_plot(test_matrix, 2, (23, 54, 10))

        for y, row in enumerate(test_matrix):
            for x, point in enumerate(row):
                self.assertEqual(point, self.colour_ob.matrix[y, x])

        self.assertEqual(2, self.colour_ob.col_num)

        for y, row in enumerate(test_ref_plot):
            for x, point in enumerate(row):
                self.assertEqual(point, self.colour_ob.ref_plot[y, x])

        self.assertEqual(0, self.colour_ob.object_count)
        self.assertEqual((23, 54, 10), self.colour_ob.colour)
        self.assertFalse(self.colour_ob.ob_matrix_list)

    def test_create_ref_plot(self):

        test_m_1 = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                             [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

        test_m_2 = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 2, 2, 2, 2, 2, 2, 2, 2, 0],
                             [0, 2, 0, 0, 0, 0, 0, 0, 2, 0],
                             [0, 2, 0, 0, 0, 0, 0, 0, 2, 0],
                             [0, 2, 0, 0, 0, 0, 0, 0, 2, 0],
                             [0, 2, 0, 0, 2, 0, 0, 0, 2, 0],
                             [0, 2, 0, 0, 0, 0, 0, 0, 2, 0],
                             [0, 2, 0, 0, 0, 0, 0, 0, 2, 0],
                             [0, 2, 2, 2, 2, 2, 2, 2, 2, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

        test_out_1 = np.array([['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
                               ['a', '0', '0', '0', '0', '0', '0', '0', '0', 'a'],
                               ['a', '0', '0', '0', '0', '0', '0', '0', '0', 'a'],
                               ['a', '0', '0', '0', '0', '0', '0', '0', '0', 'a'],
                               ['a', '0', '0', '0', '0', '0', '0', '0', '0', 'a'],
                               ['a', '0', '0', '0', '0', 'a', '0', '0', '0', 'a'],
                               ['a', '0', '0', '0', '0', '0', '0', '0', '0', 'a'],
                               ['a', '0', '0', '0', '0', '0', '0', '0', '0', 'a'],
                               ['a', '0', '0', '0', '0', '0', '0', '0', '0', 'a'],
                               ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']])

        test_out_2 = np.array([['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                               ['0', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', '0'],
                               ['0', 'a', '0', '0', '0', '0', '0', '0', 'a', '0'],
                               ['0', 'a', '0', '0', '0', '0', '0', '0', 'a', '0'],
                               ['0', 'a', '0', '0', '0', '0', '0', '0', 'a', '0'],
                               ['0', 'a', '0', '0', 'a', '0', '0', '0', 'a', '0'],
                               ['0', 'a', '0', '0', '0', '0', '0', '0', 'a', '0'],
                               ['0', 'a', '0', '0', '0', '0', '0', '0', 'a', '0'],
                               ['0', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', '0'],
                               ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']])

        self.colour_ob.matrix = test_m_1
        self.colour_ob.col_num = 1
        ref_plot = self.colour_ob.create_ref_plot(0)

        for y, row in enumerate(test_out_1):
            for x, point in enumerate(row):
                self.assertEqual(point, ref_plot[y, x])

        self.colour_ob.matrix = test_m_2
        self.colour_ob.col_num = 2
        ref_plot = self.colour_ob.create_ref_plot(0)

        for y, row in enumerate(test_out_2):
            for x, point in enumerate(row):
                self.assertEqual(point, ref_plot[y, x])

    def test_process_colour_plot(self):

        test_main_plot = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                   [1, 1, 2, 2, 2, 2, 2, 2, 1, 1],
                                   [1, 1, 2, 2, 2, 2, 2, 2, 1, 1],
                                   [1, 1, 2, 2, 1, 1, 2, 2, 1, 1],
                                   [1, 1, 2, 2, 1, 1, 2, 2, 1, 1],
                                   [1, 1, 2, 2, 2, 2, 2, 2, 1, 1],
                                   [1, 1, 2, 2, 2, 2, 2, 2, 1, 1],
                                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

        test_ref_plot = np.array([['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                  ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                  ['0', '0', 'a', 'a', 'a', 'a', 'a', 'a', '0', '0'],
                                  ['0', '0', 'a', 'a', 'a', 'a', 'a', 'a', '0', '0'],
                                  ['0', '0', 'a', 'a', '0', '0', 'a', 'a', '0', '0'],
                                  ['0', '0', 'a', 'a', '0', '0', 'a', 'a', '0', '0'],
                                  ['0', '0', 'a', 'a', 'a', 'a', 'a', 'a', '0', '0'],
                                  ['0', '0', 'a', 'a', 'a', 'a', 'a', 'a', '0', '0'],
                                  ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                  ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']])

        test_out_plot = np.array([['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                  ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                  ['0', '0', '1', '1', '1', '1', '1', '1', '0', '0'],
                                  ['0', '0', '1', '1', '1', '1', '1', '1', '0', '0'],
                                  ['0', '0', '1', '1', '0', '0', '1', '1', '0', '0'],
                                  ['0', '0', '1', '1', '0', '0', '1', '1', '0', '0'],
                                  ['0', '0', '1', '1', '1', '1', '1', '1', '0', '0'],
                                  ['0', '0', '1', '1', '1', '1', '1', '1', '0', '0'],
                                  ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                  ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']])

        self.colour_ob.set_ref_plot(test_ref_plot)
        self.colour_ob.set_col_num(2)
        self.colour_ob.process_colour_plot(None, 2, test_main_plot)

        for y, row in enumerate(test_out_plot):
            for x, point in enumerate(row):
                self.assertEqual(point, self.colour_ob.ref_plot[y,x])

    def test_create_object_count(self):
        test_ref_plot = np.array([['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                  ['0', '1', '1', '1', '0', '0', '0', '0', '0', '0'],
                                  ['0', '1', '1', '1', '0', '2', '2', '2', '0', '0'],
                                  ['0', '1', '1', '1', '0', '2', '2', '2', '0', '0'],
                                  ['0', '0', '0', '0', '0', '2', '2', '2', '0', '0'],
                                  ['0', '0', '3', '3', '3', '0', '0', '0', '0', '0'],
                                  ['0', '0', '3', '3', '3', '0', '4', '4', '4', '0'],
                                  ['0', '0', '3', '3', '3', '0', '4', '4', '4', '0'],
                                  ['0', '0', '0', '0', '0', '0', '4', '4', '4', '0'],
                                  ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']])

        self.colour_ob.set_ref_plot(test_ref_plot)
        count_val = self.colour_ob.create_object_count()
        self.assertEqual(4, count_val)

    def test_create_object_sub_plot(self):
        test_matrix = np.array([['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                                ['0', '1', '1', '1', '0', '0', '0', '0', '0', '0'],
                                ['0', '1', '1', '1', '0', '2', '2', '2', '0', '0'],
                                ['0', '1', '1', '1', '0', '2', '2', '2', '0', '0'],
                                ['0', '0', '0', '0', '0', '2', '2', '2', '0', '0'],
                                ['0', '0', '3', '3', '3', '0', '0', '0', '0', '0'],
                                ['0', '0', '3', '3', '3', '0', '4', '4', '4', '0'],
                                ['0', '0', '3', '3', '3', '0', '4', '4', '4', '0'],
                                ['0', '0', '0', '0', '0', '0', '4', '4', '4', '0'],
                                ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']])

        test_m_1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        test_m_2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 2, 2, 2, 0, 0],
                    [0, 0, 0, 0, 0, 2, 2, 2, 0, 0],
                    [0, 0, 0, 0, 0, 2, 2, 2, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        test_m_3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 3, 3, 3, 0, 0, 0, 0, 0],
                    [0, 0, 3, 3, 3, 0, 0, 0, 0, 0],
                    [0, 0, 3, 3, 3, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        test_m_4 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 4, 4, 4, 0],
                    [0, 0, 0, 0, 0, 0, 4, 4, 4, 0],
                    [0, 0, 0, 0, 0, 0, 4, 4, 4, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        matrix_list = [test_m_1, test_m_2, test_m_3, test_m_4]

        self.colour_ob.ob_matrix_list.clear()
        self.colour_ob.ref_plot = test_matrix
        self.colour_ob.colour = (234, 12, 56)

        self.colour_ob.create_object_sub_plot()

        for i, test_m in enumerate(matrix_list):
            out_ob = self.colour_ob.ob_matrix_list[i]
            out_matrix = out_ob.matrix

            for y, row in enumerate(test_m):
                for x, point in enumerate(row):

                    self.assertEqual(point, out_matrix[y, x])
            self.assertEqual((234, 12, 56), out_ob.colour)
            self.assertEqual(i + 1, out_ob.col_num)
            self.assertEqual(i + 1, out_ob.ob_id)


if __name__ == '__main__':
    unittest.main()

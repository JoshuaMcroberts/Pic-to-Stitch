import unittest
from unittest import mock
import numpy as np
import sys
sys.path.append('../pic_to_stitch/')

from pic_to_stitch import plot_objects as po


class TestPlotObjectsPlotClass(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        self.plot_ob = po.Plot()
        row = [0] * 10
        matrix = np.array([row] * 10)
        self.plot_ob.matrix = matrix
        self.plot_ob.col_list = [(180, 154, 67), (120, 254, 0), (20, 90, 0), (243, 45, 123)]
        self.plot_ob.col_amount = 4
        self.plot_ob.matrix_width = 10
        self.plot_ob.matrix_height = 10
        self.plot_ob.col_matrix_list = [1, 2, 3, 4, 5]

    def tearDown(self):
        pass

    def test_Plot__init__(self):
        plot = po.Plot()
        self.assertFalse(plot.matrix)
        self.assertFalse(plot.col_list)
        self.assertFalse(plot.col_amount)
        self.assertFalse(plot.matrix_width)
        self.assertFalse(plot.matrix_height)
        self.assertFalse(plot.col_matrix_list)

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

        self.plot_ob.set_matrix(matrix)
        for y, row in enumerate(test_matrix):
            for x, point in enumerate(row):
                self.assertEqual(point, self.plot_ob.matrix[y, x])

    def test_set_col_list(self):
        col_list = [(12, 123, 2), (34, 123, 72), (0, 0, 0), (255, 255, 255)]

        self.plot_ob.set_col_list(col_list)
        self.assertEqual([(12, 123, 2), (34, 123, 72), (0, 0, 0), (255, 255, 255)], self.plot_ob.col_list)

    def test_set_col_amount(self):
        self.plot_ob.set_col_amount(12)
        self.assertEqual(12, self.plot_ob.col_amount)

    def test_set_matrix_width(self):
        self.plot_ob.set_matrix_width(10)
        self.assertEqual(10, self.plot_ob.matrix_width)

    def test_set_matrix_height(self):
        self.plot_ob.set_matrix_height(10)
        self.assertEqual(10, self.plot_ob.matrix_height)

    def test_set_col_matrix_list(self):
        self.plot_ob.set_col_matrix_list(["a", "b", "c", "d"])
        self.assertEqual(["a", "b", "c", "d"], self.plot_ob.col_matrix_list)

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
        matrix = self.plot_ob.get_matrix()
        for y, row in enumerate(test_matrix):
            for x, point in enumerate(row):
                self.assertEqual(point, matrix[y, x])

    def test_get_col_list(self):
        col_list = self.plot_ob.get_col_list()
        self.assertEqual([(180, 154, 67), (120, 254, 0), (20, 90, 0), (243, 45, 123)], col_list)

    def test_get_col_amount(self):
        col_amount = self.plot_ob.get_col_amount()
        self.assertEqual(4, col_amount)

    def test_get_matrix_width(self):
        matrix_width = self.plot_ob.get_matrix_width()
        self.assertEqual(10, matrix_width)

    def test_get_matrix_height(self):
        matrix_height = self.plot_ob.get_matrix_height()
        self.assertEqual(10, matrix_height)

    def test_get_col_matrix_list(self):
        col_matrix_list = self.plot_ob.get_col_matrix_list()
        self.assertEqual([1, 2, 3, 4, 5], col_matrix_list)

    def test_create_sub_plot(self):
        test_matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                       [1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
                       [1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
                       [1, 2, 3, 4, 3, 4, 4, 3, 2, 1],
                       [1, 2, 3, 4, 2, 1, 4, 3, 2, 1],
                       [1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
                       [1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
                       [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        test_m_1 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        test_m_2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 2, 2, 2, 2, 2, 2, 2, 2, 0],
                    [0, 2, 0, 0, 0, 0, 0, 0, 2, 0],
                    [0, 2, 0, 0, 0, 0, 0, 0, 2, 0],
                    [0, 2, 0, 0, 0, 0, 0, 0, 2, 0],
                    [0, 2, 0, 0, 2, 0, 0, 0, 2, 0],
                    [0, 2, 0, 0, 0, 0, 0, 0, 2, 0],
                    [0, 2, 0, 0, 0, 0, 0, 0, 2, 0],
                    [0, 2, 2, 2, 2, 2, 2, 2, 2, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        test_m_3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 3, 3, 3, 3, 3, 3, 0, 0],
                    [0, 0, 3, 0, 0, 0, 0, 3, 0, 0],
                    [0, 0, 3, 0, 3, 0, 0, 3, 0, 0],
                    [0, 0, 3, 0, 0, 0, 0, 3, 0, 0],
                    [0, 0, 3, 0, 0, 0, 0, 3, 0, 0],
                    [0, 0, 3, 3, 3, 3, 3, 3, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        test_m_4 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 4, 4, 4, 4, 0, 0, 0],
                    [0, 0, 0, 4, 0, 4, 4, 0, 0, 0],
                    [0, 0, 0, 4, 0, 0, 4, 0, 0, 0],
                    [0, 0, 0, 4, 4, 4, 4, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        matrix_list = [test_m_1, test_m_2, test_m_3, test_m_4]

        test_col_list = [(180, 154, 67), (120, 254, 0), (20, 90, 0), (243, 45, 123)]
        self.plot_ob.col_matrix_list.clear()
        self.plot_ob.matrix = test_matrix
        self.plot_ob.create_sub_plot(None)

        for i, ob in enumerate(self.plot_ob.col_matrix_list):
            self.assertEqual(i + 1, ob.col_num)
            self.assertEqual(test_col_list[i], ob.colour)

            test_m = matrix_list[i]
            for y, row in enumerate(test_m):
                for x, point in enumerate(row):

                    self.assertEqual(point, ob.matrix[y, x])

if __name__ == '__main__':
    unittest.main()

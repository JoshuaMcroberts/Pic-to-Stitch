import unittest
from unittest import mock
import numpy as np
import sys
sys.path.append('../pic_to_stitch/')

from pic_to_stitch import plot_objects as po


class TestPlotObjects(unittest.TestCase):

    def test_get_object_outline(self):
        test_matrix = np.array([[0, 0, 0, 0, 0],
                                [0, 1, 1, 1, 0],
                                [0, 1, 1, 1, 0],
                                [0, 1, 1, 1, 0],
                                [0, 0, 0, 0, 0]])

        test_list = [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (2, 1)]

        max_yx, min_yx, ind_list = po.get_object_outline(test_matrix, test_matrix, (1, 1), 8, 1, 1)

        self.assertEqual(test_list, ind_list)
        self.assertEqual((3, 3), max_yx)
        self.assertEqual((1, 1), min_yx)

    def test_get_object_outline_fill(self):
        test_matrix = np.array([[0, 0, 0, 0, 0, 0],
                                [0, 1, 1, 1, 1, 0],
                                [0, 1, 1, 1, 1, 0],
                                [0, 1, 1, 1, 1, 0],
                                [0, 1, 1, 1, 1, 0],
                                [0, 0, 0, 0, 0, 0]])

        test_list = [(23, 34), (1, 1), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4),
                     (4, 3), (4, 2), (4, 1), (3, 1), (2, 1), (2, 2), (2, 3), (3, 3), (3, 2)]

        ind_list = [(23, 34)]

        ind_list = po.get_object_outline_fill(None, test_matrix, test_matrix, (1, 1), 8, 4, 1, ind_list)

        self.assertEqual(test_list, ind_list)

    def test_get_object_fill_stitch(self):

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

        test_template = np.array([['2', '0', '2', '0', '2', '0', '2', '0', '2', '0'],
                                  ['2', '0', '2', '0', '2', '0', '2', '0', '2', '0'],
                                  ['2', '0', '2', '0', '2', '0', '2', '0', '2', '0'],
                                  ['2', '0', '2', '0', '2', '0', '2', '0', '2', '0'],
                                  ['2', '0', '2', '0', '2', '0', '2', '0', '2', '0'],
                                  ['2', '0', '2', '0', '2', '0', '2', '0', '2', '0'],
                                  ['2', '0', '2', '0', '2', '0', '2', '0', '2', '0'],
                                  ['2', '0', '2', '0', '2', '0', '2', '0', '2', '0'],
                                  ['2', '0', '2', '0', '2', '0', '2', '0', '2', '0'],
                                  ['2', '0', '2', '0', '2', '0', '2', '0', '2', '0']])

        test_list = [(23, 34),

                     (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2),
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

        ind_list = [(23, 34)]

        ind_list = po.get_object_fill_stitch(None, test_template, test_matrix, (1, 2), (8, 8), (1, 1), ind_list)

        self.assertEqual(test_list, ind_list)

    def test_compare_plots(self):
        in_matrix = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

        in_template = np.array([['2', '0', '2', '0', '2', '0', '2', '0', '2', '0'],
                                ['2', '0', '2', '0', '2', '0', '2', '0', '2', '0'],
                                ['2', '0', '2', '0', '2', '0', '2', '0', '2', '0'],
                                ['2', '0', '2', '0', '2', '0', '2', '0', '2', '0'],
                                ['2', '0', '2', '0', '2', '0', '2', '0', '2', '0'],
                                ['2', '0', '2', '0', '2', '0', '2', '0', '2', '0'],
                                ['2', '0', '2', '0', '2', '0', '2', '0', '2', '0'],
                                ['2', '0', '2', '0', '2', '0', '2', '0', '2', '0'],
                                ['2', '0', '2', '0', '2', '0', '2', '0', '2', '0'],
                                ['2', '0', '2', '0', '2', '0', '2', '0', '2', '0']])

        test_plot = np.array([['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                              ['0', '0', '1', '0', '1', '0', '1', '0', '1', '0'],
                              ['0', '0', '1', '0', '1', '0', '1', '0', '1', '0'],
                              ['0', '0', '1', '0', '1', '0', '1', '0', '1', '0'],
                              ['0', '0', '1', '0', '1', '0', '1', '0', '1', '0'],
                              ['0', '0', '1', '0', '1', '0', '1', '0', '1', '0'],
                              ['0', '0', '1', '0', '1', '0', '1', '0', '1', '0'],
                              ['0', '0', '1', '0', '1', '0', '1', '0', '1', '0'],
                              ['0', '0', '1', '0', '1', '0', '1', '0', '1', '0'],
                              ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']])

        out_plot = po.compare_plots(in_matrix, 1, in_template, "2")

        for y, row in enumerate(test_plot):
            for x, point in enumerate(row):
                self.assertEqual(point, out_plot[y, x])

    def test_find_path(self):
        in_matrix = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        test_list = [(2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 6)]
        ind_list = []
        h, ind_list = po.find_path(in_matrix, (8, 6), (1, 1), ind_list)

        self.assertEqual(test_list, ind_list)
        self.assertEqual(90, h)

    def test_next_point(self):
        start_a = po.next_point((0, 0), (-4, -3))
        start_b = po.next_point((0, 0), (-45, 0))
        start_c = po.next_point((0, 0), (-2, 9))
        start_d = po.next_point((0, 0), (0, 3))
        start_e = po.next_point((0, 0), (3, 56))
        start_f = po.next_point((0, 0), (34, 0))
        start_g = po.next_point((0, 0), (3, -7))
        start_h = po.next_point((0, 0), (0, -2))

        self.assertEqual(1, start_a)
        self.assertEqual(2, start_b)
        self.assertEqual(3, start_c)
        self.assertEqual(4, start_d)
        self.assertEqual(5, start_e)
        self.assertEqual(6, start_f)
        self.assertEqual(7, start_g)
        self.assertEqual(8, start_h)

    def test_reversible_mine_sweeper_fill(self):

        in_matrix = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

        in_ref = np.array([['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                           ['0', '1', '1', '1', '1', '1', '1', '1', '1', '0'],
                           ['0', '1', 'a', 'a', 'a', 'a', 'a', 'a', '1', '0'],
                           ['0', '1', 'a', 'a', 'a', 'a', 'a', 'a', '1', '0'],
                           ['0', '1', 'a', 'a', 'a', 'a', 'a', 'a', '1', '0'],
                           ['0', '1', 'a', 'a', 'a', 'a', 'a', 'a', '1', '0'],
                           ['0', '1', 'a', 'a', 'a', 'a', 'a', 'a', '1', '0'],
                           ['0', '1', 'a', 'a', 'a', 'a', 'a', 'a', '1', '0'],
                           ['0', '1', '1', '1', '1', '1', '1', '1', '1', '0'],
                           ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']])

        test_ref = np.array([['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                             ['0', '1', '1', '1', '1', '1', '1', '1', '1', '0'],
                             ['0', '1', '1', '1', '1', '1', '1', '1', '1', '0'],
                             ['0', '1', '1', '1', '1', '1', '1', '1', '1', '0'],
                             ['0', '1', '1', '1', '1', '1', '1', '1', '1', '0'],
                             ['0', '1', '1', '1', '1', '1', '1', '1', '1', '0'],
                             ['0', '1', '1', '1', '1', '1', '1', '1', '1', '0'],
                             ['0', '1', '1', '1', '1', '1', '1', '1', '1', '0'],
                             ['0', '1', '1', '1', '1', '1', '1', '1', '1', '0'],
                             ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']])

        ref_plot = po.reversible_mine_sweeper_fill(in_matrix, in_ref, (8, 8), (1, 1), 1, 1, 1)

        for y, row in enumerate(test_ref):
            for x, point in enumerate(row):
                self.assertEqual(point, ref_plot[y, x])

    def test_check_for_number(self):
        test_m_1 = np.array([[0, 0, 0, 0, 0, 0],
                             [0, 1, 0, 0, 2, 0],
                             [0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0],
                             [0, 4, 0, 0, 3, 0],
                             [0, 0, 0, 0, 0, 0]])

        test_m_2 = np.array([['0', '0', '0', '0', '0'],
                             ['0', '1', '0', '2', '0'],
                             ['0', '0', '0', '0', '0'],
                             ['0', '5', '0', '3', '0'],
                             ['0', '0', '0', '0', '0']])

        output_1 = po.check_for_number(test_m_1, 1)
        output_2 = po.check_for_number(test_m_1, '2')
        output_3 = po.check_for_number(test_m_1, 9)
        output_4 = po.check_for_number(test_m_1, '10')
        output_5 = po.check_for_number(test_m_2, 5)
        output_6 = po.check_for_number(test_m_2, '1')
        output_7 = po.check_for_number(test_m_2, 11)
        output_8 = po.check_for_number(test_m_2, '22')

        self.assertEqual(output_1, (True, (1, 1)))
        self.assertEqual(output_2, (True, (1, 4)))
        self.assertEqual(output_3, (False, (0, 0)))
        self.assertEqual(output_4, (False, (0, 0)))
        self.assertEqual(output_5, (True, (3, 1)))
        self.assertEqual(output_6, (True, (1, 1)))
        self.assertEqual(output_7, (False, (0, 0)))
        self.assertEqual(output_8, (False, (0, 0)))

    def test_valid_position(self):

        in_matrix = np.array([[0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
                              [0, 1, 1, 1, 1, 2, 1, 1, 1, 0],
                              [0, 1, 1, 1, 2, 1, 1, 1, 1, 0],
                              [0, 1, 1, 2, 1, 1, 1, 1, 1, 0],
                              [2, 2, 2, 1, 1, 1, 1, 1, 1, 0],
                              [1, 3, 1, 1, 1, 3, 3, 3, 3, 3],
                              [3, 1, 3, 1, 1, 1, 1, 1, 1, 0],
                              [3, 1, 1, 3, 3, 1, 1, 1, 1, 0],
                              [1, 1, 1, 1, 3, 1, 1, 1, 1, 0],
                              [1, 3, 3, 3, 1, 0, 0, 0, 0, 0]])

        answer_1 = po.valid_position(in_matrix, 3, 3, 1, 2)
        answer_2 = po.valid_position(in_matrix, 3, 4, 2, 1)
        answer_3 = po.valid_position(in_matrix, 5, 5, 1, 3)
        answer_4 = po.valid_position(in_matrix, 5, 4, 3, 1)
        answer_5 = po.valid_position(in_matrix, 7, 2, 1, 3)

        self.assertEqual(answer_1, 2)
        self.assertEqual(answer_2, 1)
        self.assertEqual(answer_3, 2)
        self.assertEqual(answer_4, 1)
        self.assertEqual(answer_5, 2)

    def test_get_surrounding_points(self):

        plot = np.array([[1, 2, 2],
                         [1, 2, 2],
                         [1, 1, 1]])

        out_plot = np.array([[1, 2, 3],
                             [8, 0, 4],
                             [7, 6, 5]])

        points_1 = po.get_surrounding_points(plot, out_plot, 1, 1, 2)
        points_2 = po.get_surrounding_points(plot, out_plot, 0, 0, 1)
        points_3 = po.get_surrounding_points(plot, out_plot, 0, 1, 2)
        points_4 = po.get_surrounding_points(plot, out_plot, 0, 2, 2)
        points_5 = po.get_surrounding_points(plot, out_plot, 1, 0, 1)
        points_6 = po.get_surrounding_points(plot, out_plot, 1, 2, 2)
        points_7 = po.get_surrounding_points(plot, out_plot, 2, 0, 1)
        points_8 = po.get_surrounding_points(plot, out_plot, 2, 1, 1)
        points_9 = po.get_surrounding_points(plot, out_plot, 2, 2, 1)

        self.assertEqual([2, 1, 3, 6, 7, 5, 8, 4], points_1)
        self.assertEqual([8, 0, 2], points_2)
        self.assertEqual([0, 8, 4, 1, 3], points_3)
        self.assertEqual([4, 0, 2], points_4)
        self.assertEqual([1, 2, 7, 6, 0], points_5)
        self.assertEqual([3, 2, 5, 6, 0], points_6)
        self.assertEqual([8, 0, 6], points_7)
        self.assertEqual([0, 8, 4, 7, 5], points_8)
        self.assertEqual([4, 0, 6], points_9)

    def test_get_surrounding_points_5x5(self):

        n_matrix = np.array([[9, 10, 11, 12, 13],
                             [24,  1,  2,  3, 14],
                             [23,  8,  0,  4, 15],
                             [22,  7,  6,  5, 16],
                             [21, 20, 19, 18, 17]])

        points_1, yxs_1 = po.get_surrounding_points_5x5(n_matrix, 2, 2)
        points_2, yxs_2 = po.get_surrounding_points_5x5(n_matrix, 0, 0)
        points_3, yxs_3 = po.get_surrounding_points_5x5(n_matrix, 0, 1)
        points_4, yxs_4 = po.get_surrounding_points_5x5(n_matrix, 0, 2)
        points_5, yxs_5 = po.get_surrounding_points_5x5(n_matrix, 0, 3)
        points_6, yxs_6 = po.get_surrounding_points_5x5(n_matrix, 0, 4)
        points_7, yxs_7 = po.get_surrounding_points_5x5(n_matrix, 1, 0)
        points_8, yxs_8 = po.get_surrounding_points_5x5(n_matrix, 1, 1)
        points_9, yxs_9 = po.get_surrounding_points_5x5(n_matrix, 1, 2)
        points_10, yxs_10 = po.get_surrounding_points_5x5(n_matrix, 1, 3)
        points_11, yxs_11 = po.get_surrounding_points_5x5(n_matrix, 1, 4)
        points_12, yxs_12 = po.get_surrounding_points_5x5(n_matrix, 2, 0)
        points_13, yxs_13 = po.get_surrounding_points_5x5(n_matrix, 2, 1)
        points_14, yxs_14 = po.get_surrounding_points_5x5(n_matrix, 2, 3)
        points_15, yxs_15 = po.get_surrounding_points_5x5(n_matrix, 2, 4)
        points_16, yxs_16 = po.get_surrounding_points_5x5(n_matrix, 3, 0)
        points_17, yxs_17 = po.get_surrounding_points_5x5(n_matrix, 3, 1)
        points_18, yxs_18 = po.get_surrounding_points_5x5(n_matrix, 3, 2)
        points_19, yxs_19 = po.get_surrounding_points_5x5(n_matrix, 3, 3)
        points_20, yxs_20 = po.get_surrounding_points_5x5(n_matrix, 3, 4)
        points_21, yxs_21 = po.get_surrounding_points_5x5(n_matrix, 4, 0)
        points_22, yxs_22 = po.get_surrounding_points_5x5(n_matrix, 4, 1)
        points_23, yxs_23 = po.get_surrounding_points_5x5(n_matrix, 4, 2)
        points_24, yxs_24 = po.get_surrounding_points_5x5(n_matrix, 4, 3)
        points_25, yxs_25 = po.get_surrounding_points_5x5(n_matrix, 4, 4)

        test_1 = [0, 11, 9, 10, 13, 12, 2, 24, 1, 14, 3, 19, 21, 20, 17, 18, 6, 22, 7, 16, 5, 23, 8, 15, 4]
        test_2 = [9, 23, 0, 8, 24, 2, 1, 11, 10]
        test_3 = [10, 8, 23, 4, 0, 1, 24, 3, 2, 9, 12, 11]
        test_4 = [11, 0, 23, 8, 15, 4, 2, 24, 1, 14, 3, 9, 10, 13, 12]
        test_5 = [12, 4, 8, 0, 15, 3, 1, 2, 14, 10, 11, 13]
        test_6 = [13, 15, 0, 4, 14, 2, 3, 11, 12]
        test_7 = [24, 9, 11, 10, 22, 6, 7, 23, 0, 8, 2, 1]
        test_8 = [1, 10, 9, 12, 11, 7, 22, 5, 6, 8, 23, 4, 0, 24, 3, 2]
        test_9 = [2, 11, 9, 10, 13, 12, 6, 22, 7, 16, 5, 0, 23, 8, 15, 4, 24, 1, 14, 3]
        test_10 = [3, 12, 10, 11, 13, 5, 7, 6, 16, 4, 8, 0, 15, 1, 2, 14]
        test_11 = [14, 13, 11, 12, 16, 6, 5, 15, 0, 4, 2, 3]
        test_12 = [23, 9, 11, 10, 24, 2, 1, 21, 19, 20, 22, 6, 7, 0, 8]
        test_13 = [8, 10, 9, 12, 11, 1, 24, 3, 2, 20, 21, 18, 19, 7, 22, 5, 6, 23, 4, 0]
        test_14 = [4, 12, 10, 11, 13, 3, 1, 2, 14, 18, 20, 19, 17, 5, 7, 6, 16, 8, 0, 15]
        test_15 = [15, 13, 11, 12, 14, 2, 3, 17, 19, 18, 16, 6, 5, 0, 4]
        test_16 = [22, 24, 2, 1, 23, 0, 8, 21, 19, 20, 6, 7]
        test_17 = [7, 1, 24, 3, 2, 8, 23, 4, 0, 20, 21, 18, 19, 22, 5, 6]
        test_18 = [6, 2, 24, 1, 14, 3, 0, 23, 8, 15, 4, 19, 21, 20, 17, 18, 22, 7, 16, 5]
        test_19 = [5, 3, 1, 2, 14, 4, 8, 0, 15, 18, 20, 19, 17, 7, 6, 16]
        test_20 = [16, 14, 2, 3, 15, 0, 4, 17, 19, 18, 6, 5]
        test_21 = [21, 23, 0, 8, 22, 6, 7, 19, 20]
        test_22 = [20, 8, 23, 4, 0, 7, 22, 5, 6, 21, 18, 19]
        test_23 = [19, 0, 23, 8, 15, 4, 6, 22, 7, 16, 5, 21, 20, 17, 18]
        test_24 = [18, 4, 8, 0, 15, 5, 7, 6, 16, 20, 19, 17]
        test_25 = [17, 15, 0, 4, 16, 6, 5, 19, 18]

        self.assertEqual(test_1, points_1)
        self.assertEqual(test_2, points_2)
        self.assertEqual(test_3, points_3)
        self.assertEqual(test_4, points_4)
        self.assertEqual(test_5, points_5)
        self.assertEqual(test_6, points_6)
        self.assertEqual(test_7, points_7)
        self.assertEqual(test_8, points_8)
        self.assertEqual(test_9, points_9)
        self.assertEqual(test_10, points_10)
        self.assertEqual(test_11, points_11)
        self.assertEqual(test_12, points_12)
        self.assertEqual(test_13, points_13)
        self.assertEqual(test_14, points_14)
        self.assertEqual(test_15, points_15)
        self.assertEqual(test_16, points_16)
        self.assertEqual(test_17, points_17)
        self.assertEqual(test_18, points_18)
        self.assertEqual(test_19, points_19)
        self.assertEqual(test_20, points_20)
        self.assertEqual(test_21, points_21)
        self.assertEqual(test_22, points_22)
        self.assertEqual(test_23, points_23)
        self.assertEqual(test_24, points_24)
        self.assertEqual(test_25, points_25)

    def test_count_list(self):
        points_co_or = [(23, 6), (-32, 4), (16, 40), (-32, 4), (-32, 4), (-32, 4), (23, 6), (23, 6), (23, 6), (23, 6),
                        (23, 6), (23, 6), (23, 6), (-32, 4), (-32, 4), (16, 40), (16, 40), (16, 40), (16, 40), (16, 40),
                        (16, 40), (16, 40), (16, 40), (-32, 4), (-32, 4), (-32, 4), (16, 40), (-32, 4)]

        points_num = [3, 1, 4, 5, 2, 5, 5, 4, 3, 5,
                       1, 3, 3, 3, 4, 1, 5, 3, 2, 3,
                       1, 5, 4, 4, 1, 4, 4, 2, 4, 5,
                       4, 5, 5, 3, 4, 5, 4, 5, 2, 1]

        test_co_or_vals = [(23, 6), (-32, 4), (16, 40)]
        test_num_vals = [3, 1, 4, 5, 2]
        test_co_or_amount = [8, 10, 10]
        test_num_amount = [8, 6, 11, 11, 4]

        out_vals_co_or, out_amount_co_or = po.count_list(points_co_or)

        out_vals_num, out_amount_num = po.count_list(points_num)

        self.assertEqual(test_co_or_vals, out_vals_co_or)
        self.assertEqual(test_co_or_amount, out_amount_co_or)
        self.assertEqual(test_num_vals, out_vals_num)
        self.assertEqual(test_num_amount, out_amount_num)

    def test_t_w_p_logic(self):

        val_list_1 = [1, 2, 3, 4]
        amount_list_1 = [10, 8, 3, 20]

        val_list_2 = [(3, 1), (-4, 20), (0, 14)]
        amount_list_2 = [10, 8, 20]

        answer_1 = po.t_w_p_logic(1, 2, val_list_1, amount_list_1)

        answer_2 = po.t_w_p_logic((-4, 20), (0, 14), val_list_2, amount_list_2)

        self.assertEqual(2, answer_1)
        self.assertEqual(1, answer_2)


if __name__ == '__main__':
    unittest.main()

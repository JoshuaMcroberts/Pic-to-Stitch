import unittest
import numpy as np
import os
import sys
sys.path.append('../Pic-to-Stitch/')

from pic_to_stitch import a_star_pathing as asp
from pic_to_stitch import plot_objects as po


class TestAStarPathing(unittest.TestCase):

    def setUp(self):
        self.node = asp.Node()
        self.node.h = 10
        self.node.g = 23
        self.node.f = 33
        self.node.l_point = (1, 2)
        self.node.co_or = (2, 3)

    def test__init__(self):
        new = asp.Node()
        self.assertFalse(new.h)
        self.assertFalse(new.g)
        self.assertFalse(new.f)
        self.assertFalse(new.l_point)
        self.assertFalse(new.co_or)

    def test_set_h(self):
        self.node.set_h(35)
        self.assertEqual(35, self.node.h)

    def test_set_g(self):
        self.node.set_g(43)
        self.assertEqual(43, self.node.g)

    def test_set_f(self):
        self.node.set_f(20)
        self.assertEqual(20, self.node.f)

    def test_set_l_point(self):
        self.node.set_l_point((3, 4))
        self.assertEqual((3, 4), self.node.l_point)

    def test_set_co_or(self):
        self.node.set_co_or((2, 1))
        self.assertEqual((2, 1), self.node.co_or)

    def test_get_h(self):
        h = self.node.get_h()
        self.assertEqual(10, h)

    def test_get_g(self):
        g = self.node.get_g()
        self.assertEqual(23, g)

    def test_get_f(self):
        f = self.node.get_f()
        self.assertEqual(33, f)

    def test_get_l_point(self):
        l_point = self.node.get_l_point()
        self.assertEqual((1, 2), l_point)

    def test_get_co_or(self):
        co_or = self.node.get_co_or()
        self.assertEqual((2, 3), co_or)

    def test_move_to_a_star(self):

        plot = np.array([[1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                         [1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
                         [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                         [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                         [0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
                         [1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                         [0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
                         [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                         [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                         [1, 0, 0, 0, 1, 0, 0, 0, 0, 0]])

        test_list = [(8, 3), (7, 3), (6, 3), (5, 4), (4, 5), (3, 6), (2, 7), (1, 8)]
        ind_list = []

        yx, ind_list = asp.move_to_a_star(None, plot, (1, 8), (9, 4), ind_list)

        self.assertEqual(test_list, ind_list)
        self.assertEqual((1, 8), yx)

    def test_set_node(self):
        plot = np.array([[1, 1, 1, 1, 1, 0, 2, 0, 0, 0],
                              [1, 1, 1, 1, 1, 2, 1, 1, 1, 0],
                              [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [2, 2, 2, 1, 1, 1, 1, 1, 1, 0],
                              [1, 3, 1, 1, 1, 3, 3, 3, 3, 3],
                              [3, 1, 3, 1, 3, 1, 1, 1, 1, 0],
                              [3, 1, 1, 1, 3, 1, 1, 1, 1, 0],
                              [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                              [1, 3, 3, 3, 1, 0, 0, 0, 0, 0]])
        asp.set_node(self.node, plot, (7, 3), (1, 8), 24, (8, 4))

        self.assertEqual(80, self.node.h)
        self.assertEqual(24, self.node.g)
        self.assertEqual(104, self.node.f)
        self.assertEqual((8, 4), self.node.l_point)

    def test_lowest_f(self):
        plot = np.array([[1, 1, 1, 1],
                         [1, 1, 1, 1],
                         [1, 2, 2, 1],
                         [1, 2, 2, 1],
                         [1, 2, 2, 1]])

        open_list = []

        node_a = asp.Node()
        node_a.h = 0
        node_a.f = 44
        open_list.append(node_a)

        node_b = asp.Node()
        node_b.h = 10
        node_b.f = 44
        open_list.append(node_b)

        node_c = asp.Node()
        node_c.h = 20
        node_c.f = 44
        open_list.append(node_c)

        node_d = asp.Node()
        node_d.h = 30
        node_d.f = 44
        open_list.append(node_d)

        node_e = asp.Node()
        node_e.h = 40
        node_e.f = 44
        open_list.append(node_e)

        node_f = asp.Node()
        node_f.h = 44
        node_f.f = 44
        open_list.append(node_f)

        node_g = asp.Node()
        node_g.h = 50
        node_g.f = 60
        open_list.append(node_g)

        cur_node = asp.lowest_f(open_list)

        self.assertEqual(node_a, cur_node)
        self.assertNotEqual(node_b, cur_node)

    def test_get_surrounding_nodes(self):
        node = asp.Node()

        p_row = [node] * 3  # create an matrix of nodes the same size as main_plot matrix
        node_plot = np.array([p_row] * 3)

        points_1 = asp.get_surrounding_nodes(node_plot, 1, 1)
        points_2 = asp.get_surrounding_nodes(node_plot, 0, 0)
        points_3 = asp.get_surrounding_nodes(node_plot, 0, 1)
        points_4 = asp.get_surrounding_nodes(node_plot, 0, 2)
        points_5 = asp.get_surrounding_nodes(node_plot, 1, 0)
        points_6 = asp.get_surrounding_nodes(node_plot, 1, 2)
        points_7 = asp.get_surrounding_nodes(node_plot, 2, 0)
        points_8 = asp.get_surrounding_nodes(node_plot, 2, 1)
        points_9 = asp.get_surrounding_nodes(node_plot, 2, 2)

        test_list_1 = [(0, 1, 10, (1, 1)), (0, 0, 14, (1, 1)), (0, 2, 14, (1, 1)), (2, 1, 10, (1, 1)),
                       (2, 0, 14, (1, 1)), (2, 2, 14, (1, 1)), (1, 0, 10, (1, 1)), (1, 2, 10, (1, 1))]

        test_list_2 = [(1, 0, 10, (0, 0)), (1, 1, 14, (0, 0)), (0, 1, 10, (0, 0))]  # [8, 0, 2]

        test_list_3 = [(1, 1, 10, (0, 1)), (1, 0, 14, (0, 1)), (1, 2, 14, (0, 1)), (0, 0, 10, (0, 1)),
                       (0, 2, 10, (0, 1))]  # [0, 8, 4, 1, 3]

        test_list_4 = [(1, 2, 10, (0, 2)), (1, 1, 14, (0, 2)), (0, 1, 10, (0, 2))]  # [4, 0, 2]

        test_list_5 = [(0, 0, 10, (1, 0)), (0, 1, 14, (1, 0)), (2, 0, 10, (1, 0)), (2, 1, 14, (1, 0)),
                       (1, 1, 10, (1, 0))]  # [1, 2, 7, 6, 0]

        test_list_6 = [(0, 2, 10, (1, 2)), (0, 1, 14, (1, 2)), (2, 2, 10, (1, 2)), (2, 1, 14, (1, 2)),
                       (1, 1, 10, (1, 2))]  # [3, 2, 5, 6, 0]

        test_list_7 = [(1, 0, 10, (2, 0)), (1, 1, 14, (2, 0)), (2, 1, 10, (2, 0))]  # [8, 0, 6]

        test_list_8 = [(1, 1, 10, (2, 1)), (1, 0, 14, (2, 1)), (1, 2, 14, (2, 1)), (2, 0, 10, (2, 1)),
                       (2, 2, 10, (2, 1))]  # [0, 8, 4, 7, 5]

        test_list_9 = [(1, 2, 10, (2, 2)), (1, 1, 14, (2, 2)), (2, 1, 10, (2, 2))]  # [4, 0, 6]

        self.assertEqual(test_list_1, points_1)  # [2, 1, 3, 6, 7, 5, 8, 4]
        self.assertEqual(test_list_2, points_2)  # [8, 0, 2]
        self.assertEqual(test_list_3, points_3)  # [0, 8, 4, 1, 3]
        self.assertEqual(test_list_4, points_4)  # [4, 0, 2]
        self.assertEqual(test_list_5, points_5)  # [1, 2, 7, 6, 0]
        self.assertEqual(test_list_6, points_6)  # [3, 2, 5, 6, 0]
        self.assertEqual(test_list_7, points_7)  # [8, 0, 6]
        self.assertEqual(test_list_8, points_8)  # [0, 8, 4, 7, 5]
        self.assertEqual(test_list_9, points_9)  # [4, 0, 6]


if __name__ == '__main__':
    unittest.main()

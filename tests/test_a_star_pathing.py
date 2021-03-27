import unittest
import os
import sys
sys.path.append('../Pic-to-Stitch/')

import a_star_pathing as asp


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, False)

    def test__init__(self):
        pass

    def test_set_co_or(self, val):
        pass

    def test_set_h(self, val):
        pass

    def test_set_g(self, val):
        pass

    def test_set_f(self, val):
        pass

    def test_set_l_point(self, val):
        pass

    def test_get_f(self):
        pass

    def test_get_h(self):
        pass

    def test_get_g(self):
        pass

    def test_get_l_point(self):
        pass

    def test_get_co_or(self):
        pass

    def test_printe(self):
        pass

    def test_point_set_print(self):
        pass

    def test_move_to_a_star(self, main, main_plot, goto_yx, start_yx, passed_ind_list):
        pass

    def test_set_node(self, node, plot, start_yx, goto_yx, g, l_p):
        pass

    def test_lowest_f(self, open_list):
        pass

    def get_surrounding_nodes(self, plot, y, x):
        pass

    def test_print_node_plot(self, node_plot):
        pass

    def test_print_node_list(self, node_list):
        pass


if __name__ == '__main__':
    unittest.main()

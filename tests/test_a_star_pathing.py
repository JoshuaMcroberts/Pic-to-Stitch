import unittest
import os
import sys
sys.path.append('../Pic-to-Stitch/')


from pic_to_stitch import a_star_pathing as asp
from pic_to_stitch import plot_objects as po

class TestAStarPathing(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        self.node = asp.Node()
        self.node.h = 10
        self.node.g = 23
        self.node.f = 33
        self.node.l_point = (1, 2)
        self.node.co_or = (2, 3)

    def tearDown(self):
        pass

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

    # def test_printe(self):
    #     pass
    #
    # def test_point_set_print(self):
    #     pass
    #
    # def test_move_to_a_star(self):
    #     pass
    #
    # def test_set_node(self):
    #     pass
    #
    # def test_lowest_f(self):
    #     pass
    #
    # def get_surrounding_nodes(self):
    #     pass
    #
    # def test_print_node_plot(self):
    #     pass
    #
    # def test_print_node_list(self):
    #     pass


if __name__ == '__main__':
    unittest.main()

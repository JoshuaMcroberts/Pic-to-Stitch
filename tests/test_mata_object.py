import unittest
import numpy as np
import sys
sys.path.append('../pic_to_stitch/')

from pic_to_stitch import mata_object as mo


class TestMataObject(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        pass

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        self.mata = mo.MataObject()
        self.mata.colour_change = [75]
        self.mata.offset = 116 + 8 * 1
        self.mata.flags = 10
        self.mata.date = "20210327"
        self.mata.time = "10261000"
        self.mata.thread_count = 1
        self.mata.stitch_count = 6
        self.mata.hoop_code = 0
        self.mata.extent_1 = [6, 6, 6, 6]
        self.mata.extent_2 = [-1, -1, -1, -1]
        self.mata.extent_3 = [-1, -1, -1, -1]
        self.mata.extent_4 = [-1, -1, -1, -1]
        self.mata.extent_5 = [-1, -1, -1, -1]
        self.mata.emb_stitch_lists = [[(0, 0), (30, 0), (0, -30), (-27, 0)]]
        self.mata.stitch_lists = [[(0, 0), (30, 0), (0, -30), (-27, 0)], [(56, 12), (12, 37), (76, 87)]]
        self.mata.emb_jump_to_lists = [[(0, 0), (-18, 18)]]
        self.mata.jump_to_lists = [[(0, 0), (30, 0), (0, -30), (-27, 0)]]
        self.mata.stitch_objects = ["f", "b", "e", "d"]
        self.mata.matrix = [[0, 0, 0, 0, 4, 4, 4, 4, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 1, 0, 0, 0, 5, 0, 0],
                            [0, 0, 0, 1, 0, 0, 5, 0, 0, 0],
                            [0, 0, 0, 0, 0, 5, 0, 0, 0, 0],
                            [3, 0, 0, 0, 5, 0, 0, 0, 0, 0],
                            [3, 0, 0, 5, 0, 2, 0, 0, 0, 0],
                            [3, 0, 0, 0, 0, 0, 2, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def tearDown(self):
        pass

    def test_set_stitch_objects(self):

        stitch_objects = ["a", "b", "c", "d"]
        self.mata.set_stitch_objects(stitch_objects)
        self.assertEqual(self.mata.stitch_objects, ["a", "b", "c", "d"])

    def test_set_colour_change(self):
        colour_change_list = [12, 34, 56, 67, 78, 90]
        self.mata.set_colour_change(colour_change_list)
        self.assertEqual(self.mata.colour_change, [12, 34, 56, 67, 78, 90])

    def test_set_offset(self):
        self.mata.set_offset(234)
        self.assertEqual(self.mata.offset, 234)

    def test_set_flags(self):
        self.mata.set_flags(20)
        self.assertEqual(self.mata.flags, 20)

    def test_set_date(self):
        self.mata.set_date("20210202")
        self.assertEqual(self.mata.date, "20210202")

    def test_set_time(self):
        self.mata.set_time("14321700")
        self.assertEqual(self.mata.time, "14321700")

    def test_set_thread_count(self):
        self.mata.set_thread_count(253)
        self.assertEqual(self.mata.thread_count, 253)

    def test_set_stitch_count(self):
        self.mata.set_stitch_count(47632)
        self.assertEqual(self.mata.stitch_count, 47632)

    def test_set_hoop_code(self):
        self.mata.set_hoop_code(4)
        self.assertEqual(self.mata.hoop_code, 4)
        self.mata.set_hoop_code(3)
        self.assertEqual(self.mata.hoop_code, 3)
        self.mata.set_hoop_code(2)
        self.assertEqual(self.mata.hoop_code, 2)
        self.mata.set_hoop_code(1)
        self.assertEqual(self.mata.hoop_code, 1)
        self.mata.set_hoop_code(0)
        self.assertEqual(self.mata.hoop_code, 0)

    def test_set_extent_1(self):
        self.mata.set_extent_1([8, 2, 8, 2])
        self.assertEqual(self.mata.extent_1, [8, 2, 8, 2])
        self.mata.set_extent_1([100, 10, 100, 10])
        self.assertEqual(self.mata.extent_1, [100, 10, 100, 10])

    def test_set_extent_2(self):
        self.mata.set_extent_2([-1, -1, -1, -1])
        self.assertEqual(self.mata.extent_2, [-1, -1, -1, -1])

    def test_set_extent_3(self):
        self.mata.set_extent_3([-1, -1, -1, -1])
        self.assertEqual(self.mata.extent_3, [-1, -1, -1, -1])

    def test_set_extent_4(self):
        self.mata.set_extent_4([-1, -1, -1, -1])
        self.assertEqual(self.mata.extent_4, [-1, -1, -1, -1])

    def test_set_extent_5(self):
        self.mata.set_extent_5([-1, -1, -1, -1])
        self.assertEqual(self.mata.extent_5, [-1, -1, -1, -1])

    def test_set_stitch_list(self):
        lists = [[(8, 2,), (8, 2)], [(8, 2,), (8, 2)]]
        self.mata.set_stitch_lists(lists)
        self.assertEqual(self.mata.stitch_lists, [[(8, 2,), (8, 2)], [(8, 2,), (8, 2)]])

    def test_set_emb_stitch_list(self):
        lists = [[(8, 2,), (8, 2)], [(8, 2,), (8, 2)]]
        self.mata.set_emb_stitch_lists(lists)
        self.assertEqual(self.mata.emb_stitch_lists, [[(8, 2,), (8, 2)], [(8, 2,), (8, 2)]])

    def test_set_jump_to_list(self):
        lists = [[(8, 2,), (8, 2)], [(8, 2,), (8, 2)]]
        self.mata.set_jump_to_lists(lists)
        self.assertEqual(self.mata.jump_to_lists, [[(8, 2,), (8, 2)], [(8, 2,), (8, 2)]])

    def test_set_emb_jump_to_list(self):
        lists = [[(8, 2,), (8, 2)], [(8, 2,), (8, 2)]]
        self.mata.set_emb_jump_to_lists(lists)
        self.assertEqual(self.mata.emb_jump_to_lists, [[(8, 2,), (8, 2)], [(8, 2,), (8, 2)]])

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
        self.mata.set_matrix(matrix)
        for y, row in enumerate(self.mata.matrix):
            for x, point in enumerate(row):
                self.assertEqual(point, test_matrix[y, x])

    def test_get_stitch_objects(self):
        self.assertEqual(self.mata.get_stitch_objects(), ["f", "b", "e", "d"])

    def test_get_colour_change(self):
        self.assertEqual(self.mata.get_colour_change(), [75])

    def test_get_offset(self):
        self.assertEqual(self.mata.get_offset(), 124)

    def test_get_flags(self):
        self.assertEqual(self.mata.get_flags(), 10)

    def test_get_date(self):
        self.assertEqual(self.mata.get_date(), "20210327")

    def test_get_time(self):
        self.assertEqual(self.mata.get_time(), "10261000")

    def test_get_thread_count(self):
        self.assertEqual(self.mata.get_thread_count(), 1)

    def test_get_stitch_count(self):
        self.assertEqual(self.mata.get_stitch_count(), 6)

    def test_get_hoop_code(self):
        self.assertEqual(self.mata.get_hoop_code(), 0)

    def test_get_extent_1(self):
        self.assertEqual(self.mata.get_extent_1(), [6, 6, 6, 6])

    def test_get_extent_2(self):
        self.assertEqual(self.mata.get_extent_2(), [-1, -1, -1, -1])

    def test_get_extent_3(self):
        self.assertEqual(self.mata.get_extent_3(), [-1, -1, -1, -1])

    def test_get_extent_4(self):
        self.assertEqual(self.mata.get_extent_4(), [-1, -1, -1, -1])

    def test_get_extent_5(self):
        self.assertEqual(self.mata.get_extent_5(), [-1, -1, -1, -1])

    def test_get_stitch_lists(self):
        self.assertEqual(self.mata.get_stitch_lists(), [[(0, 0), (30, 0), (0, -30), (-27, 0)], [(56, 12), (12, 37), (76, 87)]])

    def test_get_emb_stitch_list(self):
        self.assertEqual(self.mata.get_emb_stitch_lists(), [[(0, 0), (30, 0), (0, -30), (-27, 0)]])

    def test_get_jump_to_list(self):
        self.assertEqual(self.mata.get_jump_to_lists(), [[(0, 0), (30, 0), (0, -30), (-27, 0)]])

    def test_get_emb_jump_to_list(self):
        self.assertEqual(self.mata.get_emb_jump_to_lists(), [[(0, 0), (-18, 18)]])

    def test_get_matrix(self):
        test_matrix = np.array([[0, 0, 0, 0, 4, 4, 4, 4, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 1, 0, 0, 0, 5, 0, 0],
                               [0, 0, 0, 1, 0, 0, 5, 0, 0, 0],
                               [0, 0, 0, 0, 0, 5, 0, 0, 0, 0],
                               [3, 0, 0, 0, 5, 0, 0, 0, 0, 0],
                               [3, 0, 0, 5, 0, 2, 0, 0, 0, 0],
                               [3, 0, 0, 0, 0, 0, 2, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        matrix = self.mata.get_matrix()
        for y, row in enumerate(matrix):
            for x, point in enumerate(row):
                self.assertEqual(point, test_matrix[y, x])

    def test_create_offset(self):
        test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        offset = mo.create_offset(test_list)
        self.assertEqual(offset, 212)

    def test_create_thread_count(self):
        test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        thread_count = mo.create_thread_count(test_list)
        self.assertEqual(thread_count, 12)

    def test_create_jump_to_list(self):
        row = [0] * 10
        matrix = np.array([row] * 10)

        stitch_lists = [[(2, 3), (3, 3)],
                        [(6, 5), (7, 6), (8, 7)],
                        [(5, 0), (6, 0), (7, 0)],
                        [(0, 4), (0, 5), (0, 6), (0, 7)],
                        [(2, 7), (3, 6), (4, 5), (5, 4), (6, 3)]]

        test_jumps = [[(5, 5), (4, 4), (3, 3), (2, 3)],
                      [(3, 3), (4, 4), (5, 5), (6, 5)],
                      [(8, 7), (7, 6), (6, 5), (5, 4), (5, 3), (5, 2), (5, 1), (5, 0)],
                      [(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 4), (1, 4), (0, 4)],
                      [(0, 7), (1, 7), (2, 7)]]

        jump_lists = mo.create_jump_to_lists(matrix, stitch_lists)

        self.assertEqual(jump_lists, test_jumps)

    def test_create_emb_lists(self):
        row = [0] * 10
        matrix = np.array([row] * 10)
        stitch_lists = [[(2, 3), (3, 3)],
                        [(6, 5), (7, 6), (8, 7)],
                        [(5, 0), (6, 0), (7, 0)],
                        [(0, 4), (0, 5), (0, 6), (0, 7)],
                        [(2, 7), (3, 6), (4, 5), (5, 4), (6, 3)]]
        test_lists = [[(0, 0), (0, -1)],
                      [(0, 0), (1, -1), (1, -1)],
                      [(0, 0), (0, -1), (0, -1)],
                      [(0, 0), (1, 0), (1, 0), (1, 0)],
                      [(0, 0), (-1, -1), (-1, -1), (-1, -1), (-1, -1)]]

        emb_lists = mo.create_emb_lists(stitch_lists, matrix)

        self.assertEqual(test_lists, emb_lists)


if __name__ == '__main__':
    unittest.main()


import unittest
import numpy as np
import sys
sys.path.append('../pic_to_stitch/')

from pic_to_stitch import mata_object as mo
from pic_to_stitch import stitch_objects as so


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

    def test__init__(self):
        ob = mo.MataObject()
        self.assertTrue(ob.date)
        self.assertTrue(ob.time)
        self.assertEqual(20, ob.flags)
        self.assertEqual([-1, -1, -1, -1], ob.extent_2)
        self.assertEqual([-1, -1, -1, -1], ob.extent_3)
        self.assertEqual([-1, -1, -1, -1], ob.extent_4)
        self.assertEqual([-1, -1, -1, -1], ob.extent_5)

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

    def test_create_matrix(self):
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

        stitch_ob = so.StitchObject()
        stitch_ob.set_matrix(matrix)
        ob_list = [stitch_ob]

        matrix = mo.create_matrix(ob_list)
        for y, row in enumerate(matrix):
            for x, point in enumerate(row):
                self.assertEqual(test_matrix[y, x], point)

    def test_create_stitch_count(self):
        emb_jump = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 0]]
        emb_stitch = [[0, 9, 8, 7, 6], [5, 4, 3, 2, 1]]

        stitch_count = mo.create_stitch_count(emb_jump, emb_stitch)

        self.assertEqual(20, stitch_count)

    def test_create_colour_change_list(self):
        ob_list = []
        test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(10):
            stitch_ob = so.StitchObject()
            stitch_ob.set_colour(i)
            ob_list.append(stitch_ob)
        colour_list = mo.create_colour_change_list(ob_list)
        self.assertEqual(test_list, colour_list)

    def test_stitch_lists(self):
        ob_list = []
        test_list = [[(0, 0), (0, 1), (1, 2), (2, 2)],
                     [(0, 0), (0, 1), (1, 2), (2, 2)],
                     [(0, 0), (0, 1), (1, 2), (2, 2)],
                     [(0, 0), (0, 1), (1, 2), (2, 2)],
                     [(0, 0), (0, 1), (1, 2), (2, 2)]]
        for i in range(5):
            stitch_ob = so.StitchObject()
            stitch_ob.set_stitch_list([(0, 0), (0, 1), (1, 2), (2, 2)])
            ob_list.append(stitch_ob)
        stitch_lists = mo.create_stitch_lists(ob_list)
        self.assertEqual(test_list, stitch_lists)

    def test_create_mata_object(self):
        ob_list = []
        test_stitch_lists = [[(9, 0), (9, 1), (8, 2), (7, 2)],
                             [(9, 0), (9, 1), (8, 2), (7, 2)],
                             [(9, 0), (9, 1), (8, 2), (7, 2)],
                             [(9, 0), (9, 1), (8, 2), (7, 2)],
                             [(9, 0), (9, 1), (8, 2), (7, 2)]]

        test_emb_stitches = [[(0, 0), (3, 0), (3, -3), (0, -3)],
                             [(0, 0), (3, 0), (3, -3), (0, -3)],
                             [(0, 0), (3, 0), (3, -3), (0, -3)],
                             [(0, 0), (3, 0), (3, -3), (0, -3)],
                             [(0, 0), (3, 0), (3, -3), (0, -3)]]

        test_jump_lists = [[(4, 5), (5, 4), (6, 3), (7, 2), (8, 1), (9, 0)],
                           [(7, 2), (8, 1), (9, 0)],
                           [(7, 2), (8, 1), (9, 0)],
                           [(7, 2), (8, 1), (9, 0)],
                           [(7, 2), (8, 1), (9, 0)]]

        test_emb_jumps = [[(0, 0), (-15, 15)],
                          [(0, 0), (-6, 6)],
                          [(0, 0), (-6, 6)],
                          [(0, 0), (-6, 6)],
                          [(0, 0), (-6, 6)]]

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

        for i in range(5):
            row = [0] * 10
            matrix = np.array([row] * 10)

            stitch_ob = so.StitchObject()
            stitch_ob.set_stitch_list([(0, 0), (0, 1), (1, 2), (2, 2)])
            stitch_ob.set_stitch_len(30)
            stitch_ob.set_matrix(matrix)
            stitch_ob.set_colour(i+1)

            ob_list.append(stitch_ob)

        mo.create_mata_object(ob_list, 2)

        self.assertEqual([1, 2, 3, 4, 5], mo.mata_file.colour_change)
        self.assertEqual(156, mo.mata_file.offset)
        self.assertEqual(20, mo.mata_file.flags)
        self.assertTrue(mo.mata_file.date)
        self.assertTrue(mo.mata_file.time)
        self.assertEqual(5, mo.mata_file.thread_count)
        self.assertEqual(30, mo.mata_file.stitch_count)
        self.assertEqual(2, mo.mata_file.hoop_code)
        self.assertEqual([5, 5, 5, 5], mo.mata_file.extent_1)
        self.assertEqual([-1, -1, -1, -1], mo.mata_file.extent_2)
        self.assertEqual([-1, -1, -1, -1], mo.mata_file.extent_3)
        self.assertEqual([-1, -1, -1, -1], mo.mata_file.extent_4)
        self.assertEqual([-1, -1, -1, -1], mo.mata_file.extent_5)

        for i, stitch_list in enumerate(test_stitch_lists):
            self.assertEqual(stitch_list, mo.mata_file.stitch_lists[i])

        for i, jump_list in enumerate(test_jump_lists):
            self.assertEqual(jump_list, mo.mata_file.jump_to_lists[i])

        for i, stitch_list in enumerate(test_emb_stitches):
            self.assertEqual(stitch_list, mo.mata_file.emb_stitch_lists[i])

        for i, jump_list in enumerate(test_emb_jumps):
            self.assertEqual(jump_list, mo.mata_file.emb_jump_to_lists[i])

        for y, row in enumerate(test_matrix):
            for x, point in enumerate(row):
                self.assertEqual(point, mo.mata_file.matrix[y, x])

    def test_create_extent(self):

        test_matrix_1 = [[1, 2, 3, 4],
                         [2, 4, 5, 6],
                         [3, 5, 6, 7],
                         [4, 6, 7, 8],
                         [5, 7, 8, 9],
                         [6, 8, 9, 10]]

        test_matrix_2 = [[1, 2, 3, 4, 5, 6, 7],
                         [2, 4, 5, 6, 7, 8, 9],
                         [3, 5, 6, 7, 8, 9, 10],
                         [4, 6, 7, 8, 9, 10, 11]]

        test_matrix_3 = [[1, 2, 3, 4, 5],
                         [2, 4, 5, 6, 7],
                         [3, 5, 6, 7, 8],
                         [4, 6, 7, 8, 9],
                         [5, 7, 8, 9, 10]]

        test_matrix_4 = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                         [2, 4, 5, 6, 7, 8, 9, 10, 11],
                         [3, 5, 6, 7, 8, 9, 10, 11, 12],
                         [4, 6, 7, 8, 9, 10, 11, 12, 13]]

        extent_t1 = mo.create_extent(test_matrix_1)
        extent_t2 = mo.create_extent(test_matrix_2)
        extent_t3 = mo.create_extent(test_matrix_3)
        extent_t4 = mo.create_extent(test_matrix_4)

        self.assertEqual([2, 3, 2, 3], extent_t1)
        self.assertEqual([4, 2, 4, 2], extent_t2)
        self.assertEqual([2, 2, 2, 2], extent_t3)
        self.assertEqual([4, 2, 4, 2], extent_t4)

    def test_combine_stitches(self):

        test_list = [(0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1),
                       (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1),
                       (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1),
                       (0, 1), (0, 1), (0, 1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1),
                       (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1),
                       (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1),
                       (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1),
                       (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1),
                       (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1),
                       (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1),
                       (0, -1), (0, -1), (0, -1), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 1), (-1, 1), (-1, 1),
                       (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1),
                       (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1),
                       (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1),
                       (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1),
                       (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1),
                       (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1),
                       (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1),
                       (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1),
                       (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1)]

        result_1 = [(0, 39), (0, 39), (0, 21), (0, -39), (0, -39), (0, -39), (0, -39), (0, -33), (-39, 0),
                    (-39, 0), (-39, 0), (-39, 0), (-39, 0), (-39, 0), (-39, 0), (-39, 0), (-39, 0), (-39, 0),
                    (-24, 0), (-39, 39), (-39, 39), (-39, 39), (-39, 39), (-39, 39), (-39, 39), (-9, 9)]

        result_2 = [(0, 99), (0, -126), (0, -63), (-126, 0), (-126, 0), (-126, 0), (-36, 0), (-126, 126), (-117, 117)]

        result_3 = [(0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3),
                    (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3),
                    (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3), (0, 3),
                    (0, 3), (0, 3), (0, 3), (0, -3), (0, -3), (0, -3), (0, -3), (0, -3), (0, -3),
                    (0, -3), (0, -3), (0, -3), (0, -3), (0, -3), (0, -3), (0, -3), (0, -3), (0, -3),
                    (0, -3), (0, -3), (0, -3), (0, -3), (0, -3), (0, -3), (0, -3), (0, -3), (0, -3),
                    (0, -3), (0, -3), (0, -3), (0, -3), (0, -3), (0, -3), (0, -3), (0, -3), (0, -3),
                    (0, -3), (0, -3), (0, -3), (0, -3), (0, -3), (0, -3), (0, -3), (0, -3), (0, -3),
                    (0, -3), (0, -3), (0, -3), (0, -3), (0, -3), (0, -3), (0, -3), (0, -3), (0, -3),
                    (0, -3), (0, -3), (0, -3), (0, -3), (0, -3), (0, -3), (0, -3), (0, -3), (0, -3),
                    (0, -3), (0, -3), (0, -3), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0),
                    (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0),
                    (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0),
                    (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0),
                    (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0),
                    (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0),
                    (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0),
                    (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0),
                    (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0),
                    (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0),
                    (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0),
                    (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0),
                    (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0),
                    (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0),
                    (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0),
                    (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 0), (-3, 3), (-3, 3), (-3, 3),
                    (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3),
                    (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3),
                    (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3),
                    (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3),
                    (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3),
                    (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3),
                    (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3),
                    (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3),
                    (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3), (-3, 3)]

        stitch_list_1 = mo.combine_stitches(test_list, 39)
        stitch_list_2 = mo.combine_stitches(test_list, 126)
        stitch_list_3 = mo.combine_stitches(test_list, 3)

        self.assertEqual(result_1, stitch_list_1)
        self.assertEqual(result_2, stitch_list_2)
        self.assertEqual(result_3, stitch_list_3)

    def test_process_stitch_lists(self):
        test_list_1 = [(1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1),
                       (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1),
                       (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1),
                       (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1),
                       (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1),
                       (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1),
                       (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1),
                       (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1),
                       (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1),
                       (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1),
                       (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1),
                       (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1),
                       (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1),
                       (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1),
                       (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1),
                       (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1),
                       (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1),
                       (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1),
                       (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1),
                       (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1), (1, -1),
                       (1, -1), (1, -1), (1, -1), (1, -1), (1, -1)]

        test_list_2 = [(0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1),
                       (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1),
                       (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1),
                       (0, 1), (0, 1), (0, 1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1),
                       (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1),
                       (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1),
                       (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1),
                       (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1),
                       (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1),
                       (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1), (0, -1),
                       (0, -1), (0, -1), (0, -1), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0),
                       (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 0), (-1, 1), (-1, 1), (-1, 1),
                       (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1),
                       (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1),
                       (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1),
                       (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1),
                       (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1),
                       (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1),
                       (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1),
                       (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1),
                       (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1), (-1, 1)]

        test_list_3 = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
                       (0, 0), (0, 0), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
                       (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
                       (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
                       (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (-1, -1), (-1, -1), (-1, -1),
                       (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1),
                       (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1),
                       (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1),
                       (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1),
                       (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1),
                       (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1),
                       (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1),
                       (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1),
                       (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1),
                       (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1),
                       (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1),
                       (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1),
                       (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1),
                       (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1),
                       (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1), (-1, -1),
                       (-1, -1), (-1, -1), (-1, -1), (-1, -1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
                       (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
                       (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
                       (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
                       (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]

        test_lists = [test_list_1, test_list_2, test_list_3]

        result_1 = [(9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9),
                    (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9),
                    (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9),
                    (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9),
                    (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9),
                    (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9),
                    (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (9, -9), (6, -6)]

        result_2 = [(0, 39), (0, 39), (0, 21), (0, -39), (0, -39), (0, -39), (0, -39), (0, -33), (-39, 0),
                    (-39, 0), (-39, 0), (-39, 0), (-39, 0), (-39, 0), (-39, 0), (-39, 0), (-39, 0), (-39, 0),
                    (-24, 0), (-39, 39), (-39, 39), (-39, 39), (-39, 39), (-39, 39), (-39, 39), (-9, 9)]

        result_3 = [(0, 0), (51, 51), (51, 51), (-51, -51), (-51, -51), (-51, -51), (-51, -51),
                    (-51, -51), (-51, -51), (-51, -51), (-24, -24), (51, 51), (51, 51), (24, 24)]

        result_list_1 = [result_1, result_2, result_3]

        result_4 = [(126, -126), (126, -126), (126, -126), (126, -126), (51, -51)]

        result_5 = [(0, 99), (0, -126), (0, -63), (-126, 0), (-126, 0), (-126, 0), (-36, 0), (-126, 126), (-117, 117)]

        result_6 = [(0, 0), (102, 102), (-126, -126), (-126, -126), (-126, -126), (-3, -3), (126, 126)]

        result_list_2 = [result_4, result_5, result_6]

        stitch_obs = []
        for i in range(3):
            stitch_ob = so.StitchObject()
            stitch_obs.append(stitch_ob)

        stitch_obs[0].set_stitch_len(9)
        stitch_obs[1].set_stitch_len(39)
        stitch_obs[2].set_stitch_len(51)


        # set_list = [(8, 185)]
        # for j in set_list:
        #     option, count = j
        #
        #     if option == 1:
        #         for i in range(count):
        #             stitch = (0, 0)
        #             test_list_1.append(stitch)
        #
        #     elif option == 2:
        #         for i in range(count):
        #             stitch = (0, 1)
        #             test_list_1.append(stitch)
        #
        #     elif option == 3:
        #         for i in range(count):
        #             stitch = (1, 0)
        #             test_list_1.append(stitch)
        #
        #     elif option == 4:
        #         for i in range(count):
        #             stitch = (1, 1)
        #             test_list_1.append(stitch)
        #
        #     if option == 5:
        #         for i in range(count):
        #             stitch = (0, -1)
        #             test_list_1.append(stitch)
        #
        #     elif option == 6:
        #         for i in range(count):
        #             stitch = (-1, 0)
        #             test_list_1.append(stitch)
        #
        #     elif option == 7:
        #         for i in range(count):
        #             stitch = (-1, -1)
        #             test_list_1.append(stitch)
        #
        #     elif option == 8:
        #         for i in range(count):
        #             stitch = (1, -1)
        #             test_list_1.append(stitch)
        #
        #     elif option == 9:
        #         for i in range(count):
        #             stitch = (-1, 1)
        #             test_list_1.append(stitch)
        # print(test_list_1)

        out_lists_1 = mo.process_stitch_lists(test_lists, stitch_obs, 1)
        out_lists_2 = mo.process_stitch_lists(test_lists, stitch_obs, 0)

        for ind, s_list in enumerate(out_lists_1):
            self.assertEqual(result_list_1[ind], s_list)

        for ind, s_list in enumerate(out_lists_2):
            self.assertEqual(result_list_2[ind], s_list)


if __name__ == '__main__':
    unittest.main()


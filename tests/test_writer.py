import unittest
import os
import sys
sys.path.append('../Pic-to-Stitch/')

import writer as w


class MataObject:
    def __init__(self):
        self.colour_change = [75]
        self.offset = 116 + 8 * 1  # set
        self.flags = 20  # set
        self.date = str("20210327")  # set
        self.time = str("10261000")  # set
        self.thread_count = 1  # set
        self.stitch_count = 6  # set by method
        self.hoop_code = 0  # set
        self.extent1 = [6, 6, 6, 6]  # set
        self.extent2 = [-1, -1, -1, -1]  # set
        self.extent3 = [-1, -1, -1, -1]  # set
        self.extent4 = [-1, -1, -1, -1]  # set
        self.extent5 = [-1, -1, -1, -1]  # set
        self.emb_stitch_lists = [[(0, 0), (30, 0), (0, -30), (-27, 0)]]  # set by method
        self.emb_jump_to_lists = [[(0, 0), (-18, 18)]]  # set by method


class TestWriter(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.mata = MataObject()

        self.mata_bytes = b'\x7c\x00\x00\x00\x14\x00\x00\x00\x32\x30\x32\x31\x30\x33\x32\x37\x31\x30\x32\x36\x31\x30' \
                          b'\x30\x30\x01\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x06\x00\x00\x00' \
                          b'\x06\x00\x00\x00\x06\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff' \
                          b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff' \
                          b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x06\x00\x00\x00\x06\x00\x00\x00\x06\x00' \
                          b'\x00\x00\x06\x00\x00\x00\x4b\x00\x00\x00\x0d\x00\x00\x00\x80\x02\x00\x00\x80\x02\xee\x12' \
                          b'\x00\x00\x1e\x00\x00\xe2\xe5\x00\x80\x10'

    @classmethod
    def tearDownClass(self):
        file_path = "write_test_ob.jef"
        os.remove(file_path)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_co_or_byte(self):
        self.assertEqual(w.co_or_byte((0, 0)), (b'\x00', b'\x00'))
        self.assertEqual(w.co_or_byte((127, 127)), (b'\x7F', b'\x7F'))
        self.assertEqual(w.co_or_byte((-128, -128)), (b'\x80', b'\x80'))
        self.assertEqual(w.co_or_byte((-1, -1)), (b'\xFF', b'\xFF'))

    def test_four_byte_int(self):
        self.assertEqual(w.four_byte_int(0), b'\x00\x00\x00\x00')
        self.assertEqual(w.four_byte_int(2147483647), b'\xFF\xFF\xFF\x7F')
        self.assertEqual(w.four_byte_int(-2147483648), b'\x00\x00\x00\x80')
        self.assertEqual(w.four_byte_int(-1), b'\xFF\xFF\xFF\xFF')

    def test_write_to_file(self):
        file_path = "write_test_ob.jef"
        w.write_to_file(self.mata, file_path)
        file = open(file_path, "rb")
        file_bytes = file.read()
        self.assertEqual(self.mata_bytes, file_bytes)
        file.close()

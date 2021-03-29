import unittest
import os

import sys
sys.path.append('../pic_to_stitch/')
from pic_to_stitch import writer as w
from pic_to_stitch import mata_object as mo


class TestWriter(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.mata = mo.MataObject()
        self.mata.set_colour_change([75])
        self.mata.set_offset(116 + 8 * 1)
        self.mata.set_flags(20)
        self.mata.set_date(str("20210327"))
        self.mata.set_time(str("10261000"))
        self.mata.set_thread_count(1)
        self.mata.set_stitch_count(6)
        self.mata.set_hoop_code(0)
        self.mata.set_extent_1([6, 6, 6, 6])
        self.mata.set_extent_2([-1, -1, -1, -1])
        self.mata.set_extent_3([-1, -1, -1, -1])
        self.mata.set_extent_4([-1, -1, -1, -1])
        self.mata.set_extent_5([-1, -1, -1, -1])
        self.mata.set_emb_stitch_lists([[(0, 0), (30, 0), (0, -30), (-27, 0)]])
        self.mata.set_emb_jump_to_lists([[(0, 0), (-18, 18)]])

        self.mata_bytes = b'\x7c\x00\x00\x00\x14\x00\x00\x00\x32\x30\x32\x31\x30\x33\x32\x37\x31\x30\x32\x36\x31\x30' \
                          b'\x30\x30\x01\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x06\x00\x00\x00' \
                          b'\x06\x00\x00\x00\x06\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff' \
                          b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff' \
                          b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff' \
                          b'\xff\xff\xff\xff\xff\xff\x4b\x00\x00\x00\x0d\x00\x00\x00\x80\x02\x00\x00\x80\x02\xee\x12' \
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

if __name__ == '__main__':
    unittest.main()
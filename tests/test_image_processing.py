import unittest
from unittest.mock import Mock
import numpy as np
from PIL import Image
import sys
sys.path.append('../pic_to_stitch/')

from pic_to_stitch import image_processing as im


class TestImageProcessing(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        file_path = "Guppy_test.png"
        self.img_1 = Image.open(file_path)
        file_path = "PixelArtGuppy_test.png"
        self.img_2 = Image.open(file_path)
        file_path = "PixelArtSmall_test.png"
        self.img_3 = Image.open(file_path)
        file_path = "Gradient_test.jpg"
        self.img_4 = Image.open(file_path)
        self.img_list = [self.img_1, self.img_2, self.img_3, self.img_4]

    @classmethod
    def tearDownClass(self):
        self.img_1.close()
        self.img_2.close()
        self.img_3.close()
        self.img_4.close()

    def setUp(self):
        self.mock_main = Mock()

    def tearDown(self):
        pass

    def test_image_resize(self):

        img_4 = self.img_4.copy()
        new_w, new_h = img_4.size
        img_4_r = self.img_4.copy()
        img_4_r = img_4_r.rotate(90, expand=True)

        out_img_1 = im.image_resize(self.mock_main, img_4, 1, 1, new_w, new_h)
        self.assertEqual(0, self.mock_main.hoop_code)
        out_img_2 = im.image_resize(self.mock_main, img_4, 2, 1, new_w, new_h)
        self.assertEqual(1, self.mock_main.hoop_code)
        out_img_3 = im.image_resize(self.mock_main, img_4, 3, 1, new_w, new_h)
        self.assertEqual(2, self.mock_main.hoop_code)
        out_img_4 = im.image_resize(self.mock_main, img_4, 4, 1, new_w, new_h)
        self.assertEqual(3, self.mock_main.hoop_code)
        out_img_5 = im.image_resize(self.mock_main, img_4, 5, 1, new_w, new_h)
        self.assertEqual(4, self.mock_main.hoop_code)

        new_w, new_h = img_4_r.size
        out_img_6 = im.image_resize(self.mock_main, img_4_r, 1, 1, new_w, new_h)
        self.assertEqual(0, self.mock_main.hoop_code)
        out_img_7 = im.image_resize(self.mock_main, img_4_r, 2, 1, new_w, new_h)
        self.assertEqual(1, self.mock_main.hoop_code)
        out_img_8 = im.image_resize(self.mock_main, img_4_r, 3, 1, new_w, new_h)
        self.assertEqual(2, self.mock_main.hoop_code)
        out_img_9 = im.image_resize(self.mock_main, img_4_r, 4, 1, new_w, new_h)
        self.assertEqual(3, self.mock_main.hoop_code)
        out_img_10 = im.image_resize(self.mock_main, img_4_r, 5, 1, new_w, new_h)
        self.assertEqual(4, self.mock_main.hoop_code)

        out_img_11 = im.image_resize(self.mock_main, img_4, 1, 2, 50, 100)
        self.assertEqual(4, self.mock_main.hoop_code)
        out_img_12 = im.image_resize(self.mock_main, img_4, 2, 3, 50, new_h)
        # self.assertEqual(1, self.mock_main.hoop_code)
        out_img_13 = im.image_resize(self.mock_main, img_4, 3, 4, new_w, 50)
        # self.assertEqual(2, self.mock_main.hoop_code)

        self.assertEqual((1100, 550), img_4.size)
        self.assertEqual((550, 1100), img_4_r.size)

        self.assertEqual((188, 94), out_img_1.size)
        self.assertEqual((415, 207), out_img_2.size)
        self.assertEqual((476, 238), out_img_3.size)
        self.assertEqual((529, 264), out_img_4.size)
        self.assertEqual((756, 378), out_img_5.size)

        self.assertEqual((94, 188), out_img_6.size)
        self.assertEqual((207, 415), out_img_7.size)
        self.assertEqual((207, 415), out_img_8.size)
        self.assertEqual((378, 756), out_img_9.size)
        self.assertEqual((378, 756), out_img_10.size)

        self.assertEqual((188, 377), out_img_11.size)
        self.assertEqual((188, 94), out_img_12.size)
        self.assertEqual((376, 188), out_img_13.size)

    def auto_colour_step(main):
        pass

    def test_floor_step(self):

        new_pixel_1 = im.floor_step((103, 254, 45), 1)
        new_pixel_2 = im.floor_step((103, 254, 45), 2)
        new_pixel_3 = im.floor_step((103, 254, 45), 3)
        new_pixel_4 = im.floor_step((103, 254, 45), 4)
        new_pixel_5 = im.floor_step((103, 254, 45), 5)
        new_pixel_6 = im.floor_step((103, 254, 45), 6)
        new_pixel_7 = im.floor_step((103, 254, 45), 7)
        new_pixel_8 = im.floor_step((103, 254, 45), 8)

        self.assertEqual([0, 0, 0], new_pixel_1)
        self.assertEqual([0, 127, 0], new_pixel_2)
        self.assertEqual([85, 170, 0], new_pixel_3)
        self.assertEqual([63, 191, 0], new_pixel_4)
        self.assertEqual([102, 204, 0], new_pixel_5)
        self.assertEqual([85, 212, 42], new_pixel_6)
        self.assertEqual([72, 218, 36], new_pixel_7)
        self.assertEqual([95, 223, 31], new_pixel_8)

    def pix_restrict(main):
        pass

    def test_get_liner_pixel(self):

        b = [0, 0, 0]
        g = [0, 234, 12]
        y = [0, 127, 127]
        d = [6, 6, 6]
        delete_list = [d]
        pix_mat = np.array([[b, b, g, g, g],
                            [b, d, g, g, g],
                            [g, y, g, b, b],
                            [b, b, y, d, b],
                            [d, g, b, b, b]])
        out_pix_1 = im.get_liner_pixel(pix_mat, 1, 1, delete_list)
        out_pix_2 = im.get_liner_pixel(pix_mat, 3, 3, delete_list)
        out_pix_3 = im.get_liner_pixel(pix_mat, 4, 0, delete_list)

        self.assertEqual(g, out_pix_1)
        self.assertEqual(y, out_pix_2)
        self.assertEqual(g, out_pix_3)

    def test_check_delete(self):
        del_list = [[2, 3, 4], [100, 53, 212], [51, 23, 24]]

        bool_1 = im.check_delete(del_list, (100, 100, 100))
        bool_2 = im.check_delete(del_list, (100, 53, 212))

        self.assertFalse(bool_1)
        self.assertTrue(bool_2)

    # def pix_change(main):
    #     pass

    def test_count_colour_list(self):
        pixels = [[2, 3, 4], [51, 23, 24], [2, 3, 4], [100, 53, 212], [51, 23, 24], [100, 53, 212],
                  [100, 53, 212], [2, 3, 4], [51, 23, 24], [51, 23, 24], [100, 53, 212], [2, 3, 4],
                  [100, 53, 212], [51, 23, 24], [2, 3, 4], [2, 3, 4], [2, 3, 4], [100, 53, 212]]

        test_list_1 = [[2, 3, 4], [51, 23, 24], [100, 53, 212]]
        test_list_2 = [7, 5, 6]
        test_list_3 = [9, 98, 365]

        lists = im.count_colour_list(pixels)

        self.assertEqual(pixels, lists[0])
        self.assertEqual(test_list_1, lists[1])
        self.assertEqual(test_list_2, lists[2])
        self.assertEqual(test_list_3, lists[3])

    def test_get_surrounding_pixels_3x3(self):

        plot = np.array([[[1, 1, 1], [2, 2, 2], [3, 3, 3]],
                         [[8, 8, 8], [0, 0, 0], [4, 4, 4]],
                         [[7, 7, 7], [6, 6, 6], [5, 5, 5]]])

        test_pixs_1 = [(2, 2, 2), (1, 1, 1), (3, 3, 3), (6, 6, 6), (7, 7, 7), (5, 5, 5), (8, 8, 8), (4, 4, 4)]
        test_pixs_2 = [(8, 8, 8), (0, 0, 0), (2, 2, 2)]
        test_pixs_3 = [(0, 0, 0), (8, 8, 8), (4, 4, 4), (1, 1, 1), (3, 3, 3)]
        test_pixs_4 = [(4, 4, 4), (0, 0, 0), (2, 2, 2)]
        test_pixs_5 = [(1, 1, 1), (2, 2, 2), (7, 7, 7), (6, 6, 6), (0, 0, 0)]
        test_pixs_6 = [(3, 3, 3), (2, 2, 2), (5, 5, 5), (6, 6, 6), (0, 0, 0)]
        test_pixs_7 = [(8, 8, 8), (0, 0, 0), (6, 6, 6)]
        test_pixs_8 = [(0, 0, 0), (8, 8, 8), (4, 4, 4), (7, 7, 7), (5, 5, 5)]
        test_pixs_9 = [(4, 4, 4), (0, 0, 0), (6, 6, 6)]

        test_co_or_1 = [(0, 1), (0, 0), (0, 2), (2, 1), (2, 0), (2, 2), (1, 0), (1, 2)]
        test_co_or_2 = [(1, 0), (1, 1), (0, 1)]
        test_co_or_3 = [(1, 1), (1, 0), (1, 2), (0, 0), (0, 2)]
        test_co_or_4 = [(1, 2), (1, 1), (0, 1)]
        test_co_or_5 = [(0, 0), (0, 1), (2, 0), (2, 1), (1, 1)]
        test_co_or_6 = [(0, 2), (0, 1), (2, 2), (2, 1), (1, 1)]
        test_co_or_7 = [(1, 0), (1, 1), (2, 1)]
        test_co_or_8 = [(1, 1), (1, 0), (1, 2), (2, 0), (2, 2)]
        test_co_or_9 = [(1, 2), (1, 1), (2, 1)]


        points_1 = im.get_surrounding_pixels_3x3(plot, 1, 1)
        points_2 = im.get_surrounding_pixels_3x3(plot, 0, 0)
        points_3 = im.get_surrounding_pixels_3x3(plot, 0, 1)
        points_4 = im.get_surrounding_pixels_3x3(plot, 0, 2)
        points_5 = im.get_surrounding_pixels_3x3(plot, 1, 0)
        points_6 = im.get_surrounding_pixels_3x3(plot, 1, 2)
        points_7 = im.get_surrounding_pixels_3x3(plot, 2, 0)
        points_8 = im.get_surrounding_pixels_3x3(plot, 2, 1)
        points_9 = im.get_surrounding_pixels_3x3(plot, 2, 2)

        self.assertEqual((test_pixs_1, test_co_or_1), points_1)
        self.assertEqual((test_pixs_2, test_co_or_2), points_2)
        self.assertEqual((test_pixs_3, test_co_or_3), points_3)
        self.assertEqual((test_pixs_4, test_co_or_4), points_4)
        self.assertEqual((test_pixs_5, test_co_or_5), points_5)
        self.assertEqual((test_pixs_6, test_co_or_6), points_6)
        self.assertEqual((test_pixs_7, test_co_or_7), points_7)
        self.assertEqual((test_pixs_8, test_co_or_8), points_8)
        self.assertEqual((test_pixs_9, test_co_or_9), points_9)

    def get_surrounding_pixels_5x5(pixel_matrix, y, x):
        pass

    def get_surrounding_pixels_7x7(pixel_matrix, y, x):
        pass

    def get_surrounding_pixels_9x9(pixel_matrix, y, x):
        pass

    # def get_man_merge_vals(main, change_list, pixel_list):
    #     pass

    def set_new_pixel_colour(image, new_pixel_list, pixel_change):
        pass

    # def janome_colours(main):
    #     pass

    def test_get_colour_diff(self):
        test_list = [211, 178, 145]

        pixels = [[2, 3, 4], [51, 23, 24], [100, 53, 212]]
        dif_list = im.get_colour_diff(pixels, (23, 47, 150))

        self.assertEqual(test_list, dif_list)

    def count_colour(pixel_matrix, pixel_list, colour_count, combine_count):
        pass

    def sort_algorithm(pixel_list, combine_value, colour_count):
        pass

    # def create_image_plot(main):
    #     pass

    def create_section_image(ref_plot, image):
        pass


if __name__ == '__main__':
    unittest.main()

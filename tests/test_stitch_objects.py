import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test__init__(self, passed_colour, stitch_list, max_stitch_len, matrix):
        pass

    def test_get_stitch_list(self):
        pass

    def test_set_colour(self):
        pass

    def test_get_colour(self):
        pass

    def test_process_stitch_list(self):
        pass

    def test_create_stitch_objects(self, objects):
        pass


if __name__ == '__main__':
    unittest.main()


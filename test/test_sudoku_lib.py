import unittest


class MyTestCase(unittest.TestCase):

    def test_row_valid(self):
        self.assertEqual(True, False)

    def test_row_invalid(self):
        self.assertEqual(True, False)

    def test_column_valid(self):
        self.assertEqual(True, False)

    def test_column_invalid(self):
        self.assertEqual(True, False)

    def test_cell_valid(self):
        self.assertEqual(True, False)

    def test_cell_invalid(self):
        self.assertEqual(True, False)

    def test_solved_puzzle(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

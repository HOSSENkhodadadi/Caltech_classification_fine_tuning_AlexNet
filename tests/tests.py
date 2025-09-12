import unittest
class TestCaseExample(unittest.TestCase):
    def first_test(self):
        self.assertEqual(1 + 1, 2)
if __name__ == '__main__':
    unittest.main()
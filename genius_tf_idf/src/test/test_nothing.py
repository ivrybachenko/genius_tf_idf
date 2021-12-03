import unittest


class NothingTestCase(unittest.TestCase):
    def test_that_testing_works(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()

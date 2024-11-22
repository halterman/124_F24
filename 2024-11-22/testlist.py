import unittest
from liststuff import reverse, sort

class ListTester(unittest.TestCase):
    def test_sort_1(self) -> None:
        a = [2, 67, -3, 18, 95]
        sort(a)
        # self.assertEqual(EXPECTED, ACTUAL)
        self.assertEqual([-3, 2, 18, 67, 95], a)

    def test_sort_2(self) -> None:
        a = [2, 67, -3, 18, 25]
        sort(a)
        self.assertEqual([-3, 2, 18, 25, 67], a)
    
    def test_reverse_1(self) -> None:
        a = [2, 67, -3, 18, 25]
        reverse(a)
        self.assertEqual([25, 18, -3, 67, 2], a)

    def test_reverse_2(self) -> None:
        a = [2]
        reverse(a)
        self.assertEqual([2], a)

    def test_reverse_3(self) -> None:
        a = []
        reverse(a)
        self.assertEqual([], a)



if __name__ == '__main__':
    unittest.main()
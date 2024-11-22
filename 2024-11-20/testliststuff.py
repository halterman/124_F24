import unittest
import liststuff

class ListStuffTest(unittest.TestCase):
    def test_reverse_odd_length(self) -> None:
        nums = [10, 20, 30, 40, 50]
        self.assertEqual([10, 20, 30, 40, 50], nums)
        liststuff.reverse(nums)
        self.assertEqual([50, 40, 30, 20, 10], nums)

    def test_reverse_even_length(self) -> None:
        nums = [10, 20, 30, 40, 50, 60]
        self.assertEqual([10, 20, 30, 40, 50, 60], nums)
        liststuff.reverse(nums)
        self.assertEqual([60, 50, 40, 30, 20, 10], nums)


if __name__ == '__main__':
    unittest.main()

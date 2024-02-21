import unittest
from my_module import max_consecutive_sum  # Asegúrate de reemplazar 'my_module' con el nombre de tu módulo

class TestMaxConsecutiveSum(unittest.TestCase):
  def test_max_consecutive_sum(self):
    self.assertEqual(max_consecutive_sum([1, 2, 3, 4, 5]), 9)
    self.assertEqual(max_consecutive_sum([5, 2, 8, 1, 3]), 10)
    self.assertEqual(max_consecutive_sum([-1, -2, -3, -4, -5]), -3)
    self.assertEqual(max_consecutive_sum([2, 3, -5, 8, -1]), 3)
    self.assertEqual(max_consecutive_sum([2, 3, 5, 8, 1]), 13)

if __name__ == '__main__':
    unittest.main()
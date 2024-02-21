import unittest
from my_module import find_anagrams  # Asegúrate de reemplazar 'my_module' con el nombre de tu módulo

class TestFindAnagrams(unittest.TestCase):
  def test_find_anagrams(self):
    self.assertEqual(find_anagrams(["amor", "roma", "perro"]), ["amor", "roma"])
    self.assertEqual(find_anagrams(["amor", "roma", "perro", "amro"]), ["amor", "roma", "amro"])
    self.assertEqual(find_anagrams(["amor", "roma", "perro", "amro", "mora"]), ["amor", "roma", "amro", "mora"])
    self.assertEqual(find_anagrams(["amor", "roma", "perro", "amro", "mora", "perrito"]), ["amor", "roma", "amro", "mora"])
    self.assertEqual(find_anagrams(["amor", "roma", "perro", "amro", "mora", "perrito", "romaa"]), ["amor", "roma", "amro", "mora"])

if __name__ == '__main__':
  unittest.main()
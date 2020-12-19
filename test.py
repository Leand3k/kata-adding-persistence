import main
import unittest

class TestPersistenceCase1(unittest.TestCase):
    def test_main_int(self):
        numero = 532
        result = main.Persistence(numero)
        
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
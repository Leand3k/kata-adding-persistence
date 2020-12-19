import main
import unittest

class TestPersistenceCase1(unittest.TestCase):
    def test_main_int(self):
        numero = 532
        result = main.Persistence(numero)
        
        self.assertEqual(result, 2)

    def test_main(self):
        numero = 10
        result = main.Persistence(numero)

        self.assertEqual(result, 1)

        

if __name__ == '__main__':
    unittest.main()
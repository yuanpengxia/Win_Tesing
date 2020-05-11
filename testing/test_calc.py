import sys
# print(sys.path)
sys.path.append('..')
import unittest

from python.calc import Calc



class TestCalc(unittest.TestCase):
    def test_add_1(self):
        self.calc = Calc()
        resault = self.calc.Add(1,2)
        print(resault)
        self.assertEqual(3,resault)

if __name__ == '__main__':
    unittest.main()
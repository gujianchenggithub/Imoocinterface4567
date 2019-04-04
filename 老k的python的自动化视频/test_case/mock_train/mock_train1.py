import unittest
from public import modularAA
from unittest import mock


class TestCount(unittest.TestCase):
    def test_add(self):
        count=modularAA.Count()
        count.add=mock.Mock(return_value=7,side_effect=count.add2)
        print(count.add)
        result=count.add(8,5)
        print(result)
        self.assertEqual(result,13)

if __name__ == '__main__':
    unittest.main()

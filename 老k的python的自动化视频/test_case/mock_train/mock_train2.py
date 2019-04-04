import unittest
from unittest import mock
import modularAA
'''mock一个函数'''
class TestCount1(unittest.TestCase):


    @mock.patch('modularAA.add_def')
    def test_add(self,mock_add_def):
        mock_add_def.return_value=1
        mock_add_def.side_effect=modularAA.add_def2
        result=modularAA.add_def(8, 5)
        print(result)
        self.assertEqual(result,13)



if __name__ == '__main__':
    unittest.main()
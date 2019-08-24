import unittest
from py_jenkins_demo import sample as d

class TestSample(unittest.TestCase):

    def test_func_sum(self):
        self.assertEqual(d.func_sum(1, 2), 3)

    def test_func_subtract(self):
        self.assertEqual(d.func_subtract(1, 2), -1)

    def test_func_mul(self):
        self.assertEqual(d.func_mul(1, 3), 3)


    def test_func_div(self):
        self.assertEqual(d.func_div(4, 2), 2.0)

"""
if __name__ == '__main__':
    unittest.main()
"""
"""
def suite():
    test_suite  = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestSample))
    return test_suite

mySuite = suite()
runner = unittest.TextTestRunner()
runner.run(mySuite)
"""


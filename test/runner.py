import unittest
import test_sample 

loader = unittest.TestLoader()
suite  = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_sample))
runner = unittest.TextTestRunner(verbosity=3)
runner.run(suite)

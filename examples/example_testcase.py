
import unittest
import os,sys
import time
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pyunitreport.HtmlTestRunner import HTMLTestRunner

class TestStringMethods(unittest.TestCase):
    """ Example test for HtmlRunner. """

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_error(self):
        """ This test should be marked as error one. """
        raise ValueError

    def test_fail(self):
        """ This test should fail. """
        self.assertEqual(1, 2)

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """
        pass

if __name__ == '__main__':
    import os,sys
    import time
    output = os.path.join(os.path.abspath(os.path.dirname(__file__)),"{}_{}".format(os.path.splitext(os.path.basename(sys.argv[0]))[0] ,time.strftime("%H%M%S", time.localtime())))
    unittest.main(testRunner=HTMLTestRunner(verbosity=2,output=output,report_name=time.strftime("%H%M%S", time.localtime()),report_title='example_testcase',failfast=False))
    
    
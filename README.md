# PyUnitReport

PyUnitReport is a unittest test runner that save test results in Html files, for human readable presentation of results.

## Installation

```bash
$ pip install PyUnitReport
```

## Usage

### testcase

```python
from pyunitreport import HTMLTestRunner
import unittest

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
    unittest.main(testRunner=HTMLTestRunner(output='example_dir'))
```

In most cases, you can use `PyUnitReport` with `unittest.main`, just pass it with the `testRunner` keyword.

For `HTMLTestRunner`, the only parameter you must pass in is `output`, which specifies the directory of your generated report. Also, if you want to specify the report name, you can use the `report_name` parameter, otherwise the report name will be the datetime you run test. And if you want to run testcases in `failfast` mode, you can pass in a `failfast` parameter and assign it to be True.

Here is another way to run the testcases.

```python
from pyunitreport import HTMLTestRunner

kwargs = {
    "output": output_folder_name,
    "report_name": report_name,
    "failfast": True
}
result = HTMLTestRunner(**kwargs).run(task_suite)
```

### testsuite

For those who have `test suites` it works too, just create a runner instance and call the run method with your suite.

Here is an example:

```python
from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
import ExampleTest
import Example2Test

example_tests = TestLoader().loadTestsFromTestCase(ExampleTests)
example2_tests = TestLoader().loadTestsFromTestCase(Example2Test)

suite = TestSuite([example_tests, example2_tests])
kwargs = {
    "output": output_folder_name,
    "report_name": report_name,
    "failfast": True
}
runner = HTMLTestRunner(**kwargs)
runner.run(suite)
```

## Output

### Console output

This is an example of what you got in the console.

```text
$ python examples/testcase.py

Running tests...
----------------------------------------------------------------------
 This test should be marked as error one. ... ERROR (0.000575)s
 This test should fail. ... FAIL (0.000564)s
 test_isupper (__main__.TestStringMethods) ... OK (0.000149)s
 This test should be skipped. ... SKIP (0.000067)s
 test_split (__main__.TestStringMethods) ... OK (0.000167)s
 test_upper (__main__.TestStringMethods) ... OK (0.000134)s

======================================================================
ERROR [0.000575s]: This test should be marked as error one.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "examples/testcase.py", line 23, in test_error
    raise ValueError
ValueError

======================================================================
FAIL [0.000564s]: This test should fail.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "examples/testcase.py", line 27, in test_fail
    self.assertEqual(1, 2)
AssertionError: 1 != 2

----------------------------------------------------------------------
Ran 6 tests in 0.002s

FAILED
 (Failures=1, Errors=1, Skipped=1)

Generating HTML reports...
Template is not specified, load default template instead.
Reports generated: /Users/Leo/MyProjects/ApiTestEngine/src/pyunitreport/reports/example_dir/2017-07-26-23-33-49.html
```

### Html Output

![html output](docs/html_output.gif)

![html output](docs/html_output.png)

import unittest
import function
import os

class TestFunction(unittest.TestCase):

    @unittest.skipUnless('WUNDERGROUND_INFLUX_FUNC_test_proxy' in os.environ, "skipped")
    def test_proxy(self):
        function.proxy()

from main import return_backwards_string, get_mode
import unittest
import os

class TestMain(unittest.TestCase):
    def test_return_backwards_string(self):
        random_string = "This is a random string"
        random_string_reversed = "cipe si siht"
        self.assertEqual(random_string_reversed,
                         return_backwards_string(random_string))
        
        
    def get_test_env(self):
        self.assertCountEqual(os.environ.get("MODE"), get_mode())
        
        
if __name__ == '__main__':
    unittest.main()
        
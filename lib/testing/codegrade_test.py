
  import unittest
  from codegrade import CodeGrade

class TestCodeGrade(unittest.TestCase):
    def setUp(self):
        self.codegrade = CodeGrade()

    def test_codegrade_placeholder(self):
        """Codegrade placeholder test"""
        self.assertEqual(1, 1)
if __name__ == '__main__':
    unittest.main() 

    
import unittest

class PruebaCadenas(unittest.TestCase):
    def test_upper(self):
        self.assertEquals("xopa".upper(),"XOPA")

    def test_isupper(self):
        self.assertTrue("XOPA".isupper())
        self.assertFalse("Xopa".isupper())

    def test_split(self):
        s = "Xopa gente"
        self.assertEqual(s.split(),["Xopa","gente"])
        with self.assertRaises(TypeError):
           s.split(2)

#if __name__== "__main__":
      #unittest.main()
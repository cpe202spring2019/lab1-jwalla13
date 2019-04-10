import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        #Tests that locations are represented correctly
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    def test_eq(self):
        loc1=Location("SLO", 35.3, -120.7)
        loc2=Location("SLO", 35.3, -120.7)
        loc3=Location("Pismo",20,-110)
        #Tests that equality between locations runs correctly
        self.assertTrue(loc1==loc2)
        self.assertFalse(loc1==loc3)

if __name__ == "__main__":
        unittest.main()

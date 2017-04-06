#   Brian Cleary 10353782
#Imports the unittest functions and class for use
import unittest
import math

# not the best practice, should specify the functions to import but with 10 * is fine(According to Darren)
from calculator_brian import *

class testCalculator(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(add(2,2),4)
        self.assertEqual(add(2,6),8)
        self.assertEqual(add(2,0),2)

    def testSubtract(self):
        self.assertEqual(subtract(2,2),0)
        self.assertEqual(subtract(6,2),4)
        self.assertEqual(subtract(7,4),3)
        self.assertEqual(subtract(7,4),3)
        
    def testMultiply(self):
        self.assertEqual(multiply(2,2),4)
        self.assertEqual(multiply(6,2),12)
        self.assertEqual(multiply(7,4),28)        

    def testDivide(self):
        # cannot divide by zero, return error
        self.assertEqual(divide(4, 1), 4)
        self.assertEqual(divide(4, 2), 2)
        self.assertEqual(divide(2, 2), 1) 
        self.assertEqual(divide(5, 4), 1.25) 
        self.assertEqual(divide(1, 0), 'error') 
        
    def testExponent(self):
        # 2**3 = 8
        # 2**0 = 1
        self.assertEqual(exponent(2, 3), 8)
        self.assertEqual(exponent(2, 0), 1)
        
    def testCube(self):
        # 2**3 = 8
        # -2**3 = -8
        self.assertEqual(cube(2), 8)
        self.assertEqual(cube(-2), -8)        

    def testSquare(self):
        # 2**2 = 4
        
        self.assertEqual(square(2), 4)

    def testSqrt(self):
        # 4**0.5 = 2
        # 10**0.5 = 3.162277660168379
        self.assertEqual(sqrt(4), 2)
        self.assertEqual(sqrt(10), 3.16)

    def testRad(self):
        # 90 * 3.1415926536 / 180 = 1.57
        self.assertEqual(rad(90), 1.57)
        
    def testDeg(self):
        # 2**3 = 8
        # 2**0 = 1
        self.assertEqual(deg(1.57), 89.95)
               
        
if __name__ == '__main__': # will only run this section if the file is called from cmd with python in front
    unittest.main()

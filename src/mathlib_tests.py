##
# @author Jan Pryc (xprycj00)
# @file mathlib_tests.py
# @date 22.03.2020
#

from src.mathlib import *
import unittest

##
# @brief Tests "unittest" for addition
# @details Using library unittest to test functionality of calculator
#
class mathlibadd (unittest.TestCase):
   
    ##
    # @brief Function is testing positive numbers added together
    #
    def add_positive_test(self):
        self.assertEqual(add(1,2),3)
        self.assertEqual(add(0,1),1)
        self.assertEqual(add(0,0),0)
        self.assertEqual(add(13333,16666),29999)

    ##
    # @brief Function is testing negative numbers added together
    #    
    def add_negative_test(self):
        self.assertEqual(add(-2,-20),-22)
        self.assertEqual(add(-8,0),-8)
        self.assertEqual(add(-22,-44),-66)
        self.assertEqual(add(0,-1),-1)

    ##
    # @brief Function is testing positive and negative number added together
    #   
    def add_positive_negative_test(self):
        self.assertEqual(add(-1,1),0)
        self.assertEqual(add(1,-2),-1)
        self.assertEqual(add(9,-4),5)
    
    ##
    # @brief Function is testing decimal numbers added together
    #
    def add_decimal_test(self):
        self.assertEqual(add(0.5,0.5),1.0)
        self.assertEqual(add(1.3,0.8),2.1)
        self.assertEqual(add(-0.6,0.8),0.2)
        self.assertEqual(add(-2.5,1.8),-0.7)
        self.assertEqual(add(5.65,-5.65),0.00)

##
# @brief Tests "unittest" for subtraction
# @details Using library unittest to test functionality of calculator
#
class mathlibsub (unittest.TestCase):

    ##
    # @brief Function is testing positive numbers subtracted one from the other
    #
    def sub_positive_test(self):
        self.assertEqual(sub(2,1),1)
        self.assertEqual(sub(4,12),-8)
        self.assertEqual(sub(0,0),0)
        self.assertEqual(sub(2,2),0)    

    ##
    # @brief Function is testing negative numbers subtracted one from the other
    #
    def sub_negative_test(self):
        self.assertEqual(sub(-10,0),-10)
        self.assertEqual(sub(0,-10),10)    
        self.assertEqual(sub(-2,-2),0)    
        self.assertEqual(sub(-265,-35),-230)
    
    ##
    # @brief Function is testing positive and negative number subtracted one from the other
    #
    def sub_negative_positive_test(self):
        self.assertEqual(sub(10,-5),15)    
        self.assertEqual(sub(-5,10),-15)    

    ##
    # @brief Function is testing decimal numbers subtracted one from the other
    #
    def sub_decimal_test(self):
        self.assertEqual(sub(0.5,0.5),0.0)
        self.assertEqual(sub(1.3,-0.8),2.1)
        self.assertEqual(sub(-0.6,0.8),1.4)
        self.assertEqual(sub(-2.5,-1.8),-0.7)
        self.assertEqual(sub(5.65,-5.65),11.3)

##
# @brief Tests "unittest" for multiplication
# @details Using library unittest to test functionality of calculator
#
class mathlibmul (unittest.TestCase):

    ##
    # @brief Function is testing positive numbers multiplied together
    #
    def mul_positive_test(self):
        self.assertEqual(mul(1,1),1)
        self.assertEqual(mul(0,0),0)
        self.assertEqual(mul(0,10),0)
        self.assertEqual(mul(10,0),0)
        self.assertEqual(mul(20,2),40)

    ##
    # @brief Function is testing negative numbers multiplied together
    #
    def mul_negative_test(self):
        self.assertEqual(mul(-1,-1),1)
        self.assertEqual(mul(-0,-0),0)
        self.assertEqual(mul(0,-10),0)
        self.assertEqual(mul(-10,0),0)
        self.assertEqual(mul(-20,-2),40)

    ##
    # @brief Function is testing positive and negative number multiplied together
    #
    def mul_negative_positive_test(self):
        self.assertEqual(mul(1,-1),-1)
        self.assertEqual(mul(-10,10),-100)
        self.assertEqual(mul(-0,0),0)
        self.assertEqual(mul(0,-0),0)

    ##
    # @brief Function is testing decimal numbers multiplied together
    #
    def mul_decimal_test(self):
        self.assertEqual(add(10.11,3.4),34.374)
        self.assertEqual(add(-45.65,3.6879),-168.352635)
        self.assertEqual(add(12.34,-43.21),-30.87)
        self.assertEqual(add(-25.4,-25.6),650.24)

##
# @brief Tests "unittest" for division
# @details Using library unittest to test functionality of calculator
#
class mathlibdiv (unittest.TestCase):

    ##
    # @brief Function for testing division by zero
    #
    def division_by_zero_test(self):
        with self.assertRaises(ValueError):
            div(1, 0)

    ##
    # @brief Function is testing positive numbers divided one by the other
    #
    def div_positive_test(self):
        self.assertEqual(div(3,3),1)
        self.assertEqual(div(2,1),2)
        self.assertEqual(div(0,6),0)

    ##
    # @brief Function is testing negative numbers divided one by the other
    #
    def div_negative_test(self):
        self.assertEqual(div(-6,-3),2)
        self.assertEqual(div(-6,-2),3)
        self.assertEqual(div(-0,-2),0)

    ##
    # @brief Function is testing positive and negative number divided one by the other
    #
    def div_negative_positive_test(self):
        self.assertEqual(div(15,-15),-1)
        self.assertEqual(div(-150,50),-3)
        self.assertEqual(div(150,-30),-5)
        self.assertEqual(div(-0,12),0)

    ##
    # @brief Function is testing decimal numbers divided one by the other
    #
    def div_decimal_test(self):
        self.assertEqual(div(1,3),0.33333333)
        self.assertEqual(div(-6,2),3)
        self.assertEqual(div(15,-30),0.5)
        self.assertEqual(div(-18,-2),9)

##
# @brief Tests "unittest" for power
# @details Using library unittest to test functionality of calculator
#
class mathlibpow (unittest.TestCase):

    ##
    # @brief Function is testing even numbers raised to a power of the other
    #
    def pow_even_test(self):
        self.assertTrue(pow(3,2),9)
        self.assertTrue(pow(-3,2),9)
        self.assertTrue(pow(0,2),0)

    ##
    # @brief Function is testing odd numbers raised to a power of the other
    #
    def pow_odd_test(self):
        self.assertTrue(pow(-3,1),-3)
        self.assertTrue(pow(3,3),27)
        self.assertTrue(pow(-3,3),-27)
 
##
# @brief Tests "unittest" for square root
# @details Using library unittest to test functionality of calculator
#
class mathlibsqrr (unittest.TestCase):

    ##
    # @brief Function for testing root extraction of negative number
    #
    def square_root_negative_test(self):
        with self.assertRaises(ValueError):
            sqrr(-4,2)
            
    ##
    # @brief Function is testing square root
    #       
    def sqaure_root_test(self):
        self.assertTrue(sqrr(25,2),5)
        self.assertTrue(sqrr(8,3),2)
        self.assertTrue(sqrr(0,2),0)
        self.assertTrue(sqrr(25,-2),0.2)
        
            
#!/usr/bin/env python
#-*- coding:utf-8 -*- 

import unittest
from paa_code.multiplicacao import Karatsuba

class KaratsubaTest(unittest.TestCase):

    def test_divide_number_in_two_parts(self):
        number = 12345

        k = Karatsuba()
        (left_part_returned,right_part_returned) = k.divide_number_in_two_parts(number,2)

        self.assertEquals(123,left_part_returned)
        self.assertEquals(45,right_part_returned)

    def test_divide_number_in_two_parts_two_digits(self):
        number = 12

        k = Karatsuba()
        (left_part_returned,right_part_returned) = k.divide_number_in_two_parts(number,1)

        self.assertEquals(1,left_part_returned)
        self.assertEquals(2,right_part_returned)

    def test_define_m_power(self):
        number1 = 123
        number2 = 12345

        k = Karatsuba()

        self.assertEquals(k.define_m_power(number1,number2),1)

    def test_number_of_digits(self):
        number = 123

        k =  Karatsuba()
        resultado = k.number_of_digits(number)

        self.assertEquals(resultado,3)


    def test_multiply(self):
        number_1 = 1234
        number_2 = 5678

        expected_result = 7006652

        k = Karatsuba()
        returned_result = k.multiply(number_1,number_2)

        self.assertEquals(expected_result,returned_result)

    def test_multiply_numbers_with_different_number_of_digits(self):
        number_1 = 12000
        number_2 = 56

        expected_result = 672000

        k = Karatsuba()
        returned_result = k.multiply(number_1,number_2)

        self.assertEquals(expected_result,returned_result)

    def test_multiply_one_number_with_one_digit(self):
        number_1 = 1200
        number_2 = 2

        expected_result = 2400

        k = Karatsuba()
        returned_result = k.multiply(number_1,number_2)

        self.assertEquals(expected_result,returned_result)

if __name__ == "__main__":
    unittest.main()

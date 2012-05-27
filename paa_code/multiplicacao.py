#!/usr/bin/env python
#-*- coding:utf-8 -*- 

import math

class Karatsuba(object):

    def multiply(self,num1,num2):

        if num1 / 10 == 0 or num2 / 10 == 0: # escape da recursão, um dos dois números tem 1 digito
            return num1 * num2

        m_power = self.define_m_power(num1,num2)

        (num1_left,num1_right) = self.divide_number_in_two_parts(num1,m_power)
        (num2_left,num2_right) = self.divide_number_in_two_parts(num2,m_power)

        big_num_multiplication = self.multiply(num1_left,num2_left)
        small_num_multiplication = self.multiply(num1_right,num2_right)
        crossed_mult = self.multiply(num1_left + num1_right,num2_left + num2_right) - \
                big_num_multiplication - small_num_multiplication

        result = (big_num_multiplication * 10 ** (2 * m_power)) + \
                small_num_multiplication + crossed_mult * 10 ** m_power

        return result

    def define_m_power(self,num1,num2):

        digits_of_num1 = self.number_of_digits(num1)
        digits_of_num2 = self.number_of_digits(num2)

        return min(digits_of_num1,digits_of_num2) / 2


    def divide_number_in_two_parts(self,number,m_power):

        left_part = int(math.floor(number / (10 ** m_power)))
        right_part = int(number % (10 ** m_power))

        return (left_part,right_part)

    def number_of_digits(self,number):
        return int(math.floor(math.log(number,10) + 1))

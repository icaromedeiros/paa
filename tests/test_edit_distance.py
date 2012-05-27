#!/usr/bin/env python
#-*- coding:utf-8 -*- 

import unittest
from paa_code.edit_distance import edit_distance, create_distance_matrix

class EditDistanceTest(unittest.TestCase):

    def create_distance_matrix(self):
        rows = 2
        cols = 3

        expected_list = [[0,0,0],[0,0,0]]

        self.assertEquals(expected_list, create_distance_matrix(rows, cols))

    def test_empty_strings(self):
        string1 = ""
        string2 = ""

        self.assertEquals(0, edit_distance(string1, string2))
        self.assertEquals(0, edit_distance(string2, string1))

    def test_one_empty_string(self):
        string1 = ""
        string2 = "abc"

        self.assertEquals(len(string2), edit_distance(string1, string2))
        self.assertEquals(len(string2), edit_distance(string2, string1))

    def test_two_non_empty_strings_same_length(self):
        string1 = "ameixa"
        string2 = "alerta"

        self.assertEquals(3, edit_distance(string1, string2))
        self.assertEquals(3, edit_distance(string2, string1))

    def test_two_non_empty_strings_different_length(self):
        string1 = "sort"
        string2 = "sport"

        self.assertEquals(1, edit_distance(string1, string2))
        self.assertEquals(1, edit_distance(string2, string1))
 
if __name__ == "__main__":
    unittest.main()

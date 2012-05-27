#!/usr/bin/env python
#-*- coding:utf-8 -*- 

from optparse import OptionParser

def main():
    print "\nProblem: Compute edit distance"

    parser = OptionParser()
    parser.add_option("-s1", "--string1", dest="string1")
    parser.add_option("-s2", "--string2", dest="string2")

    (options, args) = parser.parse_args()
    if options.string1 and options.string2:
        distance = edit_distance(options.string1,options.string2)

        print "Distance between %s and %s: %s" % (options.string1,options.string2,distance)
    else:
        print "Wrong parameters. Usage: ./edit_distance -s1 <string1> -s2 <string2>"

def edit_distance(string1,string2):
    rows = len(string1)
    cols = len(string2)

    if not string1 and string2:
        return cols

    if not string2 and string1:
        return rows

    if not string1 and not string2:
        return 0

    distance_matrix = create_distance_matrix(rows,cols)

    for i in range(cols):
        distance_matrix[0][i] = i

    for i in range(rows):
        distance_matrix[i][0] = i

    for i in range(rows):
        for j in range (cols):
            if string1[i] == string2[j]:
                distance_matrix[i][j] = distance_matrix[i-1][j-1]
            else:
                distance_matrix[i][j] = min(distance_matrix[i - 1][j] + 1,  # a deletion
                    distance_matrix[i][j - 1] + 1,  # an insertion
                    distance_matrix[i - 1][j - 1] + 1 # a substitution
                    )

    return distance_matrix[rows-1][cols-1]

def create_distance_matrix(rows,cols):
    distance_matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        distance_matrix.append(row)
    return distance_matrix


if __name__ == "__main__":
    main()

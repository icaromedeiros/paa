#!/usr/bin/env python
#-*- coding:utf-8 -*-

from optparse import OptionParser
import sys

def main():
    print "\nProblema: Ordenar vetores"

    parser = OptionParser()
    parser.add_option("-v", "--vetor", dest="vetor")
    parser.add_option("-i", "--insertion_sort", action="store_true",dest="insertion_sort")    
    parser.add_option("-m", "--merge_sort", action="store_true",dest="merge_sort")
        
    (options, args) = parser.parse_args()
    if options.vetor:
        vetor_splitted = options.vetor.split(",")
        vetor = list()
        for num in vetor_splitted:
            vetor.append(int(num))
            
        print "\nVetor recebido %s" % vetor
        
        vetor_final = list()
            
        if options.insertion_sort:
            vetor_final = insertion_sort(vetor)
        elif options.merge_sort:
            vetor_final = merge_sort(vetor)
            
        print "Vetor final: %s" % vetor_final
    else:
        print "Parâmetros errados"
        
def insertion_sort(vetor):
    vetor_final = list()
    return vetor_final

def merge_sort(vetor):
    if len(vetor) == 1:
        return vetor
    
    vetor_final = list()
        
    meio = len(vetor) / 2

    vetor_esq = merge_sort(vetor[0:meio])
    vetor_dir = merge_sort(vetor[meio:len(vetor)+1])
    vetor_final = intercalacao(vetor_esq,vetor_dir)
    
    return vetor_final

def intercalacao(vetor1,vetor2):
        
    vetor1.append(sys.maxint)
    vetor2.append(sys.maxint)

    i = j = 0
    vetor_final = list()
    
    for k in range(len(vetor1) + len(vetor2) - 2): # -2 por causa das duas inserções acima

        if vetor1[i] < vetor2[j]:
            vetor_final.append(vetor1[i])
            if i + 1 < len(vetor1):
                i += 1
        else:
            vetor_final.append(vetor2[j])
            if j + 1 < len(vetor2):
                j += 1
         
    
    return vetor_final
    
if __name__ == "__main__":
    main()
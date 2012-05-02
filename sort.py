#!/usr/bin/env python
#-*- coding:utf-8 -*- 

from optparse import OptionParser

def main():
    print "\nProblema: Ordenar vetores"

    parser = OptionParser()
    parser.add_option("-v", "--vetor", dest="vetor")
    parser.add_option("-i", "--insertion_sort", action="store_true",dest="insertion_sort")    
    parser.add_option("-m", "--merge_sort", action="store_true",dest="merge_sort")
    parser.add_option("-q", "--quick_sort", action="store_true",dest="quick_sort")

    (options, args) = parser.parse_args()
    if options.vetor:
        vetor_splitted = options.vetor.split(",")
        vetor = list()
        for num in vetor_splitted:
            vetor.append(int(num))

        print "\nVetor recebido %s" % vetor

        vetor_final = list()

        if options.insertion_sort:
            insertion = InsertionSort()
            vetor_final = insertion.sort(vetor)
        elif options.merge_sort:
            merge = MergeSort()
            vetor_final = merge.sort(vetor)
        elif options.quick_sort:
            quick = QuickSort()
            vetor_final = quick.sort(vetor)

        print "Vetor final: %s" % vetor_final
    else:
        print "Parâmetros errados"

class Sort(object):

    def sort(self,vetor):
        pass

class InsertionSort(Sort):

    def sort(self,vetor):
        for i in range(1,len(vetor)):
            key = vetor[i]
            j = i
            while j > 0 and vetor [j-1] > key:
                vetor[j] = vetor [j-1]
                j -= 1
            vetor[j] = key

        return vetor

class MergeSort(Sort):

    def sort(self,vetor):
        if len(vetor) == 1:
            return vetor

        vetor_final = list()

        meio = len(vetor) / 2

        vetor_esq = self.sort(vetor[0:meio])
        vetor_dir = self.sort(vetor[meio:len(vetor)+1])
        vetor_final = self.intercalacao(vetor_esq,vetor_dir)

        return vetor_final

    def intercalacao(self,vetor1,vetor2):

        i = j = 0
        vetor_final = list()

        for k in range(len(vetor1) + len(vetor2)):
            if i >= len(vetor1):
                vetor_final.append(vetor2[j]) 
                j += 1
                continue

            if j >= len(vetor2):
                vetor_final.append(vetor1[i])
                i += 1
                continue

            if vetor1[i] < vetor2[j]:
                vetor_final.append(vetor1[i])
                i += 1
            else:
                vetor_final.append(vetor2[j])
                j += 1


        return vetor_final

class QuickSort(Sort):

    def sort(self,vetor):
        if len(vetor) <= 1:
            return vetor

        less, equal, greater = self.particao(vetor)
        return self.sort(less) + equal + self.sort(greater)

    def particao(self,vetor):
        less, equal, greater = [], [], []
        pivot = self.seleciona_pivo(vetor)

        for x in vetor:
            if x < pivot: 
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)

        return (less, equal, greater)

    def seleciona_pivo(self,vetor):
        return vetor[len(vetor)-1]

class HeapSort(Sort):

    def sort(self,vetor):
        return vetor

class MaxHeap(object):

    def __init__(self,vetor):
        self.vetor = vetor
        self.build_max_heap()

    def build_max_heap(self):
        for i in range(len(self.vetor) / 2,-1,-1):
            self.max_heapify(i)

    def max_heapify(self,indice):
        left = self.left(indice)
        right = self.right(indice)

        valor_indice = self.vetor[indice]
        valor_left = self.vetor[left] if left < len(self.vetor) else None
        valor_right = self.vetor[right] if right < len(self.vetor) else None

        # nó folha
        if not valor_left and not valor_right:
            return

        maior = None
        if valor_left > valor_indice and (not valor_right or self.vetor[left] > self.vetor[right]):
            maior = left
        elif valor_right and self.vetor[right] > self.vetor[indice] and self.vetor[right] > self.vetor[indice]:
            maior = right

        if maior:
            (self.vetor[indice],self.vetor[maior]) = (self.vetor[maior], valor_indice)
            self.max_heapify(maior)

    def left(self,i):
        return 2 * i + 1

    def right(self,i):
        return 2 * i + 2

    def parent(self,i):
        if i == 0 or i == 1:
            return 0
        else:
            if i % 2 == 0:
                return i / 2 - 1
            else:
                return i / 2


if __name__ == "__main__":
    main()

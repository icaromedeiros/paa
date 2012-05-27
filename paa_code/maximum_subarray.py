#!/usr/bin/env python
#-*- coding:utf-8 -*-

from optparse import OptionParser


def main():
    print "\nProblema: Encontrar subcadeia de soma máxima em um vetor de inteiros (positivos e negativos)"

    parser = OptionParser()
    parser.add_option("-v", "--vetor", dest="vetor")
    parser.add_option("-f", "--forca_bruta", action="store_true",dest="forca_bruta")
    parser.add_option("-s", "--sarada", action="store_true",dest="sarada")
    parser.add_option("-d", "--dividir", action="store_true",dest="dividir")
    parser.add_option("-p", "--prog_dinamica", action="store_true",dest="prog_dinamica")
    
    (options, args) = parser.parse_args()
    if options.vetor:
        vetor_splitted = options.vetor.split(",")
        vetor = list()
        for num in vetor_splitted:
            vetor.append(int(num))
            
        print "\nVetor recebido %s" %vetor

        vetor_soma_max = list()
        
        if options.forca_bruta:
            vetor_soma_max = forca_bruta(vetor)
        elif options.sarada:
            vetor_soma_max = sarada(vetor)
        elif options.dividir:
            vetor_soma_max = dividir_e_conquistar(vetor)
        elif options.prog_dinamica:
            vetor_soma_max = prog_dinamica(vetor)
        else:
            print "Digite algum método [-v,-f,-s,-d,-p]"


        if len(vetor_soma_max) > 0:
            print "\nSubcadeia de maior valor: %s" % vetor_soma_max
                
    else:
        print "Input errado"
    

def forca_bruta(vetor):
    """
    Algoritmo de força bruta, complexidade O(n^3)
    """
    print "\nUsando algoritmo de força bruta"

    soma_max = 0
    i = j = 0

    for primeiro in range(len(vetor)):
        
        for ultimo in range(primeiro,len(vetor)):
            soma = 0
            
            for k in range(primeiro,ultimo+1):
                soma += vetor[k]

            if soma > soma_max:
                soma_max = soma
                i = primeiro
                j = ultimo

    return vetor[i:j+1]
    
def sarada(vetor):
    """
    Algoritmo de força bruta melhorado
    """

    soma_max = 0
    i = j = 0

    for primeiro in range(len(vetor)):
        soma = 0

        for ultimo in range(primeiro,len(vetor)):
            soma += vetor[ultimo]

            if soma > soma_max:
                soma_max = soma
                i = primeiro
                j = ultimo

    return vetor[i:j+1]
    
def dividir_e_conquistar(vetor):
    """
    Algoritmo usando a técnica de dividir para conquistar, subdivindo os vetores em vetores menores
    """
    
    left = 0
    right = len(vetor) - 1
    
    if left == right:
            return [vetor[left]]
    else:
        meio = (left + right) / 2
    
        soma_max_borda_esq = soma = 0
        for k in range(meio,-1,-1): # do meio até 0 com decréscimo de -1 por iteração
            soma += vetor[k]
            if soma > soma_max_borda_esq:
                soma_max_borda_esq = soma
    
        soma_max_borda_dir = soma = 0
        for m in range(meio+1,right+1):
            soma += vetor[m]
            if soma > soma_max_borda_dir:
                soma_max_borda_dir = soma
            
        soma_max = soma_max_borda_esq + soma_max_borda_dir
    
        vetor_left_meio = vetor[left:meio+1]
        sum_vetor_left_meio = 0
                
        vetor_meio_right = vetor[meio+1:right+1]
        sum_vetor_meio_right = 0

        vetor_soma_max_left_meio = list()
        if len(vetor_left_meio) > 0:
            vetor_soma_max_left_meio = dividir_e_conquistar(vetor_left_meio)
            sum_vetor_left_meio = sum(vetor_soma_max_left_meio)

        vetor_soma_max_meio_right = list()
        if len(vetor_meio_right) > 0:
            vetor_soma_max_meio_right = dividir_e_conquistar(vetor_meio_right)
            sum_vetor_meio_right = sum(vetor_soma_max_meio_right)

        if soma_max <= sum_vetor_left_meio >= sum_vetor_meio_right:
            return vetor_soma_max_left_meio
        elif soma_max <= sum_vetor_meio_right >= sum_vetor_left_meio:
            return vetor_soma_max_meio_right
        elif sum_vetor_left_meio <= soma_max >= sum_vetor_meio_right:
            return vetor

def prog_dinamica(vetor):
    print "Usando programacao dinamica"
    primeiro = 0
    soma = soma_max = i = j = 0

    for ultimo in range(len(vetor)):
        soma += vetor[ultimo]
        if soma > soma_max:
            soma_max = soma
            i = primeiro
            j = ultimo
        elif soma < 0:
            primeiro = ultimo + 1
            soma = 0

    return vetor[i:j+1]
    
if __name__ == "__main__":
    main()
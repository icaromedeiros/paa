#!/usr/bin/env python
#-*- coding:utf-8 -*- 

import math

class Karatsuba(object):

    def multiplique(self,num1,num2):

        if num1 / 10 == 0 or num2 / 10 == 0: # escape da recursão, um dos dois números tem 1 algarismo
            return num1 * num2

        potencia_m = self.define_potencia_m(num1,num2)

        (num1_esquerda,num1_direita) = self.divide_numero_em_duas_partes(num1,potencia_m)
        (num2_esquerda,num2_direita) = self.divide_numero_em_duas_partes(num2,potencia_m)

        multiplicacao_grandes = self.multiplique(num1_esquerda,num2_esquerda)
        multiplicacao_pequenos = self.multiplique(num1_direita,num2_direita)
        multiplicacao_cruzada = self.multiplique(num1_esquerda + num1_direita,num2_esquerda + num2_direita) - multiplicacao_grandes - multiplicacao_pequenos

        resultado = (multiplicacao_grandes * 10 ** (2 * potencia_m)) + multiplicacao_pequenos + multiplicacao_cruzada * 10 ** potencia_m

        return resultado

    def define_potencia_m(self,num1,num2):

        qtde_algarismos_num1 = self.quantidade_algarismos(num1)
        qtde_algarismos_num2 = self.quantidade_algarismos(num2)

        return min(qtde_algarismos_num1,qtde_algarismos_num2) / 2


    def divide_numero_em_duas_partes(self,numero,potencia_m):

        parte_esquerda = int(math.floor(numero / (10 ** potencia_m)))
        parte_direita = int(numero % (10 ** potencia_m))

        return (parte_esquerda,parte_direita)

    def quantidade_algarismos(self,numero):
        return int(math.floor(math.log(numero,10) + 1))


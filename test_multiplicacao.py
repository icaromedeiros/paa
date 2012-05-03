#!/usr/bin/env python
#-*- coding:utf-8 -*- 

import unittest
from multiplicacao import Karatsuba

class KaratsubaTest(unittest.TestCase):

    def test_divide_numero_em_duas_partes(self):
        numero = 12345

        k = Karatsuba()
        (parte_esquerda_retornada,parte_direita_retornada) = k.divide_numero_em_duas_partes(numero,2)

        self.assertEquals(123,parte_esquerda_retornada)
        self.assertEquals(45,parte_direita_retornada)

    def test_divide_numero_em_duas_partes_dois_algarismos(self):
        numero = 12

        k = Karatsuba()
        (parte_esquerda_retornada,parte_direita_retornada) = k.divide_numero_em_duas_partes(numero,1)

        self.assertEquals(1,parte_esquerda_retornada)
        self.assertEquals(2,parte_direita_retornada)

    def test_define_potencia_m(self):
        numero1 = 123
        numero2 = 12345

        k = Karatsuba()

        self.assertEquals(k.define_potencia_m(numero1,numero2),1)

    def test_quantidade_algarismos(self):
        numero = 123

        k =  Karatsuba()
        resultado = k.quantidade_algarismos(numero)

        self.assertEquals(resultado,3)


    def test_multiplicacao(self):
        numero_1 = 1234
        numero_2 = 5678

        resultado_esperado = 7006652

        k = Karatsuba()
        resultado_retornado = k.multiplique(numero_1,numero_2)

        self.assertEquals(resultado_esperado,resultado_retornado)

    def test_multiplicacao_numeros_algarismos_diferentes(self):
        numero_1 = 12000
        numero_2 = 56

        resultado_esperado = 672000

        k = Karatsuba()
        resultado_retornado = k.multiplique(numero_1,numero_2)

        self.assertEquals(resultado_esperado,resultado_retornado)

    def test_multiplicacao_numeros_com_um_algarismo(self):
        numero_1 = 1200
        numero_2 = 2

        resultado_esperado = 2400

        k = Karatsuba()
        resultado_retornado = k.multiplique(numero_1,numero_2)

        self.assertEquals(resultado_esperado,resultado_retornado)

if __name__ == "__main__":
    unittest.main()

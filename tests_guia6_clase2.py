import unittest
from guia6_clase2 import volumen_esfera, triada_pitagorica , suma, esMultiplo, devolver_el_doble_si_es_par , fahrenheit_a_celsius,es_primo, cuanto_primos_enrango

class test_suma(unittest.TestCase):
    def test_suma_positivos(self):
        self.assertEqual(suma(2,3),5)

    def test_suma_negativos(self):
      self.assertEqual(suma(-4, -7), -11)

class test_volumen(unittest.TestCase):
    #se pueden definir los casos por separado
    def test_volumen_1(self):
        self.assertAlmostEqual(volumen_esfera(1.0), 4.1867, places=4)

    def test_volumen_nulo(self):
        self.assertAlmostEqual(volumen_esfera(0.0), 0.0, places=1)

    def test_volumen_5_25(self):
        self.assertAlmostEqual(volumen_esfera(5.25), 605.82375, places=5)
     
        
class test_triada_pitagorica(unittest.TestCase):
    def test_triada_verdadera_correcta(self):
        self.assertTrue(triada_pitagorica(3,4,5))

    def test_triada_falsa(self):
        self.assertFalse(triada_pitagorica(1,7,9))

    def test_triada_ok_desordenada(self):
        self.assertFalse(triada_pitagorica(5,4,3))


class test_es_multiplo(unittest.TestCase):
    def test_numerosPositivos(self):
        resultado = esMultiplo(20,10)
        self.assertTrue(resultado)

    def test_mismo_numero(self):
        resultado = esMultiplo(2,2)
        self.assertTrue(resultado)

    def test_el_primero_mas_grande_no_multiplo(self):
        resultado = esMultiplo(4,3)
        self.assertFalse(resultado)



class test_devolver(unittest.TestCase):
    def test_numero_par(self):
        resultado = devolver_el_doble_si_es_par(2)
        self.assertEqual(resultado,4)
        
    def test_numero_impar(self):
        resultado = devolver_el_doble_si_es_par(3)
        self.assertEqual(resultado,3)


    def test_cero(self):
        resultado = devolver_el_doble_si_es_par(0)
        self.assertEqual(resultado,0)



class test_temp(unittest.TestCase):
    def test_cero(self):
        resultado = fahrenheit_a_celsius(32)
        self.assertEqual(resultado,0)


class test_esPrimo(unittest.TestCase):
    def test_3(self):
        resultado= es_primo(3)
        self.assertTrue(resultado)
    def test_4(self):
        resultado = es_primo(4)
        self.assertFalse(resultado)

 
    def test_uno(self):
        resultado = es_primo(1)
        self.assertFalse(resultado)

class test_primos_enrango(unittest.TestCase):
     def test_segundo_mayor(self):
         resultado = cuanto_primos_enrango(-3,4)
         resultado_esperado = 2
         self.assertEqual(resultado,resultado_esperado)

     def test_mismo_numero_primo(self):
         resultado= cuanto_primos_enrango(11,11)
         resultado_esperado=1
         self.assertEqual(resultado,resultado_esperado)
     def test_mismo_numero_noPrimo(self):
          resultado = cuanto_primos_enrango(10,10)
          resultado_esperado=0
          self.assertEqual(resultado,resultado_esperado)

     def test_primero_mayor(self):
       resultado= cuanto_primos_enrango(8,2)
       resultado_esperado=4
       self.assertEqual(resultado,resultado_esperado)

    
    


    

if __name__ == '__main__':
    unittest.main(verbosity=2)

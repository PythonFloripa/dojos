import unittest

# Converter um número inteiro para para string pt-br
# Por extenso em padrão brasileiro
# Considerar conjunções


def extenso(numero):
    if (numero < 0):
        return 'menos ' + extenso(-numero)

    unidades = ["zero", "um", "dois", "três",
                "quatro", "cinco", "seis", "sete",
                "oito", "nove", "dez", "onze",
                "doze", "treze", "quatorze", "quinze",
                "dezesseis", "dezessete", "dezoito", "dezenove"]
    
    dezenas = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta',
        'setenta', 'oitenta', 'noventa']
    
    centenas = ['cento', 'duzentos', 'trezentos', 'quatrocentos',
                'quinhentos', 'seiscentos', 'setecentos',
                'oitocentos', 'novecentos']
 
    if numero < 20:
        return unidades[numero]
    elif numero < 100:
        if numero % 10 == 0:
            return dezenas[numero // 10 - 2]
        else:
            return dezenas[numero // 10 - 2] + ' e ' + unidades[numero % 10]
    elif numero == 100:
        return "cem"
    else:
        return centenas[]

class TestDojoMethods(unittest.TestCase):

     def test_numero_simples(self):
        self.assertEqual(extenso(1), "um")
        self.assertEqual(extenso(4), "quatro")
        self.assertEqual(extenso(5), "cinco")
        self.assertEqual(extenso(7), "sete")
        self.assertEqual(extenso(20), "vinte")
    
    
     def test_dezenas(self):
        self.assertEqual(extenso(11), "onze")
        self.assertEqual(extenso(15), "quinze")
        self.assertEqual(extenso(19), "dezenove")
        self.assertEqual(extenso(20), "vinte")
        self.assertEqual(extenso(30), "trinta")
        self.assertEqual(extenso(90), "noventa")

     def test_numero_composto(self):
        self.assertEqual(extenso(27), "vinte e sete")
        self.assertEqual(extenso(94), "noventa e quatro")
     
     def test_numero_negativo(self):
        self.assertEqual(extenso(-1), "menos um")
        self.assertEqual(extenso(-13), "menos treze")
        self.assertEqual(extenso(-42), "menos quarenta e dois")
        
     def test_numero_centenas(self):
        self.assertEqual(extenso(100), "cem")
        self.assertEqual(extenso(124), "cento e vinte e quatro")
     
        
if __name__ == '__main__':
    unittest.main()

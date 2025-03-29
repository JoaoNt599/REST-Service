from django.test import TestCase
from .models import Endereco

class EnderecoModelTest(TestCase):
    
    def setUp(self):
        """ Criação de uma instância de Endereco para ser testada """
        self.endereco = Endereco.objects.create(
            linha1="Rua dos Três Irmãos, 123",
            linha2="Apto 202",
            cidade="São Paulo",
            estado="SP",
            pais="Brasil",
            latitude=-23,
            longitude=-46
        )
    
    def test_create_endereco(self):
        """ Verificar se o endereço foi criado corretamente """ 
        self.assertEqual(self.endereco.linha1, "Rua dos Três Irmãos, 123")
        self.assertEqual(self.endereco.linha2, "Apto 202")
        self.assertEqual(self.endereco.cidade, "São Paulo")
        self.assertEqual(self.endereco.estado, "SP")
        self.assertEqual(self.endereco.pais, "Brasil")
        self.assertEqual(self.endereco.latitude, -23)
        self.assertEqual(self.endereco.longitude, -46)
    
    def test_str_method(self):
        """ Teste do método __str__ """
        self.assertEqual(str(self.endereco), self.endereco.linha1)

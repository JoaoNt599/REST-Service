from django.test import TestCase
from .models import Atracao

class AtracaoModelTest(TestCase):
    
    def setUp(self):
        """ Criação de uma instância de Atracao para ser testada """
        self.atracao = Atracao.objects.create(
            nome="Montanha Russa",
            descricao="Uma montanha russa de alta velocidade.",
            horario_funcionamento="10:00 - 18:00",
            idade_minima=12
        )
    
    def test_create_atracao(self):
        """  Verificar se a atração foi criada corretamente """
        self.assertEqual(self.atracao.nome, "Montanha Russa")
        self.assertEqual(self.atracao.descricao, "Uma montanha russa de alta velocidade.")
        self.assertEqual(self.atracao.horario_funcionamento, "10:00 - 18:00")
        self.assertEqual(self.atracao.idade_minima, 12)
    
    def test_str_method(self):
        """ Teste do método __str__ """
        self.assertEqual(str(self.atracao), self.atracao.nome)


from django.test import TestCase
from django.contrib.auth.models import User
from .models import Avaliacao
from decimal import Decimal


class AvaliacaoModelTest(TestCase):
    
    def setUp(self):
        """ Criação de um usuário para associar à avaliação """
        self.user = User.objects.create_user(username='testuser', password='testpass')
    
    def test_create_avaliacao(self):
        """ Criação de uma avaliação """
        avaliacao = Avaliacao.objects.create(
            user=self.user,
            comentario="Avaliação de teste",
            nota=Decimal('4.50')
        )

        """ 
        Verificar se a avaliação foi criada corretamente 
        A data não deve ser None (auto_now_add)
        """
        self.assertEqual(avaliacao.user, self.user)
        self.assertEqual(avaliacao.comentario, "Avaliação de teste")
        self.assertEqual(avaliacao.nota, Decimal('4.50'))
        self.assertIsNotNone(avaliacao.data)   
    
    def test_str_method(self):
        """ Teste do método __str__ """
        avaliacao = Avaliacao.objects.create(
            user=self.user,
            comentario="Outro comentário",
            nota=Decimal('3.75')
        )

        """ Verificar se o método __str__ retorna o nome do usuário """
        self.assertEqual(str(avaliacao), self.user.username)


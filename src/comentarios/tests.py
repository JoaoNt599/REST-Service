from django.test import TestCase
from django.contrib.auth.models import User
from .models import Comentario

class ComentarioModelTest(TestCase):

    def setUp(self):
        """Configuração inicial"""
        self.usuario = User.objects.create_user(username="testeuser", password="senha123")
        self.comentario = Comentario.objects.create(
            usuario=self.usuario,
            comentario="comentário de teste",
            aprovado=True
        )

    def test_criacao_comentario(self):
        """Verifica se o comentário foi criado corretamente"""
        self.assertEqual(self.comentario.usuario.username, "testeuser")
        self.assertEqual(self.comentario.comentario, "comentário de teste")
        self.assertTrue(self.comentario.aprovado)

    def test_string_representation(self):
        """Verifica se o método __str__ retorna o username"""
        self.assertEqual(str(self.comentario), "testeuser")

    def test_data_automatica(self):
        """Verifica se a data foi gerada automaticamente"""
        self.assertIsNotNone(self.comentario.data)


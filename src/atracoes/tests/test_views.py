from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from atracoes.models import Atracao


class AtracaoViewTest(TestCase):

    def setUp(self):
        """Configura os dados para os testes."""
        self.url = reverse('atracao-list')
        self.atracao_data = {
            'nome': 'Parque de Diversões',
            'descricao': 'Parque com várias atrações',
            'horario_funcionamento': 'De 10h às 22h',
            'idade_minima': 5
        }

    def test_create_atracao_success(self):
        """Testa a criação de uma atração com dados válidos (200 OK)."""
        response = self.client.post(self.url, self.atracao_data, format='json')
        
        # Verifica se o código de status é 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Verifica se a atração foi criada corretamente no banco de dados
        self.assertEqual(Atracao.objects.count(), 1)
        self.assertEqual(Atracao.objects.get().nome, 'Parque de Diversões')

    def test_create_atracao_missing_field(self):
        """Testa a criação de uma atração com campos faltando (400 Bad Request)."""
        data_invalid = self.atracao_data.copy()
        del data_invalid['nome']  # Remove o campo 'nome' para simular erro

        response = self.client.post(self.url, data_invalid, format='json')
        
        # Verifica se o código de status é 400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_atracoes(self):
        """Testa a listagem de atrações (200 OK)."""
        Atracao.objects.create(**self.atracao_data)

        response = self.client.get(self.url, format='json')
        
        # Verifica se o código de status é 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verifica se a resposta contém a atração criada
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nome'], 'Parque de Diversões')

    def test_get_atracao_not_found(self):
        """Testa a tentativa de acessar uma atração que não existe (404 Not Found)."""
        url_not_found = reverse('atracao-detail', args=[2])
        response = self.client.get(url_not_found, format='json')
        
        # Verifica se o código de status é 404 Not Found
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_internal_server_error(self):
        """Testa um erro interno do servidor (500 Internal Server Error)."""
        invalid_url = '/invalid-url/'
        response = self.client.get(invalid_url)
        
        # Verifica se o código de status é 500 Internal Server Error
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

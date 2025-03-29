from django.test import TestCase
from atracoes.models import Atracao
from django.core.exceptions import ValidationError

class AtracaoModelTest(TestCase):

    def test_atracao_creation(self):
        """Testa a criação de uma atração com dados válidos."""
        atracao = Atracao.objects.create(
            nome="Parque Nacional",
            descricao="Parque para atividades ao ar livre.",
            horario_funcionamento="De 8h às 18h",
            idade_minima=10
        )
        # Verifica se o objeto foi criado com sucesso
        self.assertEqual(atracao.nome, "Parque Nacional")
        self.assertEqual(atracao.descricao, "Parque para atividades ao ar livre.")
        self.assertEqual(atracao.horario_funcionamento, "De 8h às 18h")
        self.assertEqual(atracao.idade_minima, 10)

    def test_nome_required(self):
        """Testa se o campo 'nome' é obrigatório."""
        atracao = Atracao(
            descricao="Descrição válida",
            horario_funcionamento="De 9h às 17h",
            idade_minima=5
        )
        with self.assertRaises(ValidationError):
            atracao.full_clean()  # Tenta validar e esperar uma exceção

    def test_descricao_required(self):
        """Testa se o campo 'descricao' é obrigatório."""
        atracao = Atracao(
            nome="Atração sem descrição",
            horario_funcionamento="De 10h às 20h",
            idade_minima=12
        )
        with self.assertRaises(ValidationError):
            atracao.full_clean() 

    def test_horario_funcionamento_required(self):
        """Testa se o campo 'horario_funcionamento' é obrigatório."""
        atracao = Atracao(
            nome="Atração sem horário",
            descricao="Descrição válida",
            idade_minima=12
        )
        with self.assertRaises(ValidationError):
            atracao.full_clean() 

    def test_idade_minima_required(self):
        """Testa se o campo 'idade_minima' é obrigatório."""
        atracao = Atracao(
            nome="Atração sem idade mínima",
            descricao="Descrição válida",
            horario_funcionamento="De 10h às 20h"
        )
        with self.assertRaises(ValidationError):
            atracao.full_clean()  

    def test_str_method(self):
        """Testa o método __str__ do modelo Atracao."""
        atracao = Atracao.objects.create(
            nome="Parque de Diversões",
            descricao="Parque de diversões para todas as idades.",
            horario_funcionamento="Das 10h às 22h",
            idade_minima=5
        )
        self.assertEqual(str(atracao), "Parque de Diversões")


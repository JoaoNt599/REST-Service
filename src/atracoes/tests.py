from django.test import TestCase
from .models import Atracao
from django.core.exceptions import ValidationError


class AtracaoModelTest(TestCase):
    def test_atracao_nome_obrigatorio(self):
        """Testa se o campo 'nome' é obrigatório"""
        atracao = Atracao(
            descricao="Uma atração turística",
            horario_funcionamento="9h às 18h",
            idade_minima=12
        )
        with self.assertRaises(ValidationError):
            atracao.full_clean() 

    def test_atracao_descricao_obrigatorio(self):
        """Testa se o campo 'descricao' é obrigatório"""
        atracao = Atracao(
            nome="Passeio no parque",
            horario_funcionamento="9h às 18h",
            idade_minima=12
        )
        with self.assertRaises(ValidationError):
            atracao.full_clean()

    def test_atracao_horario_funcionamento_obrigatorio(self):
        """Testa se o campo 'horario_funcionamento' é obrigatório"""
        atracao = Atracao(
            nome="Passeio no parque",
            descricao="Uma atração turística",
            idade_minima=12
        )
        with self.assertRaises(ValidationError):
            atracao.full_clean()

    def test_atracao_idade_minima_obrigatoria(self):
        """Testa se o campo 'idade_minima' é obrigatório"""
        atracao = Atracao(
            nome="Passeio no parque",
            descricao="Uma atração turística",
            horario_funcionamento="9h às 18h",
        )
        with self.assertRaises(ValidationError):
            atracao.full_clean()

    def test_atracao_criar_com_dados_validos(self):
        """Testa se é possível criar uma instância com dados válidos"""
        atracao = Atracao(
            nome="Passeio no parque",
            descricao="Uma atração turística",
            horario_funcionamento="9h às 18h",
            idade_minima=12
        )
        try:
            atracao.full_clean()
            atracao.save() 
        except ValidationError:
            self.fail("O modelo Atracao não passou na validação, mas deveria.")

        # Verifica se a instância foi salva corretamente
        self.assertEqual(Atracao.objects.count(), 1)
        self.assertEqual(Atracao.objects.first().nome, "Passeio no parque")

from django.db import models


class Atracao(models.Model):

    nome = models.CharField(
        max_length=150,
        blank=False,
        error_messages={
            "blank": "O campo 'nome' não pode estar em branco."
        }
    )

    descricao = models.TextField(
        blank=False,
        error_messages={
            "blank": "O campo 'descrição' não pode estar em branco."
        }
    )

    horario_funcionamento = models.TextField()
    idade_minima = models.IntegerField()
    foto = models.ImageField(upload_to='atracoes', null=True, blank=True)


    def __str__(self):
        return self.nome
    


from django.db import models

# Create your models here.
class Categorias(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome

class Transacao(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    observacao = models.TextField(null=True, blank=True)
    class Meta:
        verbose_name_plural = "Transacoes"
    def __str__(self):
        return self.descricao
from django.db import models
from produto.models import Produtos, Cores
class Entradas(models.Model):
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE, verbose_name="Produto")
    preco = models.DecimalField("Preço", decimal_places=2, max_digits=8, default=0)
    quantidade = models.IntegerField("Quantidade", default=0)
    cor = models.ForeignKey(Cores, on_delete=models.PROTECT, verbose_name='Cor')
    criado = models.DateTimeField("Criado em", auto_now_add=True)
    modificado = models.DateTimeField("Modificado em", auto_now=True)

    def __str__(self) -> str:
        return self.produto.produto

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-produto']
    
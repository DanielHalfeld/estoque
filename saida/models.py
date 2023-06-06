from django.db import models
from produto.models import Produtos
class Saidas(models.Model):
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE, verbose_name="Produto")

    preco = models.DecimalField("Preço", decimal_places=2, max_digits=8, default=0)

    quantidade = models.IntegerField("Quantidade", default=0)

    retirado = models.DateTimeField("Retirado em", auto_now_add=True)
    
    modificado = models.DateTimeField("Modificado em", auto_now=True)

    def __str__(self) -> str:
        return self.produto.produto

    class Meta:
        verbose_name = 'Saida'
        verbose_name_plural = 'Saidas'
        ordering = ['-produto']
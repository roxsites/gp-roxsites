from django.db import models

class Produto(models.Model):
    produto_nome = models.CharField(max_length=40)
    produto_marca = models.CharField(max_length=30)
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='produtos_fotos', null=True, blank=True)

    def __str__(self):
        return self.produto_nome + ' ' + self.produto_marca
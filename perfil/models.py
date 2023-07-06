from django.db import models

class Categoria(models.Model): # é referente a uma tabela do banco de dados
    categoria = models.CharField(max_length=50) # é referente a uma coluna do banco de dados
    essencial = models.BooleanField(default=False) # se a categoria é essencial ou não
    valor_planejamento = models.FloatField(default=0) # valor que o usuário planejou gastar na categoria
    def __str__(self): 
        return self.categoria
    
class Conta(models.Model):
    banco_choices = (
        ('NU', 'Nubank'),
        ('CE', 'Caixa econômica'),
    )

    tipo_choices = (
        ('pf', 'Pessoa Física'),
        ('pj', 'Pessoa Jurídica'),
    )
    
    apelido = models.CharField(max_length=50)
    banco = models.CharField(max_length=2, choices=banco_choices)
    tipo = models.CharField(max_length=2, choices = tipo_choices)
    valor = models.FloatField()
    icone = models.ImageField(upload_to='icones')

    def __str__(self):
        return self.apelido
from django.db import models
from datetime import datetime
# Vamos criar uma classe Model que futuramente ira se torna uma tabela 
'''
Investimento
Valor
Pago
Data
'''
class Investimento(models.Model):
    # tipos das colunas dessa tabela na classe 
    investimento = models.TextField(max_length=255) # max_length expecifica o tamanho do campo
    valor = models.FloatField()
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now)
from django.db import models

class Entry(models.Model):
    value = models.FloatField(verbose_name='Valor Recebido')
    origin = models.CharField(max_length=100, verbose_name='Origem')
    date = models.DateField(verbose_name='Data Recebimento')

    def __str__(self):
        return self.origin


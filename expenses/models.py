from django.db import models

class Status(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Expenses(models.Model):
    id = models.AutoField(primary_key=True)
    exp_name = models.CharField(max_length=200, verbose_name='Despesa')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default='Pendente', related_name='expense_status')
    value = models.FloatField(blank=True, null=True, verbose_name='Valor')
    payday = models.DateField(blank=True, null=True, verbose_name='Data de Pagamento')

    def __str__(self):
        return self.exp_name
    

class Extract(models.Model):
    total_exp = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.total_exp
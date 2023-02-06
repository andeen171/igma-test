from django.db import models


class Client(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['-created_at']

from django.db import models

# Create your models here.
class compromisso(models.Model):
    titulo = models.TextField(max_length=50)
    descricao = models.TextField(max_length=500)
    data = models.DateField()

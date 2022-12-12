from django.db import models

# Create your models here.
class DispModel(models.Model):
    addr = models.CharField(max_length=100, unique=True)
    local = models.CharField(max_length=100)
    funcao = models.CharField(max_length=400)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.addr

class ReportModel(models.Model):
    addr = models.ForeignKey(DispModel, on_delete=models.CASCADE, related_name="reports")
    status = models.CharField(max_length=100)
    bits = models.CharField(max_length=50)
    horario = models.DateTimeField()
    timestamp = models.IntegerField()

    def __str__(self):
        return self.addr.nome




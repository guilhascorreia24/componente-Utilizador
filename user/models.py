from django.db import models
class Utilizador(models.Model):
    idutilizador = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    email = models.CharField(unique=True, max_length=45, blank=True, null=True)
    telefone = models.CharField(unique=True, max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    username = models.CharField(db_column='userName', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'utilizador'

    def __str__(self):
        return str(self.idutilizador)

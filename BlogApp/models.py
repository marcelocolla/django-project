from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length = 100)
    imageurl = models.ImageField(upload_to='images/')
    resumo = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.name

class Comentario(models.Model):
    nome = models.CharField(max_length = 100)
    mensagem = models.CharField(max_length = 300)
    blog = models.ManyToManyField(Blog)

    def __str__(self):
        return self.nome

from django.db import models

# Create your models here.
class Blog(models.Model):
    titulo = models.CharField(max_length = 100)
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    resumo = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    nome = models.CharField(max_length = 100)
    mensagem = models.TextField()
    createAt = models.DateTimeField(auto_now_add=True, blank=True)
    blog = models.ForeignKey(Blog, default="", on_delete=models.CASCADE, related_name='cmm')

    def __str__(self):
        return self.nome

from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    imagem = models.FileField(upload_to = 'pic_folder/', blank=True)

    def __str__(self):
        return self.titulo
from django.forms import ModelForm
from Lab1.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields=['titulo', 'texto', 'imagem']
from django.shortcuts import render, redirect
from Lab1.models import Post
from Lab1.forms import PostForm

# Create your views here.
def home(request):
    return render(request, 'Lab1/index.html')


def lista(request):
    lista = Post.objects.all().order_by('-id')
    return render(request, 'Lab1/lista.html', {'posts':lista})   

def novo(request):
    form = PostForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(lista)

    return render(request,'Lab1/novo.html', {'form':form})
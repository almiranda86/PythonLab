from django.conf.urls import url
from Lab1.views import home, lista, novo

urlpatterns = [
    url(r'^$', home),
    url(r'^listar', lista),
    url(r'^novo', novo),
]
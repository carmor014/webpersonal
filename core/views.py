from django.shortcuts import render, HttpResponse

htmal_base = """
<h1>Chorizos Charala</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me/">Acerca de</a></li>
    <li><a href="/portafolio/">Portafolio</a></li>
    <li><a href="/contacto/">Contactanos</a></li>
<ul>
"""

# Create your views here.


def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")




def contacto(request):
    return render(request, "core/contacto.html")
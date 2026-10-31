##
# paginas - views.py
##
from django.shortcuts import render

def home (request):
    return render(
        request,
         'paginas/home.html', 
         {'titulo': "Pagina Principal"}
    )

#sobre ()  -  retorna a pagina estatica paginas/ sobre.html

def sobre(request):
    return render(
        request,
        "paginas/sobre.html",
        {"titulo": "Sobre Nós"},
    )

# politica_privacidade () - retorna a página estática paginas/politica_privacidade.html

def politica_privacidade(request):
    return render(
        request,
        "paginas/politica_privacidade.html",
        {"titulo": "Política de Privacidade"},
    )


from django.http import HttpResponse


def test_view(request):
        return HttpResponse("esta é a rota de teste")

def index_view(request):
        return HttpResponse("<h1>esta é a rota de views<h1>")
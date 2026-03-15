from django.http import HttpRequest, HttpResponse

def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, World! This is a Blog Projet in Django v6.")

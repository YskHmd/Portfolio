from django.http import HttpResponse 
from django.views.generic import TemplateView

def helloworldfanction(request):
    returnedObject = HttpResponse('<h1>Hello world</h1>')
    return returnedObject
""""HttpResponseを使ってurls.pyからのリクエストを返す"""

class HelloWorldClass(TemplateView):
    template_name = 'hello.html'
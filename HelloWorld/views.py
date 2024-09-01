from django.http import HttpResponse 

def helloworldfanction(request):
    returnedObject = HttpResponse('<h1>Hello world</h1>')
    return returnedObject
""""HttpResponseを使ってurls.pyからのリクエストを返す"""
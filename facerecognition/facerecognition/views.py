from django.http import HttpResponse

def doSomething(request):
    return HttpResponse("Some information")
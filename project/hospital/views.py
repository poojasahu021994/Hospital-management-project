from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
 
def apponimant(request):
    return render(request, 'apponimant.html')

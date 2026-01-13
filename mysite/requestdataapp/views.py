from django.shortcuts import render
from .forms import UserBioForm

def req(request):
    return render(request, 'requestdataapp/request-query-params.html')


def bio(request):
    context = {
        'form': UserBioForm()
    }
    return render(request, 'requestdataapp/user-bio-form.html', context)

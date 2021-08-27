from django.shortcuts import render,get_object_or_404,redirect
from django.views import generic
from .models import Aula
from .forms import NovaAulaForm
from django.contrib import messages
import os
import socket

# Create your views here.


def reload():
    try:
        HOST = 'localhost'    # The remote host
        PORT = 50007              # The same port as used by the server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(b'reload')
    except:pass

class Autoclass(generic.ListView,generic.FormView):
    
    template_name='index.html'
    context_object_name='aulas'
    model = Aula
    form_class= NovaAulaForm
    success_url="/crud/adcionar"
    

def DeleteAula(request,pk):
    reload()
    '''Deleta uma aula da base de dados'''
    
    aula=get_object_or_404(Aula,pk=pk)
    aula.delete()
    return(redirect("crud:Autoclass"))

class NovaAula(generic.FormView):

    template_name='form.html'
    form_class= NovaAulaForm
    
    success_url="/crud/adcionar"

def AddAula(request):
 
    nova=NovaAulaForm(request.POST,instance=Aula())
    if nova.is_valid():
        nova.save()
    reload()
    return(redirect("crud:Autoclass"))
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, ListView,UpdateView,DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from Universidad.Apps.ventas.forms import NewClienteForm
from Universidad.Apps.ventas.models import Cliente

# Create your views here.

"""

def login_(request):
    
    return render(request, 'welcome.html', {})



def inicio(request):
    
    return render(request, 'welcome.html', {})
"""

def foo(request):
	return render(request, 'welcome.html')
    #return HttpResponse("Hello World!")


def index(request):
    
    return render(request, 'welcome.html', {})


class RegisterCliente(CreateView):
    model = Cliente
    template_name = "register.html"
    pk_url_kwarg = 'registerpk'
    form_class = NewClienteForm
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        form.instance.contrato = self.request.user.id
        return super(RegisterUser, self).form_valid(form)
from django.conf.urls import patterns, include, url
from . import views
from django.contrib.auth.decorators import login_required

from Apps.ventas.views import *

urlpatterns = [
    url(r'^register', RegisterCliente.as_view(), name = 'register' ),
]
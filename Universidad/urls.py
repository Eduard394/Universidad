from django.contrib import admin
from django.contrib.auth.decorators import login_required
from Universidad.Apps.ventas.views import foo
from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^clientes/', include('Universidad.Apps.ventas.urls')),
    #url(r'^inicio$', login_required(views.home), name = 'inicio' ),
    #url(r'^login/$', login_, name='login_'),
    url(r'inicio/$', foo),


]

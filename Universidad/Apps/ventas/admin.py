# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Universidad.Apps.ventas.models import *

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(Cartera)
admin.site.register(Abono)



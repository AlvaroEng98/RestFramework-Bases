from django.urls import path
from inmuebleslist_app.api.views import listar_inmuebles, inmueble_detalle

urlpatterns = [
    
    
    path('list/', listar_inmuebles, name='inmuebles-list'),
    path('<int:x>', inmueble_detalle, name='inmueble-id'),


]

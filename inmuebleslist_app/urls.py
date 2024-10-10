from django.urls import path
from inmuebleslist_app.views import listar_inmuebles,inmueble_for_id

urlpatterns = [
    
    
    path('list/', listar_inmuebles, name='inmuebles-list'),
    path('<int:x>', inmueble_for_id, name='inmueble-id'),


]

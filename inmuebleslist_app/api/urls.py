from django.urls import path
#from inmuebleslist_app.api.views import listar_inmuebles, inmueble_detalle
from inmuebleslist_app.api.views import InmuebleDetalleAV, InmuebleListAV,EmpresaListAV, EmpresaDetalleAV

urlpatterns = [
    
    
    # path('list/', listar_inmuebles, name='inmuebles-list'),
    # path('<int:x>', inmueble_detalle, name='inmueble-id'),
      path('list/', InmuebleListAV.as_view(), name='inmuebles-list'),
      path('<int:id>', InmuebleDetalleAV.as_view(), name='inmueble-id'),


      path('empresas/', EmpresaListAV.as_view(), name='empresa-list'),
      path('empresas/<int:id>', EmpresaDetalleAV.as_view(), name='empresa-id'),
      

]

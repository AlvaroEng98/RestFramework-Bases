from django.urls import path
#from inmuebleslist_app.api.views import listar_inmuebles, inmueble_detalle
from inmuebleslist_app.api.views import EdificacionListAV, EdificacionDetalleAV,EmpresaAV, EmpresaDetalleAV

urlpatterns = [
    
    
    # path('list/', listar_inmuebles, name='inmuebles-list'),
    # path('<int:x>', inmueble_detalle, name='inmueble-id'),
      path('list/', EdificacionListAV.as_view(), name='edificacion-list'),
      path('<int:id>', EdificacionDetalleAV.as_view(), name='edificacion-detalle'),


      path('empresas/', EmpresaAV.as_view(), name='empresa-list'),
      path('empresas/<int:id>', EmpresaDetalleAV.as_view(), name='empresa-detalle'),
      

]

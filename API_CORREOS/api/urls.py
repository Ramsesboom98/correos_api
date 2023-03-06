from django.urls import path
from .views import CorreoView
urlpatterns = [
    path('correos/',CorreoView.as_view(), name='correos_list'),
    path('correos/<int:id>',CorreoView.as_view(), name='correos_list'),
    path('correos/destinatario/<str:destinatario>',CorreoView.as_view(), name='correos_list'),
    path('correos/emisor/<str:emisor>',CorreoView.as_view(), name='correos_list'),
    path('correos/fecha/<str:fecha>',CorreoView.as_view(), name='correos_list'),
    path('correos/empresa/<str:empresa>',CorreoView.as_view(), name='correos_list'),
    path('correos/codigoSMTP/<str:codigoSMTP>',CorreoView.as_view(), name='correos_list'),
    path('correos/contenido/<str:contenido>',CorreoView.as_view(), name='correos_list'),
    path('',CorreoView.index,name='index'),

    
    path('destinatario/<str:destinatario>',CorreoView.index,name='index'),
    path('emisor/<str:emisor>',CorreoView.index,name='index'),
    path('fecha/<str:fecha>',CorreoView.index,name='index'),
    path('empresa/<str:empresa>',CorreoView.index,name='index'),
    path('codigoSMTP/<str:codigoSMTP>',CorreoView.index,name='index'),
    path('contenido/<str:contenido>',CorreoView.index,name='index')
]
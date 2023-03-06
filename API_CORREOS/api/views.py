from django.shortcuts import render
from django.views import View 
from .models import Correo
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import timezone

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
class CorreoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,destinatario="",emisor="",fecha="",empresa="",codigoSMTP="",contenido=""):

        correos=[]
        #----------------------------------------------------------------------------------
        if(destinatario!=""):
            correos = list(Correo.objects.filter(destinatario__contains=destinatario).values())
            print("destinatario")
        elif(emisor!=""):
            correos = list(Correo.objects.filter(emisor__contains=emisor).values())
            print("emisor")
        elif(fecha!=""):
            correos = list(Correo.objects.filter(fecha__contains=fecha).values())
            print("fecha")
        elif(empresa!=""):
            correos = list(Correo.objects.filter(empresa__contains=empresa).values())
            print("empresa")
        elif(codigoSMTP!=""):
            correos = list(Correo.objects.filter(codigoSMTP__contains=codigoSMTP).values())
            print("codigoSMTP")
        elif(contenido!=""):
            correos = list(Correo.objects.filter(contenido__contains=contenido).values())
            print("contenido")
        #----------------------------------------------------------------------------------
        #print("-----------------")
        if len(correos)>0:
            datos={'messagge':"Success",'correos':correos}
            #aqui hacer la busqueda
        else:
            print("vacio----------------------------------------")
            datos = {'messagge':"Correos not found ... Empty list",'correos':correos}
        return JsonResponse(datos)
    
    
    def post(self,request):
        #el json que se manda es request.body
        jd = json.loads(request.body) # para mandar como diccionario

        empresa = jd['empresa']
        lista_empresas = ['empresa1', 'empresa2', 'empresa3']
        
        if empresa in lista_empresas:
            Correo.objects.create(
                destinatario = jd['destinatario'],
                emisor =  jd['emisor'],
                fecha= jd['fecha'],
                empresa =jd['empresa'], 
                codigoSMTP = jd['codigoSMTP'],
                contenido = jd['contenido']
            )

            datos = {'messagge':"Success POST ..."}
        else:
            datos = {'messagge':"La empresa no se encuentra registrada ..."}
        #
        return JsonResponse(datos)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        correos = list(Correo.objects.filter(id=id).values())
        if len(correos)>0:
            correo = Correo.objects.get(id=id)
            print("aqio llefo")
            correo.destinatario = jd['destinatario'],
            correo.emisor =  jd['emisor'],
            #correo.fecha= jd['fecha'],
            #expected string or bytes-like object
            correo.fecha= jd['fecha'],
            correo.empresa =jd['empresa'], 
            correo.codigoSMTP = jd['codigoSMTP'],
            correo.contenido = jd['contenido']
            print(type(jd['contenido']))

            #correo.save()
            
            datos = {'messagge':"Dato actualizado"}
        else:
            datos = {'messagge':"La empresa no se encuentra registrada ..."}
        return JsonResponse(datos)

        
    def delete(self,request):
        correos = list(Correo.objects.filter(id=id).values())
        if len(correos)>0:
            Correo.objects.filter(id=id).delete()
            datos = {'messagge':"Dato eliminado"}
        else:
            datos = {'messagge':"No se encontro el correo ..."}
        return JsonResponse(datos)
    
    def index(request,destinatario="",emisor="",fecha="",empresa="",codigoSMTP="",contenido=""):
        lista_correos = []
        

        #print("-----------------------------------------------------------");
        if(destinatario!=""):
            lista_correos = Correo.objects.filter(destinatario__contains=destinatario).all()
            print("destinatario")
        elif(emisor!=""):
            lista_correos = Correo.objects.filter(emisor__contains=emisor).all()
            print("emisor")
        elif(fecha!=""):
            lista_correos = Correo.objects.filter(fecha__contains=fecha).all()
            print("fecha")
        elif(empresa!=""):
            lista_correos = Correo.objects.filter(empresa__contains=empresa).all()
            print("empresa")
        elif(codigoSMTP!=""):
            lista_correos = Correo.objects.filter(codigoSMTP__contains=codigoSMTP).all()
            print("codigoSMTP")
        elif(contenido!=""):
            lista_correos = Correo.objects.filter(contenido__contains=contenido).all()
            print("contenido")

        #-------------------------------------
        

        #----------------------------------------------------------------------
        page = request.GET.get('page',1)
        paginator = Paginator(lista_correos,2)
        try:
            correos = paginator.page(page)
        except PageNotAnInteger:
            correos = paginator.page(1)
        except EmptyPage:
            correos = paginator.page(paginator.num_pages)

        return render(request,'index.html',{'correos':correos})
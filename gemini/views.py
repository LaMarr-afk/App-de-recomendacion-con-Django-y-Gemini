from django.shortcuts import render
from .recolectar import info
import google.generativeai as genai


def inicio(request):
    comentario = request.GET.get('comentario')
    genai.configure(api_key="AIzaSyAxGjaJAmogw6Gl841M6CtcO2XvtO7q02o")
    model =genai.GenerativeModel(model_name="gemini-pro") 
    if comentario:
        consulta= comentario + " Devuelve la respuesta en formato html"
        response=model.generate_content(consulta)
        return render(request,'inicio.html',{
        'form':info(),'respuesta':response.text,'comentario':comentario
         })
    return render(request,'inicio.html',{'form':info()})

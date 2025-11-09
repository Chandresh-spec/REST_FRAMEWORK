from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.



@api_view(['GET','POST','PUT'])
def hello_api(request):
    data={
           "name":"chandres",
           "subject":['kannada','english','ds','python'],
           "class":"3rd year"
        }
    
    if request.method=='POST':
        print("YOU HIT POST METHPD")
        return Response(data)
    
    elif request.method=='GET':
        print("YOU HIT GET METHPD")
        return Response(data)
       
    
    elif request.method=='PUT':
        print("YOU HIT PUT METHPD")
        return Response(data)



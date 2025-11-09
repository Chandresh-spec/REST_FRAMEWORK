from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializers
# Create your views here.



@api_view(['GET','POST','PUT','PATCH','DELETE'])
def  hello_api(request):
    if  request.method=="GET":
        st=Student.objects.all()

        serializer=StudentSerializers(st,many=True)

        return Response(serializer.data)

    elif request.method=='POST':
        serializer=StudentSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response("data saved sucesfully")
        return Response(serializer.errors)
    
    elif request.method=='PUT':
        id=request.GET.get('id')

        st=Student.objects.get(id=id)

        serializer=StudentSerializers(st,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response("data updated sucessfully")
        
        return Response(serializer.errors)
    


    elif request.method=='PATCH':
        id=request.GET.get('id')

        st=Student.objects.get(id=id)

        serializer=StudentSerializers(st,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response("data patched sucesfully")
        
        return Response(serializer.errors)
    

        

    elif request.method=="DELETE":
        id=request.GET.get("id")

        st=get_object_or_404(Student,id=id)
        st.delete()

        return Response("deleted sucesfully")





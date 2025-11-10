from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializers,RegisterSerialIzers
from rest_framework.views import APIView

# Create your views here.


@api_view(['POST'])
def registerserialzers(request):
    serializers= RegisterSerialIzers(data=request.data)

    if serializers.is_valid():
        data=serializers.validated_data
        return Response({"message":"sucess"})
    return Response(serializers.errors)



# @api_view(['GET','POST','PUT','PATCH','DELETE'])
# def  hello_api(request):
    # if  request.method=="GET":
        # st=Student.objects.all()

        # serializer=StudentSerializers(st,many=True)

        # return Response(serializer.data)

    # elif request.method=='POST':
        # serializer=StudentSerializers(data=request.data)

        # if serializer.is_valid():
            # serializer.save()
            # return Response("data saved sucesfully")
        # return Response(serializer.errors)
    # 
    # elif request.method=='PUT':
        # id=request.GET.get('id')

        # st=Student.objects.get(id=id)

        # serializer=StudentSerializers(st,data=request.data)

        # if serializer.is_valid():
            # serializer.save()
            # return Response("data updated sucessfully")
        # 
        # return Response(serializer.errors)
    # 


    # elif request.method=='PATCH':
        # id=request.GET.get('id')

        # st=Student.objects.get(id=id)

        # serializer=StudentSerializers(st,data=request.data,partial=True)

        # if serializer.is_valid():
            # serializer.save()

            # return Response("data patched sucesfully")
        # 
        # return Response(serializer.errors)
    # 

        # 

    # elif request.method=="DELETE":
        # id=request.GET.get("id")

        # st=get_object_or_404(Student,id=id)
        # st.delete()

        # return Response("deleted sucesfully")






@api_view(['POST','GET','PUT'])

def StudentDetails(request):

    if request.method=="GET":
        items=Student.objects.all()
        serializers=StudentSerializers(items,many=True)

        return Response(serializers.data)
    elif request.method=="POST":
        serializers=StudentSerializers(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response({"status":"sucess"})
    
        return Response(serializers.errors)
    

    elif request.method=="PUT":
        id=request.GET.get("id")

        st=get_object_or_404(Student,id=id)
        serializers=StudentSerializers(st,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"status":"sucess"})

        return Response(serializers.errors)





class Student_View(APIView):
    def get(self,request):
        st=Student.objects.all()
        serializer=StudentSerializers(st,many=True)
        return  Response(serializer.data)
    

    def post(self,request):
        serializers=StudentSerializers(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response({"message":"sucess"})
        
        return Response(serializers.errors)
    

    def put(self,request):
        id=self.request.GET.get('id')
        st=get_object_or_404(Student,id=id)

        serialzers=StudentSerializers(st,data=request.data)

        if serialzers.is_valid():
            serialzers.save()
            return Response({"sucess":"data  updated sucesfully"})
        

        return Response(serialzers.errors)
    

    def patch(self,request):
        id=self.request.GET.get("id")
        st=get_object_or_404(Student,id=id)

        serializers=StudentSerializers(st,data=request.data,partial=True)

        if serializers.is_valid():
            serializers.save()
            return Response("data patched sucessfully")
        
        return Response(serializers.errors)

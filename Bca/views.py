from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializers
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets

class Student_View(APIView):

    def get(self,request):

        st=Student.objects.all()

        serializer=StudentSerializers(st,many=True)

        return Response(serializer.data)
    

    def post(self,request):
        
        serializer=StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'sucess'})
        return Response(serializer.errors)


    def put(self,request):
        id=self.request.GET.get('id')

        st=get_object_or_404(Student,id=id)

        serializser=StudentSerializers(st,data=request.data)


        if serializser.is_valid():
            serializser.save()
            return Response({"status":"success"})
        return Response(serializser.errors)
    

    def patch(self,request):
        id=self.request.GET.get('id')
        st=get_object_or_404(Student,id=id)

        serializer=StudentSerializers(st,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"status":"updated sucessfully"})
        return Response(serializer.errors)
        
    def delete(self,request):
        id=self.request.GET.get('id')

        st=get_object_or_404(Student,id=id)

        st.delete()
        return Response({"status":"deleted sucesfully"})




class Student_ViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
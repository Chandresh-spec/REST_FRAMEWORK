from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializers,StudentSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

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





class Simple_ViewSet(viewsets.ViewSet):
    
    def list(self,request):
        item=Student.objects.all()
        serializers=StudentSerializers(item,many=True)
        return Response(serializers.data)
    
    def retrieve(self,request,pk=None):
        queryset=Student.objects,all()
        user=get_object_or_404(queryset,pk=pk)
        serializers=StudentSerializers(user)
        return Response(serializers.data)
    



class StudentView(APIView):
    def post(self,request):
        serializer=StudentSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {"status":False,
                 "errors":serializer.errors,
                "message":"Validation failed",},status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer.save()
        
        return Response({
            "status":True,
            "message":"user  created sucesfully"
            },status=status.HTTP_200_OK
        )
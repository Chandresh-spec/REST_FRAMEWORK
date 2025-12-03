from rest_framework.views import APIView
from .models import Student,Info,Teacher
from .serializers import StudentSerializers,StudentSerializer,LoginSerializer,Infoserializer,TeacherSerializer,LoginTeacherserializer,Logintseerializer,CustomStudentSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from  rest_framework.decorators import api_view
from .permission import IsAdminUser
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


class LoginView(APIView):
    def post(self,request):
        serializer=LoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {
                    "message":"validation failed",
                    "status ":False,
                    "errors":serializer.errors
                },status=status.HTTP_400_BAD_REQUEST
            )
        
        username=serializer.validated_data['username']
        password=serializer.validated_data['password']

        user=authenticate(username=username,password=password)

        if not user:
            return Response(
                {
                    "status":False,
                    "message":"usernot found"

                },status=status.HTTP_400_BAD_REQUEST
            )
        
        return Response(
            {"status": True, "message": "Login successful"},
            status=status.HTTP_200_OK
        )
        



class Info_views(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        info=Info.objects.all()
        serializer=Infoserializer(info,many=True)

        return Response(
            serializer.data
        )
    

    def post(self,request):
        serialzer=Infoserializer(data=request.data)

        if not serialzer.is_valid():
            return Response({
                "status":False,
                "message":"validation fails",
                "errors":serialzer.errors
            },status=status.HTTP_400_BAD_REQUEST)
        

        serialzer.save()
        return Response({
            "status":True,
            "message":"saved sucessfully",
            },status=status.HTTP_200_OK)
    
    def put(self,request):
        id=request.GET.get('id')
        info=get_object_or_404(Info,id=id)

        serializer=Infoserializer(info,data=request.data)
        
        if not serializer.is_valid():
            return Response({
                "status":False,
                "message":"validation fails",
                "errors":serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)
        

        serializer.save()
        return Response({
            "status":True,
            "message":"saved sucessfully",
            },status=status.HTTP_200_OK)
    
    def patch(self,request):
        id=request.GET.get('id')
        info=get_object_or_404(Info,id=id)
        serializer=Infoserializer(info,data=request.data,partial=True)
    
        if not serializer.is_valid():
             return Response({
                "status":False,
                "message":"validation fails",
                "errors":serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)
    
        serializer.save()
        return Response({
             "status":True,
             "message":"saved sucessfully",
        },status=status.HTTP_200_OK)
    

    def delete(self,request):
        id=request.GET.get('id')
        obj=get_object_or_404(Info,id=id)

        if obj:
            obj.delete()
            return Response({
                "message":"deleted sucesfully"
                
            },status=status.HTTP_200_OK)
        
        return Response({
            "message":"object not found"
        },status=status.HTTP_400_BAD_REQUEST)





class Product_views(viewsets.ReadOnlyModelViewSet):
    queryset=Info.objects.all()
    serializer_class=Infoserializer




@api_view(['GET','POST','PUT'])
def teacher_view(request):
    if request.method=="GET":
        items=Teacher.objects.all()
        serializer=TeacherSerializer(items,many=True)

        return Response(serializer.data)
    
    elif request.method=="POST":
        serializer=TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"sucessfull"
            },status=status.HTTP_200_OK)
        
        return Response({
            "message":"error found",
            "error":serializer.errors
        },status=status.HTTP_400_BAD_REQUEST)


    elif request.method=="PUT":
        id=request.GET.get('id')

        tc=get_object_or_404(Teacher,id=id)

        serializer=TeacherSerializer(tc,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response({
               "message":"sucessfull"
            },status=status.HTTP_200_OK)
        
        return Response({
          "message":"error found",
          "error":serializer.errors
        },status=status.HTTP_400_BAD_REQUEST)




class TeacherLogin(APIView):


    def post(self,request):
        serializer=LoginTeacherserializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                "status":False,
                "message":"plz enter the right details",
                "error":serializer.errors
            })
        
        serializer.save()
        return Response({
            "status":True,
            "message":"user registered sucesfully"
        },status=status.HTTP_200_OK)



class Login_views(APIView):
    def post(self,request):
        serializer=Logintseerializer(data=request.data)

        if serializer.is_valid():

            username=serializer.validated_data['username']
            password=serializer.validated_data['password']
            user=authenticate(username=username,password=password)
            print(user)

            if user:
                token_obj,_=Token.objects.get_or_create(user=user)
                return Response({
                    "status":True,
                    "message":"user logged in",
                    "token":token_obj.key
                },status=status.HTTP_200_OK)
            
            return Response({
                "message":"user does not exits"
            })
            
        
        return Response({
            "status":False,
            "error":serializer.errors
        },status=status.HTTP_400_BAD_REQUEST)
    

class Student_api(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        return Response({
            "status":"sucess"
        })




class Tester(APIView):
    def post(self,request):
        serializer=CustomStudentSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                "status":False,
                "message":"user doest not exist"
                
                            
                })
        serializer.save()
        return Response({
            serializer.data
        })


from rest_framework_simplejwt.tokens import RefreshToken
class CustomLoginAPI(APIView):
    def post(self,request):
        serializer=Logintseerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                "status":False,
                "message":"plz enter the valid  name"
            })
        
        user=authenticate(username=serializer.validated_data["username"],password=serializer.validated_data['password'])

        if not user:
            return Response({
                "message":"user does not exist"
            })
        
        refresh=RefreshToken.for_user(user)

        return Response({
            "message":"user logged in ",
            "access_token":str(refresh.access_token),
            "refresh_token":str(refresh),
        })
        



class basic_view(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        data=Teacher.objects.all()
        serializer=TeacherSerializer(data,many=True)
        return Response(serializer.data)
    


class AdminOnly_view(APIView):
    permission_classes=[IsAuthenticated,IsAdminUser]

    def get(self,request):
        return Response({"sucess":"sucess"})
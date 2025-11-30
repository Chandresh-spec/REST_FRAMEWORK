from rest_framework import serializers
from .models import Student,Color,Info,Teacher,Profile
from django.contrib.auth.models import User
from rest_framework.response import Response

class RegisterSerialIzers(serializers.Serializer):
    name=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()
    confirm_password=serializers.CharField()

    def validate_name(self,value):
        if len(value)<=3:
            raise serializers.ValidationError("name characater must be greater than 3")
        return value
    
    def validate(self, attrs):
        if attrs['password']!=attrs['confirm_password']:
            raise serializers.ValidationError("password must match")
        
        return attrs

class ColorSerializers(serializers.ModelSerializer):
    class Meta:
        model=Color
        fields=['color']


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
       model=Student
       fields="__all__"
    


    
    def validate_age(self,value):
        if value <5 or value >=25:
            raise serializers.ValidationError("age must be between 5 to 25")
        return value
    

    def validate_grade(self,value):

        if value not in {'A','B','C','D','E'}:
            raise serializers.ValidationError("grade must be in between {'A','B','C','D','E'}")
        
        return value
    

   
    def create(self, validated_data):
        validated_data['name']=validated_data['name'].upper()
        return Student.objects.create(**validated_data)
    

    # def update(self, instance, validated_data):
        # instance.age=validated_data.get("age",instance.age)
        # instance.save()
        # return instance
      

        

class StudentSerializer(serializers.Serializer):
    username=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()


    def validate(self, attrs):
        if User.objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError({"username":"useralready exist"})
        
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({"email":" email already exist"})
        
        return attrs

    def create(self, validated_data):
        user=User.objects.create(username=validated_data['username'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()

        return user


class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
        
        


class Infoserializer(serializers.ModelSerializer):
    class Meta:
        model=Info
        fields="__all__"

    

    def validate_name(self,value):
        if not value.isalpha():
            raise serializers.ValidationError("name must be  in character")
        
        return value
                

    
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields="__all__"
    

    def to_internal_value(self,data):
        data=data.copy()
        branch=data.get('branch')
        if isinstance(branch,str):
            if branch.startswith('1bca'):
               data['branch']='1YEAR'
            elif branch.startswith('2bca'):
               data['branch']='2YEAR'
            else:
               data['branch']='3YEAR'
     
        return super().to_internal_value(data)
    

    def validate_name(self,value):
        if not value.isalpha():
            raise serializers.ValidationError("name must be in alphabet")
        
        return value
    
    # def validate(self,attrs):
        # if attrs['experience']>0 and attrs['branch'] in ['2bca','2bcom','1bsc']:
            # return attrs
        # raise serializers.ValidationError("experience must be greater than 0 and barnch  must ['bca','bcom','bsc']")
    # 


    def to_representation(self, instance):
        rep=super().to_representation(instance)
        rep['experience']=f"{instance.branch} experince of {instance.experience}"

        return rep


class LoginTeacherserializer(serializers.Serializer):
      username=serializers.CharField()
      email=serializers.EmailField()
      password=serializers.CharField()


      def create(self, validated_data):
          user=User.objects.create(username=validated_data['username'],email=validated_data['email'])
          user.set_password(validated_data['password'])
          user.save()
          return user
      
      def update(self, instance, validated_data):
          pass
          


class Logintseerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
        





# class Exampleserializer(serializers.ModelSerializer):
    # created_at=serializers.DateTimeField(read_only=True)
    # secret_note = serializers.CharField(write_only=True, required=False)
    # username=serializers.CharField(required=True)
    # age=serializers.IntegerField(allow_null=True)
    # bio=serializers.CharField(allow_blank=True)
# 
    # role=serializers.CharField(default="member")
    # email_add
# 


    # class Meta:
        # model=Profile



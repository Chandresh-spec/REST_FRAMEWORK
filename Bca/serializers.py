from rest_framework import serializers
from .models import Student,Color
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
        
        
        

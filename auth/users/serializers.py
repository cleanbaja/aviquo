from rest_framework import serializers
from .models import ExtracurricularReference
from django.contrib.auth.models import User

class ECSSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtracurricularReference
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
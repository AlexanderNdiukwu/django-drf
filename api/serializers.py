from rest_framework import serializers
from .models import Todo
# from django.contrib.auth import get_user_model




class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta :
#         model = get_user_model()
#         fields = ['username','profile_pic','bio','phone_number','email']
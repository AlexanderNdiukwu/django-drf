from rest_framework import serializers
from .models import *


class variationvauleserializer(serializers.ModelSerializer):
    # variation = variationserializer()
  
    class Meta:
        model = Variation_value_input
        fields = ('variation_value_id', 'variation','variation_value_value',)


class variationserializer(serializers.ModelSerializer):
    # variation_name = variationvauleserializer(many=True )
    class Meta:
        model = Variation
        fields = ('variation_id','variation_value',)



class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = ['folder_id','folder_name','folder_description','folder_created_at','folder_updated_at']



class statusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['status_id','status_input']




class TodoSerializer(serializers.ModelSerializer):

    # folder = FolderSerializer()
    # status = serializers.StringRelatedField()
    # variation_value_input = variationvauleserializer()
    # items = variationvauleserializer()
    # v_input = variationvauleserializer(many=True,read_only=True)\
    variation_value_input = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Todo
        fields =  ('id','title','folder','status','description','completed','created_at','updated_at','variation_value_input',)


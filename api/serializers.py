from rest_framework import serializers
from .models import *

class variationserializer(serializers.ModelSerializer):
    # variation_name = variationvauleserializer(many=True )
    class Meta:
        model = Variation
        fields = ('variation_id','variation_value',)



class variationvauleserializer(serializers.ModelSerializer):
    # variation = variationserializer()
    got = serializers.CharField(source='variation')  

    class Meta:
        model = Variation_value_input
        fields = ('variation_value_id', 'variation','variation_value_value','got')



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
    # v_input = variationvauleserializer(many=True,read_only=True)
    # variation_value_input = variationvauleserializer(many=True)


    # variation_value_input = variationvauleserializer(many=True)
    # folder = FolderSerializer()
    # variation_value = serializers.CharField(source='variation_value_input')
    folder_name = serializers.CharField(source='folder.folder_description')


    
    class Meta:
        model = Todo
        fields =  ('id','title','folder','status','description','completed','created_at','updated_at','variation_value_input')


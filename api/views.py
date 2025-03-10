from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo
from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.
class ApiTodoView(APIView):
    def get(self , request):
        todo = Todo.objects.all()
        serializer = TodoSerializer(todo , many=True )
        return Response(serializer.data)
    
    def post (self , request ):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class ApiSingleTodo (APIView ):
    def get (self , request , pk ):
        todo = get_object_or_404(Todo,pk=pk )
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    def post(self , request , pk ):
        todo = get_object_or_404(Todo,pk=pk )
        serializer = TodoSerializer(todo , data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self , request , pk ):
        todo = get_object_or_404(Todo,pk = pk )
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

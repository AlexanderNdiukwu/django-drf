from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework import status,generics,permissions
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
# class ApiTodoView(APIView):
#     filter_backend = [DjangoFilterBackend]
#     filter_fields = ['title']
  

#     def get(self , request):
      
#         # todo = Todo.objects.filter(user= request.user)
#         todo = Todo.objects.all()
#         filter_backend = DjangoFilterBackend()
#         queryset = filter_backend.filter_queryset(request, queryset, self)



#         serializer = TodoSerializer(todo , many=True )
      
#         return Response({
#             'todo':serializer.data,
#             'count':len(todo),
          
            
#         })
    

#     def post (self , request ):
#         serializer = TodoSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    

class ApiTodoView(generics.ListCreateAPIView): 
    # queryset = Todo.objects.all() 
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    # permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['title', 'status','completed'] 
    search_fields = ['title','completed']
    
    

    def get_queryset(self):
        user = self.request.user
        # qs = super().get_queryset()
        return Todo.objects.filter(user=user)
 


class ApiSingleTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class= TodoSerializer
    
    

# class ApiSingleTodo (APIView ):
#     def get (self , request , pk ):
#         todo = get_object_or_404(Todo,pk=pk )
#         serializer = TodoSerializer(todo)
#         return Response(serializer.data)
#     def put(self , request , pk ):
#         todo = get_object_or_404(Todo,pk=pk )
#         serializer = TodoSerializer(todo , data= request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     def delete(self , request , pk ):
#         todo = get_object_or_404(Todo,pk = pk )
#         todo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



class ApiStatusView ( APIView):
    def get( self , request ):
        status = Status.objects.all()
        serializers = statusSerializer(status , many=True)
        return Response(serializers.data)
    def post(self ,request ):
        serializers = statusSerializer(data = request.data) 
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
    
class deletestatus(APIView):
    def get (self ,request,pk):
        status = get_object_or_404(Status,pk = pk )
        serializers = statusSerializer(status)
        return Response(serializers.data)
    def delete (self ,request, pk ):
        statuse = get_object_or_404(Status, pk=pk)
        statuse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class ApiFolderview(generics.list)      





class ApiFolderView ( APIView):
    def get( self , request ):
        status = Folder.objects.all()
        serializers = FolderSerializer(status , many=True)
        return Response(serializers.data)
    def post(self ,request ):
        serializers = FolderSerializer(data = request.data) 
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)

class Deletefolder (APIView):
    def get (self ,request,pk):
        folder = get_object_or_404(Folder,pk = pk )
        serializers = FolderSerializer(folder)
        return Response(serializers.data)
    def post (self , request , pk):
        folder = get_object_or_404(Folder,pk=pk )
        serializers= FolderSerializer(folder,data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response (serializers.data)

    def delete (self , request , pk ):
        folder = get_object_or_404(Folder,pk = pk )
        folder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ApiVariationView(APIView):
    def get(self , request):
        variation = Variation.objects.all()
        serializers = variationserializer(variation,many=True)
        return Response(serializers.data)
    def post (self , request ):
        serializers = variationserializer(data = request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
    
class ApiVariationValueview(APIView):
    def get(self , request):
        variationValue = Variation_value_input.objects.all()
        serializers = variationvauleserializer(variationValue,many=True)
        return Response({'value':serializers.data,'count':len(variationValue)})
    def put (self , request ):
        serializers = variationvauleserializer(data = request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
    


class apitodoview(APIView):
    def get (self ,request):
        todo = Todo.objects.all()
        serializers = checkUndoTodo({'count':len(todo)})
        return Response(serializers.data)

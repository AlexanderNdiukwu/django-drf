from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework import status,generics,permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

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
class adminonly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method =='POST':

          return request.user.is_staff
        return True
    

class ApiTodoView(generics.ListCreateAPIView): 
    queryset = Todo.objects.all() 
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    permission_classes = [adminonly]
    pagination_class = PageNumberPagination
    filterset_fields = ['title', 'status','completed'] 
    search_fields = ['title','completed']
    
    

    # def get_queryset(self):
    #     user = self.request.user
    #     return Todo.objects.filter(user=user)
    
    # def create(self, request , *args , **kwargs):
    #     permissions = [permissions.is]
 


class ApiSingleTodo(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class= TodoSerializer


class StatusViewSet(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = statusSerializer

# this is the previous apiview 
# class ApiStatusView ( APIView):
#     def get( self , request ):
#         status = Status.objects.all()
#         serializers = statusSerializer(status , many=True)
#         return Response(serializers.data)
#     def post(self ,request ):
#         serializers = statusSerializer(data = request.data) 
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#         return Response(serializers.data)
    
# class deletestatus(APIView):
#     def get (self ,request,pk):
#         status = get_object_or_404(Status,pk = pk )
#         serializers = statusSerializer(status)
#         return Response(serializers.data)
#     def delete (self ,request, pk ):
#         statuse = get_object_or_404(Status, pk=pk)
#         statuse.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class FolderViewSet (ModelViewSet):
    queryset= Folder.objects.all()
    serializer_class = FolderSerializer    





# class ApiFolderView ( APIView):
#     def get( self , request ):
#         status = Folder.objects.all()
#         serializers = FolderSerializer(status , many=True)
#         return Response(serializers.data)
#     def post(self ,request ):
#         serializers = FolderSerializer(data = request.data) 
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#         return Response(serializers.data)

# class Deletefolder (APIView):
#     def get (self ,request,pk):
#         folder = get_object_or_404(Folder,pk = pk )
#         serializers = FolderSerializer(folder)
#         return Response(serializers.data)
#     def post (self , request , pk):
#         folder = get_object_or_404(Folder,pk=pk )
#         serializers= FolderSerializer(folder,data=request.data)
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#         return Response (serializers.data)

#     def delete (self , request , pk ):
#         folder = get_object_or_404(Folder,pk = pk )
#         folder.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class VariationViewSet (ModelViewSet):
    queryset= Variation.objects.all()
    serializer_class = variationserializer    

class VariationValueViewSet (ModelViewSet):
    queryset= Variation_value_input.objects.all()
    serializer_class = variationvauleserializer    


# class ApiVariationView(APIView):
#     def get(self , request):
#         variation = Variation.objects.all()
#         serializers = variationserializer(variation,many=True)
#         return Response(serializers.data)
#     def post (self , request ):
#         serializers = variationserializer(data = request.data)
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#         return Response(serializers.data)
    
# class ApiVariationValueview(APIView):
#     def get(self , request):
#         variationValue = Variation_value_input.objects.all()
#         serializers = variationvauleserializer(variationValue,many=True)
#         return Response({'value':serializers.data,'count':len(variationValue)})
#     def put (self , request ):
#         serializers = variationvauleserializer(data = request.data)
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#         return Response(serializers.data)
    


class apitodoview(APIView):
    def get (self ,request):
        todo = Todo.objects.all()
        serializers = checkUndoTodo({'count':len(todo)})
        return Response(serializers.data)

from django.urls import path

from . import views 


urlpatterns = [
    path ('todo/',views.ApiTodoView.as_view()),
    path ('todo/<int:pk>',views.ApiSingleTodo.as_view())
 
]
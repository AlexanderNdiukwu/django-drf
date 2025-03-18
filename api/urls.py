from django.urls import path

from . import views 


urlpatterns = [
    path ('todo/',views.ApiTodoView.as_view()),
    path ('todo/<int:pk>',views.ApiSingleTodo.as_view()),
    path ('status/',views.ApiStatusView.as_view()),
    path ('folder/',views.ApiFolderView.as_view()),
    path ('folder/<int:pk>',views.Deletefolder.as_view()),
    path ('status/<int:pk>',views.deletestatus.as_view()),
    path ('Variation/',views.ApiVariationView.as_view()),
    path ('VariationValue/',views.ApiVariationValueview.as_view()),
    # path ('todoinfo/',views.apitodoview.as_view()),
 
]
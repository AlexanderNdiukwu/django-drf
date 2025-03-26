from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import include
from . import views 

router = DefaultRouter()
router.register('status', views.StatusViewSet,basename='status')
router.register('folder',views.FolderViewSet,basename='folder')
router.register('variation',views.VariationViewSet,basename='variation')
router.register('variationvalue',views.VariationValueViewSet,basename='variationvalue')



urlpatterns = [
    path('',include(router.urls)),
    path ('todo/',views.ApiTodoView.as_view()),
    path ('todo/<int:pk>',views.ApiSingleTodo.as_view()),

    # path ('status/',views.ApiStatusView.as_view()),
    # path ('folder/',views.ApiFolderView.as_view()),
    # path ('folder/<int:pk>',views.Deletefolder.as_view()),
    # path ('status/<int:pk>',views.deletestatus.as_view()),
    # path ('Variation/',views.ApiVariationView.as_view()),
    # path ('VariationValue/',views.ApiVariationValueview.as_view()),
    path ('todoinfo/',views.apitodoview.as_view()),
 
]
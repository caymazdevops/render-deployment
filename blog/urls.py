from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet
from . import views

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('', include(router.urls)),
]
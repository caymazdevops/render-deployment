from django.urls import path
from .views import SportListCreateAPIView

urlpatterns = [
    path('sports/', SportListCreateAPIView.as_view(), name='sport-list-create'),
]

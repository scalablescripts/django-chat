from django.urls import path
from .views import MessageAPIView

urlpatterns = [
    path('messages', MessageAPIView.as_view())
]

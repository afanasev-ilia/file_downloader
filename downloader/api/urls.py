from django.urls import path

from api.views import FileAPIView

urlpatterns = [
    path('upload/', FileAPIView.as_view(), name='upload'),
]

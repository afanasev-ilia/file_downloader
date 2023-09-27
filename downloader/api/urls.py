from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import FileAPIView

urlpatterns = [
    path('upload/', FileAPIView.as_view(), name='upload'),

# router = DefaultRouter()
# router.register('files', FileViewSet, basename='files')

# urlpatterns = [
#     path('upload/', include(router.urls), name='upload'),
]

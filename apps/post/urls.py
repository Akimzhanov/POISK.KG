from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import StorageViewSet, FindViewSet, LostViewSet


router = DefaultRouter()
router.register('post', StorageViewSet, 'post')

urlpatterns = [
    path('find-list/', FindViewSet.as_view(), name='find'),
    path('lost-list/', LostViewSet.as_view(), name='lost'),
]

urlpatterns += router.urls
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from user.views import UserViewSet

router = DefaultRouter()
router.register('user', UserViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]

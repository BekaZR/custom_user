from django.urls import path

from rest_framework.routers import DefaultRouter as DR

from mainapp.views import UserView

router = DR()
router.register('user', UserView, basename='user')

urlpatterns = [
    
]

urlpatterns += router.urls
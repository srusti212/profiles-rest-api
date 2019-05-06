from django.conf.urls import url
from . import views
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
# When specifying a modelviewset, DRF automatically figures out by looking at the model registered with the serializer
router.register('profile', views.UserProfileViewSet)

""" This is gonna map to API view """
urlpatterns = [
url(r'^hello-view/', views.HelloApiView.as_view()),
url(r'',include(router.urls))
]

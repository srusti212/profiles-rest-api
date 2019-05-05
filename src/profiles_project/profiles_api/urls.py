from django.conf.urls import url
from . import views
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

""" This is gonna map to API view """
urlpatterns = [
url(r'^hello-view/', views.HelloApiView.as_view()),
url(r'',include(router.urls))
]

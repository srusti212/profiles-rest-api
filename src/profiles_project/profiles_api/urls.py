from django.conf.urls import url
from . import views
""" This is gonna map to API view """
urlpatterns = [
url(r'^hello-view/', views.HelloApiView.as_view())
]

from django.conf.urls import url
from . import views
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
""" There are two mandatory arguments to the register() method: prefix - The URL prefix to use for this set of routes, viewset - The viewset class. """
router = DefaultRouter()

""" The basename argument is used to specify the initial part of the view name pattern.  """

router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

""" Typically you won't need to specify the basename argument,
but if you have a viewset where you've defined a custom get_queryset method,
 then the viewset may not have a .queryset attribute set i.e. if its not a model viewset that is why DRF doesnt know what to call these objects. """

router.register('profile', views.UserProfileViewSet)

router.register('login', views.LoginViewSet, base_name='login')

router.register('feed', views.UserProfileFeedViewSet)

""" This is gonna map to API view """
urlpatterns = [
url(r'^hello-view/', views.HelloApiView.as_view()),
url(r'',include(router.urls))
]

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from robots.views import RSeoStatusViewSet, UserViewSet

router = DefaultRouter()
router.register(r'rseostatus', RSeoStatusViewSet)
router.register(r'users', UserViewSet)

app_name = 'robots'
urlpatterns = [
    url(r'^', include(router.urls)),

]


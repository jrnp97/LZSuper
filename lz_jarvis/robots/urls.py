from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from robots.views import index, RSeoStatusViewSet

router = DefaultRouter()
router.register(r'rseostatus', RSeoStatusViewSet)

app_name = 'robots'
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^robot/$', index, name='index'),

]


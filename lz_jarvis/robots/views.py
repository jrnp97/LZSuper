from django.contrib.auth.models import User
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework import permissions

from robots.tasks import google, duck, yahoo, bing
from robots.models import RSeoStatus
from robots.serializers import RSeoStatusSerializer, UserSerializer
from robots.permissions import IsOwnerOrReadOnly

from celery import group


class RSeoStatusViewSet(viewsets.ModelViewSet):
    queryset = RSeoStatus.objects.all()
    serializer_class = RSeoStatusSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def retrieve(self, request, pk=None, *args, **kwargs):
        response = super(RSeoStatusViewSet, self).retrieve(request, *args, **kwargs)

        tasks_exec = [google, yahoo, bing, duck]
        browser_nav = list(filter(lambda x: response.data[x] is True, ['google', 'yahoo', 'duckduck', 'bing']))

        group(task.s(response.data['keyword']) for task in tasks_exec if
              task.name in browser_nav)().get()

        return JsonResponse({'message': 'Task send successfully'})

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


rseostatus_list = RSeoStatusViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
rseostatus_detail = RSeoStatusViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

from django.contrib.auth.models import User
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework import permissions

from robots.tasks import send_email
from robots.models import RSeoStatus
from robots.serializers import RSeoStatusSerializer, UserSerializer
from robots.permissions import IsOwnerOrReadOnly


class RSeoStatusViewSet(viewsets.ModelViewSet):
    queryset = RSeoStatus.objects.all()
    serializer_class = RSeoStatusSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    # def retrieve(self, request, pk=None, *args, **kwargs):
    #     send_email.delay()
    #     return JsonResponse({'message': 'Task send successfully'})

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


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


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

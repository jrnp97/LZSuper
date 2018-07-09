from django.http import JsonResponse
from django.shortcuts import render

from rest_framework import viewsets

from robots.tasks import send_email
from robots.models import RSeoStatus
from robots.serializers import RSeoStatusSerializer


def index(request):
    if request.method == 'POST':
        send_email.delay()
    return render(request, 'robots/index.html')


class RSeoStatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RSeoStatus.objects.all()
    serializer_class = RSeoStatusSerializer

    def retrieve(self, request, pk=None, *args, **kwargs):
        send_email.delay()
        return JsonResponse({'message': 'Task send successfully'})


rseostatus_list = RSeoStatusViewSet.as_view({
    'get': 'list'
})
rseostatus_detail = RSeoStatusViewSet.as_view({
    'get': 'retrieve'
})




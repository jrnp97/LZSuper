from django.contrib.auth.models import User
from django.http import JsonResponse

from rest_framework.viewsets import ViewSet
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from robots.models import RSeoStatus, TaskRun
from robots.api.serializers import TaskResultSerializer, TaskResultStatusSerializer
from robots.api.permissions import IsOwnerOrReadOnly
from robots.tasks import show_message

from django_celery_results.models import TaskResult

robot_info = {
    "keyword": "pizzeta",
    "domain": "pizzeria.com",
    "google": True,
    "yahoo": True,
    "bing": True,
    "duckduck": True,
    "destination": "pruebadajngo@gmail.com"
}


class TaskResultViewSet(ViewSet):

    def list(self, request):
        results = TaskResult.objects.all()
        serializer = TaskResultSerializer(results,
                                          context={'request': request},
                                          many=True
                                          )
        return JsonResponse(serializer.data, safe=False)

    def retrieve(self, request, task_id):
        result = TaskResult.objects.get(task_id=task_id)
        print(result.result)
        serializer = TaskResultStatusSerializer(result, context={'request': request})
        return JsonResponse(serializer.data)


task_result_list = TaskResultViewSet.as_view(
    {'get': 'list'}
)

task_result_detail = TaskResultViewSet.as_view(
    {'get': 'retrieve'}
)


class TaskOptions(ViewSet):
    permission_classes = (IsOwnerOrReadOnly, )

    def create(self, request):
        message = request.data
        task = show_message.delay(msg=message)
        return Response({'task_id': task.task_id})

    def status(self, request, task_id=None):
        pass


create_task = TaskOptions.as_view(
    {'post': 'create'}
)

from rest_framework import serializers

from django_celery_results.models import TaskResult

from robots.models import TaskRun


class TaskResultSerializer(serializers.HyperlinkedModelSerializer):

    result = serializers.HyperlinkedIdentityField(view_name='robots:task_result_detail',
                                                  lookup_field='task_id',
                                                  lookup_url_kwarg='task_id'
                                                  )
    task_id = serializers.ReadOnlyField()

    class Meta:

        model = TaskResult
        fields = (
            'task_id',
            'status',
            'result',
            'date_done',
        )


class TaskResultStatusSerializer(serializers.ModelSerializer):
    task_id = serializers.ReadOnlyField()

    class Meta:
        model = TaskResult
        fields = (
            'task_id',
            'result',
            'meta',
        )


class TaskRunSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = TaskRun
        fields = (
            'id',
            'task_id',
            'state',
            'task_environment',
        )
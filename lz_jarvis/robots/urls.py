from django.conf.urls import url

from robots.views import (task_result_list, task_result_detail,
                          create_task, task_execution_list, task_execution_detail
                          )

app_name = 'robots'
urlpatterns = [
    url(r'^task/create/$', create_task, name='create_task'),
    url(r'^task/$', task_execution_list, name='task_execution_list'),
    url(r'^task/(?P<task_id>(\w+|[-]+)+)/$', task_execution_detail, name='task_execution_detail'),
    url(r'^tasks_done/$', task_result_list, name='task_result_list'),
    url(r'^tasks_done/(?P<task_id>(\w+|[-]+)+)/$', task_result_detail, name='task_result_detail'),
]


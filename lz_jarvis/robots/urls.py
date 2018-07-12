from django.conf.urls import url

from robots.views import (task_result_list, task_result_detail,
                          create_task,
                          )

app_name = 'robots'
urlpatterns = [
    url(r'^task/create/$', create_task),
    url(r'^tasks_done/$', task_result_list),
    url(r'^tasks_done/(?P<task_id>(\w+|[-]+)+)/$', task_result_detail, name='task_result_detail'),
]


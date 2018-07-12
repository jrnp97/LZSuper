from __future__ import absolute_import

import os
from celery import Celery
from celery.schedules import crontab



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lz_jarvis.settings')

app = Celery('lz_jarvis')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'reporte_usuario': {
#         'task': 'read_file.tasks.reporte_usuario',
#         'schedule': crontab(minute='*/1')
#     }
# }


@app.task(bind=True)
def test_task(self):
    print("Hola Mundo")

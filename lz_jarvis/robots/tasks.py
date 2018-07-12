from __future__ import absolute_import

import time

# from django.core.mail import EmailMessage
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError

from celery.worker.request import Request
from celery import current_app
from celery import Task

from robots.models import TaskRun

app = current_app


class CustomRequest(Request):

    def on_accepted(self, pid, time_accepted):
        super(CustomRequest, self).on_accepted(pid, time_accepted)
        # Task accept going to save on database
        TaskRun.objects.create(task_id=self.task_id).save()


class CustomTask(Task):

    Request = CustomRequest

    def update_state(self, task_id=None, state=None, meta=None):
        """Update task state.

        Arguments:
            task_id (str): Id of the task to update.
                Defaults to the id of the current task.
            state (str): New state.
            meta (Dict): State meta-data.
        """
        if task_id is None:
            task_id = self.request.id

        if state == 'STARTED' or state == 'PAUSED' or state == 'PENDING':
            try:
                task_db = TaskRun.objects.get(task_id=task_id)
                print(task_db)
                task_db.status = state
                task_db.save()
            except ObjectDoesNotExist:
                # If task don't exist on db will be create
                try:
                    TaskRun.objects.create(task_id=task_id, status=state).save()
                except IntegrityError:
                    # Unique Constraint Error (Some thread cloud be write on DB before) <To check>
                    pass
        else:
            print(task_id)

        self.backend.store_result(task_id, meta, state)

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        """Handltask_ider called after the task returns.

        Arguments:
            status (str): Current task state.
            retval (Any): Task return value/exception.
            task_id (str): Unique id of the task.
            args (Tuple): Original arguments for the task.
            kwargs (Dict): Original keyword arguments for the task.
            einfo (~billiard.einfo.ExceptionInfo): Exception information.

        Returns:
            None: The return value of this handler is ignored.
        """
        if status == 'PAUSED':
            pass  # Save robot serialized when is PAUSED
        else:  # Clean on TaskRun database task totally executed
            try:
                TaskRun.objects.get(task_id=task_id).delete()
                print(f"Task {task_id} deleted")
            except Exception as e:
                print(f"Task {task_id} isn't enable to delete, error {e}")

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        # Delete task from task running table
        try:
            TaskRun.objects.get(task_id=task_id).delete()
            print(f"Task {task_id} deleted")
        except Exception as e:
            print(f"Task {task_id} isn't enable to delete, error {e}")


@app.task(base=CustomTask, bind=True)
def show_message(self, *args, **kwargs):
    self.update_state(state='STARTED', meta={'msg': 'i\'m a pretty message'})
    message = kwargs.pop('msg', None)
    print(f"The worker received this {message}")
    time.sleep(10)
    return "By"


# @app.task
# def send_email():
#     e = EmailMessage()
#     e.subject = 'Reporte Usuarios'
#     e.to = ['<>', ]
#     e.from_email = '<>'
#     e.body = 'Anexo reporte en archivo xls'
#     e.send()
#
#     return 'Mensaje Enviado'

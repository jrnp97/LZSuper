from django.db import models


class RSeoStatus(models.Model):
    """ Model describing robot options and functionality """
    owner = models.ForeignKey('auth.User', related_name='rseostatus', on_delete=models.CASCADE)
    keyword = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    google = models.BooleanField(default=False)
    yahoo = models.BooleanField(default=False)
    bing = models.BooleanField(default=False)
    duckduck = models.BooleanField(default=False)
    destination = models.TextField(default='pruebadajngo@gmail.com')

    def __str__(self):
        return self.keyword


class TaskRun(models.Model):
    """ Model with only tasks on executing """
    TASK_STATE_CHOICES = (
        ('STARTED', 'started'),
        ('PENDING', 'pending'),
        # ('PAUSED', 'paused')
    )
    task_id = models.CharField(max_length=200, null=False, blank=False, editable=False)
    status = models.CharField(max_length=50, default='PENDING', choices=TASK_STATE_CHOICES)
    task_environment = models.TextField(null=True, blank=True, default=None)

from django.db import models


class RSeoStatus(models.Model):
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



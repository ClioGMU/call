from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
    )
    call_date = models.DateField(default=None)
    denomination = models.CharField(max_length=25, default=None)
    city = models.CharField(max_length=25, default=None)
    state = models.CharField(max_length=15, default=None)
    body = models.TextField()


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])
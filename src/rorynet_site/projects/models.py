from django.db import models
from django.utils import timezone

class Project(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True,
        null=True)
    source_code_link = models.CharField(max_length=200)
    id_string = models.CharField(max_length=50)
    picture = models.CharField(max_length=50)

    def publish(self):
        self.published_date = timezone.now
        self.save()

    def __str__(self):
        return self.title

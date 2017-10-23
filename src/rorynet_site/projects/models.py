from django.db import models
from datetime import datetime

class Project(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(
        default=datetime.now)
    published_date = models.DateTimeField(
        blank=True,
        null=True)
    source_code_link = models.CharField(max_length=200)
    id_string = models.CharField(max_length=50)

    def publish(self):
        self.published_date = datetime.now
        self.save()

    def __str__(self):
        return self.title

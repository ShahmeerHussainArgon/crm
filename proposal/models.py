from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=255)
    source_link = models.URLField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    client = models.CharField(max_length=255)

    def __str__(self):
        return self.title

from django.db import models


class Movie(models.Model):
    code = models.IntegerField(unique=True)
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

from django.db import models
import uuid

class Holder(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Work(models.Model):
    title = models.CharField(max_length=200)
    xref = models.UUIDField(default=uuid.uuid4, editable=False)
    holder = models.ManyToManyField(Holder, null=True)

    def __str__(self):
        return self.title
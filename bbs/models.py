from django.db import models
import uuid

class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.content
    
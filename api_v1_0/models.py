import uuid
from django.db import models


class Todo_v1_0(models.Model):
    id = models.IntegerField(primary_key=True)
    task_id = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=128, null=False)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

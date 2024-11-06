import uuid
from django.db import models

class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    building = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.city}, {self.street}, {self.building}"

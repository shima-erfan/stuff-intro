from django.db import models
import uuid

class Stuff(models.Model):
    name        = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default='default.png')
    id          = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    created     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created', 'name']

    


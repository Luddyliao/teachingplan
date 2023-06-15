from django.db import models

# Create your models here.
class Journal(models.Model):
    content = models.TextField("內容")
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content
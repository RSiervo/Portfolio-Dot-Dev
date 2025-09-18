from django.db import models

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="certificates/")
    date_received = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

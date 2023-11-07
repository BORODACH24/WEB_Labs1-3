from django.db import models


# Create your models here.
class Vacancy(models.Model):
    title = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    job_type = models.CharField(max_length=50)
    description = models.TextField()
    pass

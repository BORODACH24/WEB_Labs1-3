from django.db import models


# Create your models here.
class FAQ(models.Model):
    question = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    answer = models.TextField()
    pass

from django.db import models

# Create your models here.


class Feedback(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    stars = models.CharField(max_length=1)
    main_part = models.TextField()
    pass

from django.db import models


# Create your models here.
class Newsletter(models.Model):
    title = models.CharField(max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="news images/", null=True)
    summary = models.TextField()
    main_part = models.TextField()
    pass

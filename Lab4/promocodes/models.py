from django.db import models


# Create your models here.
class PromoCode(models.Model):
    promo_code = models.CharField(max_length=50)
    discount = models.DecimalField(max_digits=4, decimal_places=2)
    finish_date = models.DateTimeField()
    description = models.TextField()

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    pass

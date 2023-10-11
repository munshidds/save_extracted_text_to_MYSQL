
from django.db import models

class CustomerImage(models.Model):
    customer_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='customer_images/')
    upload_date = models.DateTimeField(auto_now_add=True)

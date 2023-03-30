from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    description = models.CharField(max_length=50)
    client_score = models.IntegerField(default=0)
    date_joined = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return self.first_name

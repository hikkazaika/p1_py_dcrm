from django.db import models

class Record(models.Model):
    create_at = models.DateTimeField(auto_now_add = True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

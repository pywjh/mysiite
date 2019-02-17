from django.db import models

# Create your models here.

class UserModule(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return 'UserModule<username=%s, password=%s, email=%s>'%(
            self.username, self.password, self.email
        )
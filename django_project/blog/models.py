from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    subject = models.CharField(max_length=100)
    section = models.CharField(max_length=60, choices=[("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),("6","6"),("7","7"),("8","8"),("9","9"),("10","10"),("To be Filled","To be Filled")], default="To be Filled")
    instructor = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

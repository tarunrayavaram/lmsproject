from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile,self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width >300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Extend(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length=60, choices=[("student","student"),("teacher","teacher")], default="student")

    def __str__(self):
        return f'{self.user.username} tag'

class StudentExtend(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    section = models.CharField(max_length=60, choices=[("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),("6","6"),("7","7"),("8","8"),("9","9"),("10","10"),("To be Filled","To be Filled")], default="To be Filled")

    def __str__(self):
        return f'{self.user.username} section'

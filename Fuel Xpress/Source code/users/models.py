from django.db import models
from django.contrib.auth.models import User
from PIL import Image

#It is o create profile model
class Fuelxpress_Profile(models.Model):
    FE_user = models.OneToOneField(User, on_delete=models.CASCADE)
    FE_image = models.ImageField(default='default.jpg', upload_to='profile_pics')
#To represent the string username
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        FE_img = Image.open(self.image.path)
#To check the size of image and resize it
        if FE_img.height > 300 or FE_img.width > 300:
            output_size = (300, 300)
            FE_img.thumbnail(output_size)
            FE_img.save(self.image.path)

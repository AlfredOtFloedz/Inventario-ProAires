from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
        
    staff = models.OneToOneField(User, on_delete=models.CASCADE)
    address =  models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    image = models.ImageField(default='avatar.jpg', upload_to='Profile_Images')
    
    class Meta:
        verbose_name_plural = 'Perfiles'
    
    def _str_(self):
        return f'{self.staff.username}-Profile'
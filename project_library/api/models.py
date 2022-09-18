from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    USER_ROLE=(
        ('LIBRARIAN','LIBRARIAN'),
        ('MEMBER','MEMBER'),
    )
    user=models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    role=models.CharField(max_length=10,choices=USER_ROLE)


class BookModel(models.Model):
    book_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    book_number = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
 
    def __str__(self):
        return str(self.name) + " ["+str(self.book_number)+']'

from django.contrib.auth.models import User
from django.db import models

from books.choices import User_Type
from books.models import Borrowing


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    borrowed_books = models.ManyToManyField(Borrowing, null=True, blank=True)
    user_type = models.PositiveIntegerField(choices=User_Type.USER_TYPE_CHOICES, default=User_Type.ANONYMOUS)

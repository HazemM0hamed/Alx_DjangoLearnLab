from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Ensure this is unique
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Ensure this is unique
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser',
    )
    objects = CustomUserManager()
    def __str__(self):
        return self.username
    

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    class Meta:
        permission = [
                ("can_view", "Can view book"),
                ("can_create", "Can create book"),
                ("can_edit", "Can edit book"),
                ("can_delete", "Can delete book"),
        ]


    def __str__(self):
        return self.title

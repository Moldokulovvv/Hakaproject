from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

# User = get_user_model()

class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='users')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.get_full_name()



# class UserManager(BaseUserManager):
#     def _create_user(self,email,password, **extra_fields):
#         if not email:
#             raise ValueError('Email is required')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create(self, email,password, **extra_fields):
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email,password, **extra_fields)
#
#     def create_superuser(self,email, password, **extra_fields):
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active',True)
#         extra_fields.setdefault('is_staff', True)
#         if extra_fields.get('is_superuser') is False:
#             raise ValueError('Super user must have is_superuser=True')
#         return self._create_user(email,password,**extra_fields)


# class User(AbstractBaseUser):
#     email = models.EmailField(max_length=100, primary_key=True)
#     is_active = models.BooleanField(default=False)
#     name = models.CharField(max_length=100, blank=True)
#     last_name = models.CharField(max_length=100, blank=True)
#     is_superuser = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     activation_code = models.CharField(max_length=15, blank=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     objects = UserManager()
#
#     def has_perm(self, obj=None):
#         return self.is_superuser
#
#     def has_module_perms(self, app_label):
#         return self.is_staff
#
#     def create_activation_code(self):
#         from django.utils.crypto import get_random_string
#         code = get_random_string(15)
#         if User.objects.filter(activation_code=code).exists():
#             self.create_activation_code()
#         self.activation_code = code
#         self.save(update_fields=['activation_code'])
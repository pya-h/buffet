import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    # simple validation method for skipping non-correct data
    # also there is extra validations in forms.py section
    def validate_credentials(self, username, contact, password):
        if not username:
            raise ValueError('Username field is essential')
        if not password:  # and can add some other properties
            raise ValueError('Password is empty')
        if not contact:
            raise ValueError('Email or Phone number is essential')

    # this method is called when the account goes to 'auth.html' in the register tab and clicks on sign up
    def create_user(self, username, contact, password, is_staff=False):
        self.validate_credentials(username, contact, password)
        u = self.model(username=username, contact=self.normalize_email(contact))
        u.set_password(password)
        u.is_staff = is_staff
        u.is_active = u.is_superuser = False
        u.save(using=self._db)
        return u

    # this method is for superusers
    # run command below to create a superuser for you are site, so you can log in the admin panel
    # python manage.py createsuperuser
    def create_superuser(self, username, contact, password):
        self.validate_credentials(username, contact, password)
        su = self.model(username=username, contact=self.normalize_email(contact))
        su.set_password(password)
        su.is_active = su.is_staff = su.is_superuser = True
        su.save(using=self._db)
        return su


# our custom account model with custom fields and on
class Account(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # id auto generated by uuid
    
    username = models.CharField(max_length=20, unique=True)  # id determined by account
    
    # login field is phone number or email
    contact = models.CharField(max_length=50, unique=True)  # phone number or email

    # requirements:
    joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)  # if ypu are a staff member then u can access admin page too
    is_active = models.BooleanField(default=False)  # if you are an active and busy member of the site
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['contact']  # contact means email or phone number
    objects = UserManager()

    # this is for admin users
    # this two method below, gives permission to appropriate users
    # to sign in into admin panel in 'localhost:8000/admin' or '127.0.0.1:8000/admin'
    def has_perm(self, perm, obj=None):
        return self.is_active and self.is_staff

    def has_module_perms(self, perm, obj=None):
        return self.is_superuser and self.is_active and self.is_staff

    # this will return the string value of a account object which is its username
    def __str__(self) -> str:
        return self.username

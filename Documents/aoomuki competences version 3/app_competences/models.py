from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import (BaseUserManager, AbstractBaseUser)
from django.contrib.auth.models import UserManager

class Society(models.Model):
    name = models.CharField('Société', max_length=200, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Société"

class ListWorkStation(models.Model):
    name = models.CharField('nom', max_length=50, unique=True)
    commentary = models.CharField('commentaire', max_length=250, unique=False)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Liste postes de travail"
        
class Certification(models.Model):
    name = models.CharField('nom', max_length=200, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Certification"

class Field(models.Model):
    name = models.CharField('nom', max_length=200, unique=True)
    description = models.CharField('description', max_length=250, unique=False)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Domaine"

class Competence(models.Model):
    name = models.CharField('nom', max_length=50, unique=False)
    commentary = models.CharField('commentaire', max_length=250, unique=False)
    field = models.ForeignKey(Field,on_delete=models.CASCADE, null=True, default=1)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Compétence"

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(verbose_name='Adresse mail', max_length=255, unique=True)
    username = models.CharField(verbose_name='Nom d\'utilisateur',max_length=50, null=True, blank=True)
    last_name = models.CharField(verbose_name=' Nom',max_length=50)
    first_name = models.CharField(verbose_name='Prénom',max_length=50)
    is_active = models.BooleanField(verbose_name='Adresse mail',default=True)
    is_staff = models.BooleanField(verbose_name='Equipe ?',default=False)
    is_superuser = models.BooleanField(verbose_name='Superuser ?',default=False)
    is_collaborater = models.BooleanField(verbose_name='Collaborateur ?',default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    workstation = models.ForeignKey(ListWorkStation,on_delete=models.CASCADE,verbose_name='Poste', null=True)
    society = models.ForeignKey(Society,on_delete=models.CASCADE,verbose_name='Société', null=True)
    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','last_name', 'first_name'] # Email & Password are required by default.

    objects = UserManager() 

    # def get_full_name(self):
    #     # The user is identified by their email address
    #     return self.email

    # def get_short_name(self):
    #     # The user is identified by their email address
    #     return self.email

    # def __str__(self):
    #     return self.email

    # def has_perm(self, perm, obj=None):
    #     "L'utilisateur dispose-t-il d'une autorisation spécifique?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # def has_module_perms(self, app_label):
    #     "L'utilisateur a-t-il les autorisations pour afficher l'application `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # @property
    # def is_staff(self):
    #     "L'utilisateur est-il membre du personnel?"
    #     return self.is_staff

    # @property
    # def is_admin(self):
    #     "L'utilisateur est-il un membre administrateur?"
    #     return self.is_admin

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


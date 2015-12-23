"""
Definition of models.
"""
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class Doctor(models.Model):
	nom = models.CharField(max_length=150)
	specialite = models.CharField(max_length=50)
	adresse = models.TextField(null=True)
	email = models.EmailField(max_length=254)
	phone_number1 = models.CharField(max_length=16)
	anecdote = models.TextField(null=True)
	country = models.CharField(max_length=50)

class Hospital(models.Model):
	nom = models.CharField(max_length=200)
	quartier = models.CharField(max_length=75)
	adresse = models.TextField(null=True)
	email = models.EmailField(max_length=254)
	phone_number1 = models.CharField(max_length=16)
	phone_number2 = models.CharField(max_length=16)
	specialite = models.CharField(max_length=50)

class MyUserManager(BaseUserManager):
    def create_user(self, name=None, email=None, password=None):
        """
        Creates and saves a User with the given name, email, country, specialite and password.
        """
        if not name:
        	raise ValueError('Must include name')

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
        	name = name,
            email = self.normalize_email(email),
			country = country,
			specialite = specialite,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email,  password):
        """
        Creates and saves a superuser with the given username, email and password.
        """

        user = self.create_user(
			name=name,
			email=email,
            password=password,
			country=country,
			specialite=specialite,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyDoctor(AbstractBaseUser):
	name = models.CharField(max_length=255, unique=True,)
	email = models.EmailField(verbose_name='email address', max_length=255, unique=True,)
	country = models.CharField(max_length=255,)
	specialite = models.CharField(max_length=255,)
	owner_first_name = models.CharField(max_length=120,)
	owner_last_name = models.CharField(max_length=120,)
	is_member = models.BooleanField(default=False, verbose_name='Is Paid Member')
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = MyUserManager()

	USERNAME_FIELD = 'name'
	REQUIRED_FIELDS = ['email', 'country', 'specialite']

	def get_full_name(self):
	    # The user is identified by their email address
	    return "%s %s" %(self.owner_first_name, self.owner_last_name)

	def get_short_name(self):
	    # The user is identified by their email address
	    return self.owner_first_name

	def __str__(self):
	    return self.name

	def get_country(self):
		return self.country

	def get_specialite(self):
		return self.specialite

	def has_perm(self, perm, obj=None):
	    "Does the user have a specific permission?"
	    # Simplest possible answer: Yes, always
	    return True

	def has_module_perms(self, app_label):
	    "Does the user have permissions to view the app `app_label`?"
	    # Simplest possible answer: Yes, always
	    return True

	@property
	def is_staff(self):
	    "Is the user a member of staff?"
	    # Simplest possible answer: All admins are staff
	    return self.is_admin

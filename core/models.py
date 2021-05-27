from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
DEPARTMENT_CHOICE = (
    ('HR','HR'),
    ('Infrastructures','Infrastructures'),
    ('IT services','IT services')
)
DESIGNATION_CHOICE = (
    ('Javascript Developer','Javascript Developer'),
    ('Python Developer','Python Developer'),
    ('PHP Developer','PHP Developer')
)
GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)
class Employee(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    department = models.CharField(choices=DEPARTMENT_CHOICE,max_length=250)
    designation = models.CharField(choices=DESIGNATION_CHOICE,max_length=250)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=50)
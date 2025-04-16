from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from datetime import date

class UserProfile(models.Model):
    GENDER_CHOICES = {
        "M" : "male",
        "F" : "female",
    }
    HOBBIES_CHOICES = {
        "S" : "sports",
        "M" : "music",
        "T" : "travel",
    }
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    gender = models.CharField("gender", choices = GENDER_CHOICES)
    birth_date = models.DateField("birth date")
    country = CountryField("ucountry")
    profile_picture = models.ImageField("profile picture", upload_to = 'media')
    hobbies = MultiSelectField("hobbies", choices = HOBBIES_CHOICES)
    mobile_number = PhoneNumberField("mobile number", unique = True)
    
    def __str__(self):
        return f"{self.user}"
    
    def get_age(self):
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))

    
    class Meta:
        db_table = 'user_profile'

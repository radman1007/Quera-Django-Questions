from django.db import models
import jdatetime


class CustomUser(models.Model):
    GENDER_BOX = {
        'M' : 'Male',
        'F' : 'Female',
    }
    username = models.CharField(max_length=256)
    fullname = models.CharField(max_length=256)
    gender = models.CharField(max_length=1, choices=GENDER_BOX)
    national_code = models.CharField(max_length=10)
    # birthday_date = 
    # ceremony_datetime = 
    country = models.CharField(max_length=256 ,default="Iran")

    def __str__(self):
        return self.username

    def get_first_and_last_name(self):
        fullname = self.fullname.split(' ')
        if len(fullname) == 2:
            first_name, last_name = fullname
            return {'first_name' : first_name, 'last_name':last_name}
        else:
            return False

    def is_birthday(self):
        if self.birthday_date == jdatetime.date.today():
            return True
        else:
            return False
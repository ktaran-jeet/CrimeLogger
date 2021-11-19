from django.db import models


class Criminal(models.Model):
    photo = models.ImageField(upload_to='images/',blank= True);
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250 , blank = True)       #blank=true::optional
    wanted_level = models.TextField(blank=True)
    nick_name = models.CharField(max_length=250 , blank = True)
    obligations = models.TextField( blank= True)
    crime_areas = models.TextField(blank =True)
    prize_money = models.TextField(null=True , default = "0")
    number_of_times_tapped = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.first_name;

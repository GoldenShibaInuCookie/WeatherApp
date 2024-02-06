from django.db import models

class Location(models.Model):
    Country = models.CharField(max_length = 2) # A country code with two letters#
    County = models.CharField(max_length = 30) # The name of the county
    Town = models.CharField(max_length = 50) # The name of the town
    
class Weather(models.Model):
    CurrentTemperature = models.IntegerField() # Current temperature in Celcius
    WeatherType = models.CharField(max_length = 20) # Type of weather (E.g Storm, foggy, etc.)
    Humidity = models.IntegerField() # Current humidity
    Precipitation = models.IntegerField # Current precipitation in mm
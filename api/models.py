from django.db import models


# Create your models here.

class VoterRecord(models.Model):
    identity_number = models.CharField(max_length=15, unique=True,primary_key=True)
    block_code = models.CharField(max_length=200)
    polling_station = models.CharField(max_length=200)
    polling_booth = models.CharField(max_length=200)

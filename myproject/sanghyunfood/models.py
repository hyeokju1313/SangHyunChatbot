from django.db import models

class Menu(models.Model):
        id = models.AutoField(primary_key=True)
        menu = models.CharField(max_length=100, default="")

from django.db import models

class Statistika(models.Model):
    umumiy_foyda = models.IntegerField(blank=True,null=True)
    bugungi_savdo = models.IntegerField(blank=True,null=True)
    bugungi_foyda = models.IntegerField(blank=True,null=True)
    bugungi_zarar = models.IntegerField(blank=True,null=True)
    soni = models.SmallIntegerField(blank=True,null=True)
    def __str__(self):
        return self.umumiy_foyda

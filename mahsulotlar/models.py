from django.db import models

class Mahsulot(models.Model):
    nomi = models.CharField(max_length=69)
    firma_nomi = models.CharField(max_length=69,blank=True,null=True)
    kel_narxi = models.IntegerField(blank=True,null=True)
    sot_narxi = models.IntegerField(blank=True,null=True)
    optm_narxi = models.IntegerField(blank=True,null=True)
    kel_soni = models.SmallIntegerField(blank=True,null=True)
    foyda = models.IntegerField(blank=True,null=True)
    zarar = models.IntegerField(blank=True,null=True)
    qoldiq = models.SmallIntegerField(blank=True,null=True)
    kilosi = models.SmallIntegerField(blank=True,null=True)
    blogi = models.CharField(max_length=15,blank=True,null=True)
    def __str__(self):
        return f"{self.nomi}({self.firma_nomi})"

class Nasiya(models.Model):
    tovar_nomi = models.CharField(max_length=69)
    summasi = models.IntegerField(blank=True,null=True)
    dokon_nomi = models.CharField(max_length=69,null=True,blank=True)
    xodim_ismi = models.CharField(max_length=25)
    def __str__(self):
        return f"{self.tovar_nomi}({self.dokon_nomi})"
from pyexpat import model
from django.db import models

class transaksi(models.Model):
    Image = models.ImageField(upload_to='static/image', blank= True, null= True)
    Uraian = models.CharField(max_length=225,default="")
    Tanggal_Transaksi= models.DateField()
    Status = models.CharField(max_length=100, default="")
    Nominal = models.DecimalField(max_digits=10, decimal_places=2, default=0)


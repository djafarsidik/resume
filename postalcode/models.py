from django.db import models

# Create your models here.

class Provinsi(models.Model):
    code = models.CharField(max_length=2)
    nama = models.CharField(max_length=200)

    def __str__(self):
        return self.nama
        
class Kab_kota(models.Model):
    code = models.CharField(max_length=5)
    nama = models.CharField(max_length=200)
    type = models.CharField(max_length=10, choices=(
        ("kabupaten", "Kabuputen"),
        ("kota", "Kota")
    ))
    provinsi = models.ForeignKey(Provinsi, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nama
from django.db import models

JINS=[
    ('erkak','erkak'),
    ('ayol','ayol'),
]
DARAJA=[
    ('Bakalavir','Bakalavir'),
    ('Magistir','Magistir'),
    ('Academik','Academik'),
    ('Fan Doctori','Fan Doctori'),
]
class Yonalish(models.Model):
    nom=models.CharField(max_length=200)
    aktiv=models.BooleanField()
    def __str__(self):
        return self.nom

class Fan(models.Model):
    nom=models.CharField(max_length=200)
    yonalish=models.ForeignKey(Yonalish,on_delete=models.CASCADE)
    asosi=models.BooleanField(max_length=200)
    def __str__(self):
        return self.nom

class Ustoz(models.Model):
    ism=models.CharField(max_length=50)
    jins=models.CharField(max_length=30,choices=JINS)
    yosh=models.PositiveIntegerField()
    daraja=models.CharField(max_length=30,choices=DARAJA)
    fan=models.ForeignKey(Fan,on_delete=models.CASCADE)
    def __str__(self):
        return self.ism


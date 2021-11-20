from django.db import models

# Create your models here.

class Muallif(models.Model):
    nomi = models.CharField(max_length=200)
    reyting = models.IntegerField()

    def __str__(self) -> str:
        return self.nomi

class Kitob(models.Model):
    nomi = models.CharField(max_length=100)
    betlar_soni = models.IntegerField()
    muallif = models.ForeignKey(Muallif, related_name="kitoblar", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nomi

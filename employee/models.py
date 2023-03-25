from django.db import models


class Employee(models.Model):
    eid = models.CharField(max_length=20)
    etype = models.CharField(max_length=25)
    eprice = models.CharField(max_length=100)
    ecsell = models.CharField(max_length=50)
    etypeiden = models.CharField(max_length=10)
    eperson = models.CharField(max_length=10)

    def __str__(self):
        return "%s" % (self.etype)

    class Meta:
        db_table = "employee"

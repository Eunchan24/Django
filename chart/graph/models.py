from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    population = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Covid(models.Model):
    accDefRate     =        models.FloatField(max_length=15, db_column='accDefRate', blank=True, null=True)
    accExamCnt     =        models.IntegerField(max_length=4,  db_column='accExamCnt', blank=True, null=True)
    accExamCompCnt =        models.IntegerField(max_length=4,db_column='accExamCompCnt', blank=True, null=True)
    careCnt        =        models.IntegerField(max_length=4,db_column='careCnt', blank=True, null=True)
    clearCnt       =        models.IntegerField(max_length=4, db_column='clearCnt', blank=True, null=True)
    createDt       =        models.DateTimeField(db_column='createDt', blank=True, null=True)
    deathCnt       =        models.IntegerField(max_length=4, db_column='deathCnt', blank=True, null=True)
    decideCnt      =        models.IntegerField(max_length=4, db_column='decideCnt', blank=True, null=True)
    examCnt        =        models.IntegerField(max_length=4, db_column='examCnt', blank=True, null=True)
    resutlNegCnt   =        models.IntegerField(max_length=4, db_column='resutlNegCnt', blank=True, null=True)
    seq            =        models.IntegerField(max_length=4, db_column='seq', blank=True, null=True)
    stateDt        =        models.DateField(db_column='stateDt', blank=True, null=True)
    stateTime      =        models.TimeField(db_column='stateTime', blank=True, null=True)
    updateDt       =        models.DateTimeField(db_column='updateDt', blank=True, null=True)



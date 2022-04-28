from django.db import models


# Create your models here.
class Detail(models.Model):
    SEX = (
        (0, 'Female'),
        (1, 'Male')
    )
    CP = (
        (0, 'typical angina'),
        (1, 'atypical angina'),
        (2, 'non-anginal pain'),
        (3, 'asymptomatic')
    )
    RESTECG = (
        (0, 'Normal'),
        (1, 'ST-T wave abnormality'),
        (2, 'Left ventricular hypertrophy')
    )
    EXANG = (
        (0, 'No'),
        (1, 'Yes')
    )
    SLOPE = (
        (0, 'Upsloping'),
        (1, 'Flat'),
        (2, 'Downsloping')
    )
    THAL = (
        (3, 'Normal'),
        (6, 'Fixed defect'),
        (7, 'Reversable defect')
    )
    TARGET = (
        (1, 'No'),
        (2, 'Yes')
    )
    FBS = (
        (0, 'False'),
        (1, 'True')
    )
    EXANG = (
        (0, 'No'),
        (1, 'Yes')
    )
    age = models.IntegerField()
    sex = models.IntegerField(choices=SEX)
    cp = models.IntegerField(choices=CP)
    trestbps = models.IntegerField()
    chol = models.IntegerField()
    fbs = models.IntegerField(choices=FBS)
    restecg = models.IntegerField(choices=RESTECG)
    thalach = models.IntegerField()
    exang = models.IntegerField(choices=EXANG)
    oldpeak = models.IntegerField()
    slope = models.IntegerField(choices=SLOPE)
    ca = models.IntegerField()
    thal = models.IntegerField(choices=THAL)
    target = models.IntegerField(choices=TARGET)
    pos = models.FloatField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

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
    cp = models.IntegerField(choices=CP, verbose_name='Chest Pain Type')
    trestbps = models.IntegerField(verbose_name='Resting Blood Pressure (mmHg)')
    chol = models.IntegerField(verbose_name='Serum Cholestoral (mg/dl)')
    fbs = models.IntegerField(choices=FBS, verbose_name='Fasting Blood Sugar > 120 mg/dl')
    restecg = models.IntegerField(choices=RESTECG, verbose_name='Resting Electrocardiographic Results')
    thalach = models.IntegerField(verbose_name='Maximum Heart Rate')
    exang = models.IntegerField(choices=EXANG, verbose_name='Exercise Induced Angina')
    oldpeak = models.IntegerField(verbose_name='ST Depression (mmHg)')
    slope = models.IntegerField(choices=SLOPE, verbose_name='Slope of Peak Exercise ST Segment')
    ca = models.IntegerField(verbose_name='Number of Vessels Colored by Flourosopy')
    thal = models.IntegerField(choices=THAL, verbose_name='Thalassemia')
    target = models.IntegerField(choices=TARGET)
    pos = models.FloatField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

from django.db import models

class TeachingPlan(models.Model):
    seme = models.TextField('學期')
    cclass = models.TextField('班級')
    ffile = models.FileField('教學計劃')
    subject = models.TextField('科目')
    teacher = models.ForeignKey(User, models.CASCADE)
    created = models.DateField(auto_now_add=True)

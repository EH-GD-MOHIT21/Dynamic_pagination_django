from django.db import models

# Create your models here.

class paginationdata(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='imgs')

class generalpagination(models.Model):
    date = models.DateField()
    extra = models.ForeignKey(paginationdata,on_delete=models.CASCADE)
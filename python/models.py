from django.db import models

# Create your models here.

#class StudentRegister(models.Model):


class StudentRegister(models.Model):
    
    name=models.CharField(max_length=30)

    email=models.EmailField(blank=False,unique=True)

    password=models.CharField(max_length=50)
    
    college=models.CharField(max_length=50)

    sid=models.CharField(max_length=30)

    qualification=models.CharField(max_length=50)

    location=models.CharField(max_length=40)

    sex=models.CharField(max_length=40)

    image=models.CharField(max_length=100)

    def __str__(self):

        return self.name


class EmployeeRegister(models.Model):
    
    name=models.CharField(max_length=30)

    email=models.EmailField(blank=False,unique=True)

    password=models.CharField(max_length=50)
    
    college=models.CharField(max_length=50)

    eid=models.CharField(max_length=30)

    designation=models.CharField(max_length=50)

    qualification=models.CharField(max_length=50)

    location=models.CharField(max_length=40)

    cfee=models.CharField(max_length=30,default=0)

    sex=models.CharField(max_length=40)

    image=models.CharField(max_length=100)

    def __str__(self):

        return self.name


class ChartInformation(models.Model):

    sid=models.CharField(max_length=30)
    
    
    eid=models.CharField(max_length=30)


    message=models.CharField(max_length=500)


    reply=models.CharField(max_length=500)

    today=models.DateField()



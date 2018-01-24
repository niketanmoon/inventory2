from django.db import models
os_choices=(
	('window','Windows'),
	('linux','Linux'),
	)
# Create your models here.
class Computer(models.Model):
	ip_address=models.GenericIPAddressField(unique=True)
	SerialKey = models.CharField(max_length=120,null=True, unique=True)
	HostName = models.CharField(max_length=120,unique=True)
	BrandName = models.CharField(max_length=120)
	OsName = models.CharField(max_length=120,choices=os_choices,default='Windows')
	OsVersion = models.IntegerField(default=7)
	Processor = models.CharField(max_length= 200)
	Ram = models.CharField(max_length=50,default='64 GB')
	ExternalStorage = models.CharField(max_length=50, default='1 TB')
	Location = models.CharField(max_length = 120, default='Pune')
	
	def __str__(self):
		return self.ip_address

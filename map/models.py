from django.db import models

class Citizen(models.Model):

	citizenID = models.CharField(max_length=200)
	rec_date = models.DateTimeField('date recieved')
	
	def __str__(self):
		return self.citizenID
	


class Location(models.Model):

	citizen = models.ForeignKey(Citizen)
	latitude = models.DecimalField(max_digits=10,decimal_places=8)
	longitude = models.DecimalField(max_digits=10,decimal_places=8)
	
	def __str__(self):
		return str(self.citizen)+', '+str(self.latitude)+', '+str(self.latitude)

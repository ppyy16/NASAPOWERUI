from django.db import models

# Create your models here.
#MODELS> definitive source of information about your data


#things that you want to render
class dummy(models.Model):
	name = models.CharField(max_length=20)
	status = models.CharField(max_length=20, default='Unknown')

	class Meta:
		db_table = 'info'
	
	def __str__(self):
		return self.name

from django.db import models

class People(models.Model):
	full_name = models.CharField(max_length=100)
	code = models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)
	second_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	short_name = models.CharField(max_length=100)
	
	def __str__(self):
		return self.full_name

class Store(models.Model):
	description = models.CharField(max_length=100)
	code = models.CharField(max_length=100)
	
	def __str__(self):
 		return self.description
 		

class Check(models.Model):
	description = models.CharField(max_length=100)
	code = models.CharField(max_length=100)
	name_number = models.CharField(max_length=100)
	
	def __str__(self):
 		return self.description

class Currensy(models.Model):
	nominal_value = models.IntegerField()	


class Sales(models.Model):
	#date = models.DateTimeField(default=datetime.now,blank=True)
	date_auto = models.DateTimeField(auto_now_add=True, blank=True)

	store = models.ForeignKey(Store, on_delete=models.CASCADE)
	people = models.ForeignKey(People, on_delete=models.CASCADE)
	check_name = models.ForeignKey(Check, on_delete=models.CASCADE)
	currensy = models.ForeignKey(Currensy, on_delete=models.CASCADE)

	Z_report_501 = models.DecimalField(max_digits=5, decimal_places=2)
	Z_report_502 = models.DecimalField(max_digits=5, decimal_places=2)
	cashless = models.DecimalField(max_digits=5, decimal_places=2)
	cash_day_start = models.DecimalField(max_digits=5, decimal_places=2)
	cash_day_end = models.DecimalField(max_digits=5, decimal_places=2)
	cost = models.CharField(max_length=200)
	sum_cost = models.DecimalField(max_digits=5, decimal_places=2)
	count_currensy = models.IntegerField(default=0)	
	sum_Z_report = models.DecimalField(max_digits=5, decimal_places=2)
	sum_check = models.DecimalField(max_digits=5, decimal_places=2)

	def save(self, *args, **kwargs):
		self.sum_Z_report = self.Z_report_501 + self.Z_report_502
		self.sum_check = self.Z_report_501 + self.Z_report_502 - self.cashless



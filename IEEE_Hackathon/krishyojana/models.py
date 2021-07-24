from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
	crop_name = models.CharField(max_length=100)
	harvest_time = models.CharField(max_length=100)
	rate = models.FloatField()
	amount_left = models.FloatField()
	date_posted = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='emarket')
	add_to_cart = models.ManyToManyField(User, related_name='add_to_cart', default=None, blank=True)

	def __str__(self):
		return self.crop_name

	def get_absolute_url(self):
		return reverse('krish-emarket')

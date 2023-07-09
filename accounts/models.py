from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class CustomUser(AbstractUser):
	id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	mobile_number=models.CharField(max_length=25)
	birth_date=models.DateField(null=True, blank=True)
	gender_choices=(
		('N', 'NONE'),
		('F', 'FEMALE'),
		('M', 'MALE'),
		)
	gender=models.CharField(max_length=10, choices=gender_choices, default="N")

	def get_absolute_url(self):
		return reverse("user_detail", args=[str(self.id)])
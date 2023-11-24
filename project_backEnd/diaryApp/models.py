from django.db import models
from datetime import datetime

class Daily_diary1(models.Model):
	diary_created_date = models.DateField(default=datetime.now, blank=True)
	diary_updated_date = models.DateField(auto_now=True)
	diary_title = models.CharField(max_length=50)
	diary_contents = models.CharField(max_length=500)



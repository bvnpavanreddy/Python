from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Question(models.Model):
	title = models.TextField()
	status = models.CharField(default='inactive', max_length=20)
	created_by = models.ForeignKey(User,null=True,blank=True,on_delete='CASCADE')

	start_date=models.DateTimeField(null=True,blank=True)
	end_date=models.DateTimeField(null=True,blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title


class Choice(models.Model):
	question=models.ForeignKey('polls.Question',on_delete='CASCADE')
	text=models.TextField(null=True,blank=True)


	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return text

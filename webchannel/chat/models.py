from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
	author = models.ForeignKey(User, related_name='author_message', on_delete=models.CASCADE, blank= True, null=True)
	content = models.TextField(blank= True, null=True) 
	timestamp = models.DateTimeField(auto_now_add=True, blank= True, null=True)

	def __str__(self):
		return self.author.username

	def last_10_message(self):
		return Message.objects.order_by('-timestamp').all()[:10]

	

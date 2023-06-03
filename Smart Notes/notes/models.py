from django.db import models
from django.contrib.auth.models import User
class Notes(models.Model):
    #title for the notes 
    title=models.CharField(max_length=200)
    #notes 
    text=models.TextField()
    #when this note is created(time)
    created=models.DateTimeField(auto_now_add=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE,related_name="notes")



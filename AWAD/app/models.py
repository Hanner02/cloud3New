"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
    

class LogMessage(models.Model):
    title=models.CharField(max_length=100)
    message=models.TextField()
    log_date=models.DateTimeField()
    rating = models.IntegerField(default=0)
    def to_dict(self):
        return{'id':self.id,'title':self.title,'message':self.message, 'rating':self.rating}   
    def __str__(self):
        return "id:"+str(self.id)+", title:"+self.title+", message:"+self.message+", rating:"+str(self.rating)
    

class Film(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(max_length=200, blank=True, null=True)
    def __str__(self):
        return "title:"+self.title+", description:"+self.description+self.image_url
    

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'film')  # Prevent duplicate entries

    def __str__(self):
        return f"{self.user.username}'s watchlist"

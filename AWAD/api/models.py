from django.db import models

class ReviewItem(models.Model):
    title=models.CharField(max_length=100)
    message=models.TextField()
    log_date=models.DateTimeField()
    rating = models.IntegerField(default=0)
    
    

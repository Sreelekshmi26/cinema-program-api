from django.db import models

# Create your models here.
class Movies(models.Model):
    STATUS_TYPE_CHOICES = (
        ("coming-up", "Coming Up"),
        ("starting", "Starting"),
        ("running", "Running"),
        ("finished", "Finished"),
    )
    name = models.CharField(max_length=60, blank=True, null=True)
    protagonists = models.CharField(max_length=60, blank=True, null=True)
    poster  = models.URLField(max_length=200, blank=True, null=True)
    trailer  = models.URLField(max_length=200, blank=True, null=True)
    start_date = models.DateField()
    status = models.CharField(
        max_length=60, choices=STATUS_TYPE_CHOICES, default="user"
    )
    rank = models.IntegerField() 
    
    def __str__(self):
        return self.name
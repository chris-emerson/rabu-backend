from django.db import models

class Activity(models.Model):
    """A django model representing an Activity"""
    full_description = models.TextField(null=False, blank=True)
    description = models.CharField(max_length=255, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=255, null=True, blank=False)
    objects = models.Manager()
    
    def __str__(self):
        return str(self.description)
    
    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'
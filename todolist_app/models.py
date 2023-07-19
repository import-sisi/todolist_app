from django.db import models
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    priority = models.IntegerField(default=1)
    due_date = models.DateField('Updated', auto_now=True)
    completed = models.BooleanField(default=False)
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField('Created', auto_now_add=True)
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.title



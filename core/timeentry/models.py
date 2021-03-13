from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):

    PROJECT_CHOICES = (
    ('web-app','WEB APP'),
    ('mobile-app', 'MOBILE APP'),
    ('machine-learning','MACHINE LEARNING'),
    ('ai','AI'),
    ('deep-learning','DEEP LEARNING'),
)

    name = models.CharField(max_length=150)
    project = models.CharField( max_length=20, choices=PROJECT_CHOICES,default="web-app")
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False,null=False)
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False,null=False)
    start = models.DateTimeField(auto_now=False, auto_now_add=False,null=True)
    finish = models.DateTimeField(auto_now=False, auto_now_add=False,null=True)
    created_at = models.DateTimeField(auto_now = True)
    

    class Meta:
       db_table = "Task"

    def __str__(self):
        return self.name

    @classmethod
    def get_projects(cls):
        return set(cls.PROJECT_CHOICES)
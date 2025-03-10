from django.db import models



class Status (models.Model):
    status_choices = [
        ('important','important'),
        ('not important','not important'),
        ('not sure','not sure')
    ]
    status_id = models.AutoField(primary_key=True)
    status_input = models.CharField(max_length=120,choices=status_choices,default='not sure')

    def __str__(self):
        return self.status_input



class Todo(models.Model):
    title = models.CharField(max_length=120)
    status = models.ForeignKey(Status,on_delete=models.CASCADE , null=True, blank=True)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

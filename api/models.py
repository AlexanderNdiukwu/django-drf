from django.db import models





class Folder (models.Model):
    folder_id = models.AutoField(primary_key=True)
    folder_name = models.CharField(max_length=600)
    folder_description = models.TextField(max_length=600)
    folder_created_at = models.DateTimeField(auto_now_add=True)
    folder_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self ):
        return self.folder_name



class Status (models.Model):
    status_choices = [
        ('important','important'),
        ('not important','not important'),
        ('not sure','not sure')
    ]
    status_id = models.AutoField(primary_key=True)
    status_input = models.CharField(max_length=600,choices=status_choices,default='not sure')

    def __str__(self):
        return self.status_input
    
class Variation(models.Model):
    variation_id = models.AutoField(primary_key=True)
    variation_value = models.CharField(max_length=15)

class Variation_value_input(models.Model):
    variation_value_id = models.AutoField(primary_key=True)
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE,blank=True , null=True,related_name="variation_name")
    variation_value_value = models.CharField(max_length=15)




class Todo(models.Model):
    title = models.CharField(max_length=200)
    folder = models.ForeignKey(Folder,on_delete=models.CASCADE, blank=True , null=True  )
    variation_value_input = models.ManyToManyField(Variation_value_input,blank=True , related_name='v_input')
    status = models.ForeignKey(Status,on_delete=models.CASCADE, blank=True , null=True )
    description = models.TextField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

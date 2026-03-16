from django.db import models
class userreg(models.Model):
    username=models.CharField(max_length=70)
    email = models.CharField(max_length=100, null=True, blank=True)
    password=models.CharField(max_length=100)

    def __str__(self):
     return self.username
    

class Task(models.Model):
    user = models.ForeignKey(userreg, on_delete=models.CASCADE)   # ⭐ important
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    

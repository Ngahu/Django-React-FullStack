from django.db import models

# Create your models here.




class Lead(models.Model):
    """
    Description:Contains a single lead.\n
    """
    name  = models.CharField(max_length=100)
    email = models.EmailField(max_length = 150,unique=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


    
    class Meta:
        ordering = ["-created_at"]
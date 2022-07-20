from django.db import models

# Create your models here.

class Category(models.Model):
    diag_code=models.CharField(max_length=10)
    title=models.CharField(max_length=200)
    created_on=models.DateTimeField(auto_now_add=True)
    update_on=models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        """Return a human readable representation of the model instance."""
        return self.title
    
    
    
class Code(models.Model):
    dignosis_code=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    abbreviated_description=models.CharField(max_length=2048)
    full_description=models.TextField()
    
    def __str__(self) -> str:
        """Return a human readable representation of the model instance."""
        return self.dignosis_code
    
    



    
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Recipes(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.CharField(max_length=10)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to="recipes")  
    recipe_view_count = models.IntegerField(default=1)

    # def __str__(self) -> str:
    #     return self.userpython
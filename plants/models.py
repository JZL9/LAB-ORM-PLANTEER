from django.db import models

# Create your models here.

class Plant(models.Model):

    class Category(models.TextChoices):
        TREE = "tree", "Tree"
        FRUIT = "fruit", "Fruit"
        VEGETABLE = "vegetable", "Vegetables"
        FLOWER = "flower", "Flower"
        HERB = "herb", "Herb"
        SUCCULENT = "succulent", "Succulent"

    name = models.CharField(max_length=1024)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to="plants/")
    category = models.CharField(max_length=20, choices=Category.choices, default=Category.TREE)
    is_edible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
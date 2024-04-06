from django.db import models
from django.urls import reverse

PLANTAIN_TYPES = (
    ('C', 'Cooking Plantains'),
    ('S', 'Sweet Plantains'),
    ('G', 'Green Plantains'),
    ('R', 'Ripe Plantains'),
)


# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('drinks_detail', kwargs={'pk': self.id})


class Plantain(models.Model):
    name = models.CharField(max_length=100)
    ptype = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    origin = models.CharField(max_length=100)
    image_url = models.URLField(blank=True)
    drinks = models.ManyToManyField(Drink)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'plantain_id': self.id})
    
class Recipe(models.Model):
    plantain = models.ForeignKey(Plantain, on_delete=models.CASCADE)
    ingredients = models.TextField() 
    directions = models.TextField()
    serving = models.IntegerField()
    plntype = models.CharField(
        max_length=1,
        choices=PLANTAIN_TYPES,
        default=PLANTAIN_TYPES[0][0]
    )

    plantain = models.ForeignKey(Plantain, on_delete=models.CASCADE)

    def __str__(self):
        return f"Recipe for {self.plantain.name} that uses {self.get_plntype_display()}"
    
    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.id})
    

from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Plantain, Drink
from .forms import RecipeForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plantains_index(request):
    plantains = Plantain.objects.all()
    return render(request, 'plantains/index.html', {
        'plantains': plantains
    })

def plantains_detail(request, plantain_id):
    plantain = Plantain.objects.get(id=plantain_id)
    id_list = plantain.drinks.all().values_list('id')
    drinks_plantain_doesnt_have = Drink.objects.exclude(id__in=id_list)

    recipe_form = RecipeForm()
    return render(request, 'plantains/detail.html', {
        'plantain': plantain,
        'recipe_form': recipe_form,
        'drinks': drinks_plantain_doesnt_have,
    })

def assoc_drink(request, plantain_id, drink_id):
    Plantain.objects.get(id=plantain_id).drinks.add(drink_id)
    return redirect ('detail', plantain_id=plantain_id)

def unassoc_drink(request, plantain_id, drink_id):
    Plantain.objects.get(id=plantain_id).drinks.remove(drink_id)
    return redirect ('detail', plantain_id=plantain_id)


def add_recipe(request, plantain_id):
    form = RecipeForm(request.POST)

    if form.is_valid():
        new_recipe = form.save(commit=False)
        new_recipe.plantain_id = plantain_id
        new_recipe.save()
    return redirect('detail', plantain_id=plantain_id)

class PlantainCreate(CreateView):
    model = Plantain
    fields= ['name', 'description', 'origin', 'image_url']

class PlantainUpdate(UpdateView):
    model = Plantain
    fields= ['ptype', 'description', 'origin', 'image_url' ]

class PlantainDelete(DeleteView):
    model = Plantain
    success_url = '/plantains'

class DrinkList(ListView):
    model = Drink

class DrinkDetail(DetailView):
    model = Drink
    dields = '__all__'

class DrinkCreate(CreateView):
    model = Drink
    fields = '__all__'

class DrinkUpdate(UpdateView):
    model = Drink
    fields = '__all__'

class DrinkDelete(DeleteView):
    model = Drink
    success_url = '/drinks'
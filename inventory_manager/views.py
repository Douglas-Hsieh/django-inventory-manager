from django.shortcuts import render, redirect, reverse
from inventory_manager.models import Drink, Snack
from .forms import DrinkForm, SnackForm


def home_view(request):
    """ Homepage """
    return render(request, 'inventory_manager/home.html')


def drink_create_view(request):
    """ Handles creation of Drink """

    if request.method == 'GET':
        # User retrieves form
        form = DrinkForm()
        context = {
            'form': form,
        }
        return render(request, 'inventory_manager/drink_create.html', context)
    elif request.method == 'POST':
        # User submits form
        form = DrinkForm(request.POST or None)
        if form.is_valid():
            # Create Drink
            form.save()
        return redirect(to=reverse('inventory_manager:home'))
    else:
        return redirect(to=reverse('inventory_manager:home'))


def drink_detail_view(request, pk):
    """ Handles displaying details on Drink """
    try:
        drink = Drink.objects.get(pk=pk)
    except Drink.DoesNotExist:
        return redirect(to=reverse('inventory_manager:home'))

    context = {
        'drink': drink
    }
    return render(request, 'inventory_manager/drink_detail.html', context)


def drink_update_view(request, pk):
    """ Handles updating a Drink """
    try:
        drink = Drink.objects.get(pk=pk)
    except Drink.DoesNotExist:
        return redirect(to=reverse('inventory_manager:home'))

    if request.method == 'GET':
        context = {
            'form': DrinkForm(instance=drink),
            'drink': drink,
        }
        return render(request, 'inventory_manager/drink_update.html', context)
    elif request.method == 'POST':
        form = DrinkForm(request.POST or None)
        if form.is_valid():
            drink.name = form.cleaned_data['name']
            drink.ingredients = form.cleaned_data['ingredients']
            drink.snacks.set(form.cleaned_data['snacks'])
            drink.save()
        return redirect(to=reverse('inventory_manager:home'))
    else:
        return redirect(to=reverse('inventory_manager:home'))


def drink_delete_view(request, pk):
    """ Handles deleting a Drink """
    try:
        drink = Drink.objects.get(pk=pk)
    except Drink.DoesNotExist:
        return redirect(to=reverse('inventory_manager:home'))

    drink.delete()
    return redirect(to=reverse('inventory_manager:home'))


def drink_list_view(request):
    """ Handles listing a set of Drinks """

    drinks = Drink.objects.all()
    context = {
        'drinks': drinks
    }
    return render(request, 'inventory_manager/drink_list.html', context)


def snack_create_view(request):
    """ Handles creation of Snack """

    if request.method == 'GET':
        # User retrieves form
        form = SnackForm()
        context = {
            'form': form,
        }
        return render(request, 'inventory_manager/snack_create.html', context)
    elif request.method == 'POST':
        # User submits form
        form = SnackForm(request.POST or None)
        if form.is_valid():
            # Create Snack
            form.save()
        return redirect(to=reverse('inventory_manager:home'))

    return redirect(to=reverse('inventory_manager:home'))


def snack_detail_view(request, pk):
    """ Handles displaying details on Snack """

    try:
        snack = Snack.objects.get(pk=pk)
    except Snack.DoesNotExist:
        return redirect(to=reverse('inventory_manager:home'))
    context = {
        'snack': snack
    }
    return render(request, 'inventory_manager/snack_detail.html', context)


def snack_update_view(request, pk):
    """ Handles updating a Snack """
    try:
        snack = Snack.objects.get(pk=pk)
    except Snack.DoesNotExist:
        return redirect(to=reverse('inventory_manager:home'))

    if request.method == 'GET':
        context = {
            'form': SnackForm(instance=snack),
            'snack': snack,
        }
        return render(request, 'inventory_manager/snack_update.html', context)
    elif request.method == 'POST':
        form = SnackForm(request.POST or None)
        if form.is_valid():
            snack.name = form.cleaned_data['name']
            snack.ingredients = form.cleaned_data['ingredients']
            snack.drinks.set(form.cleaned_data['drinks'])
            snack.save()
        return redirect(to=reverse('inventory_manager:home'))
    else:
        return redirect(to=reverse('inventory_manager:home'))


def snack_delete_view(request, pk):
    """ Handles deleting a Snack """
    try:
        snack = Snack.objects.get(pk=pk)
    except Snack.DoesNotExist:
        return redirect(to=reverse('inventory_manager:home'))

    snack.delete()
    return redirect(to=reverse('inventory_manager:home'))


def snack_list_view(request):
    """ Handles listing a set of Snacks """
    snacks = Snack.objects.all()
    context = {
        'snacks': snacks
    }
    return render(request, 'inventory_manager/snack_list.html', context)

from django import forms
from inventory_manager.models import Drink, Snack


class DrinkForm(forms.ModelForm):

    snacks = forms.ModelMultipleChoiceField(queryset=Snack.objects.all(), required=False)

    class Meta:
        model = Drink
        fields = [
            'name',
            'ingredients',
            'snacks',
        ]


class SnackForm(forms.ModelForm):

    drinks = forms.ModelMultipleChoiceField(queryset=Drink.objects.all(), required=False)

    class Meta:
        model = Snack
        fields = [
            'name',
            'ingredients',
            'drinks',
        ]

    def save(self, *args, **kwargs):
        instance = super(SnackForm, self).save(*args, **kwargs)

        # Make ModelForm work for reverse side of ManyToMany relationship between Drink, Snack
        instance.drinks.set(self.cleaned_data['drinks'])

        return instance


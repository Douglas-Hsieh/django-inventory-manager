from django.test import TestCase
from django.urls import reverse
from .models import Drink, Snack
# Create your tests here.


class DrinkCreateViewTests(TestCase):
    """
    Test Drink creation and a Drink's recommended Snacks
    """
    url = reverse('inventory_manager:drink_create')

    def test_create_one_drink(self):
        """
        Test creating one Drink
        :return:
        """

        response = self.client.post(path=self.url, data={
            'name': 'snack',
            'ingredients': 'ingredient'
        })

        self.assertEqual(response.status_code, 302)  # Redirect

        drink = Drink.objects.get(pk=1)
        self.assertEqual(drink.name, 'snack')
        self.assertEqual(drink.ingredients, 'ingredient')

    def test_create_one_drink_with_two_recommended_snacks(self):
        """
        Test creating one Drink that has two recommended snacks and one snack it does not recommend.
        :return:
        """

        # Snacks that exist before creating drink
        snack_1 = Snack.objects.create(name='snack 1', ingredients='snack ingredient 1')
        snack_2 = Snack.objects.create(name='snack 2', ingredients='snack ingredient 2')
        snack_3 = Snack.objects.create(name='snack 3', ingredients='snack ingredient 3')

        response = self.client.post(path=self.url, data={
            'name': 'drink',
            'ingredients': 'drink ingredient',
            'snacks': (2, 3)
        })

        self.assertEqual(response.status_code, 302)  # Redirect

        drink = Drink.objects.get(pk=1)
        drink_snacks = drink.snacks.all()

        # drink correctly recommends snacks
        self.assertRaises(Snack.DoesNotExist, drink_snacks.get, pk=1)  # drink does not recommend snack 1
        self.assertEqual(drink_snacks.get(pk=2), snack_2)  # drink recommends snack 2
        self.assertEqual(drink_snacks.get(pk=3), snack_3)  # drink recommends snack 3

        # recommended snacks correctly recommend drink
        self.assertFalse(snack_1.drinks.all())  # snack 1 does not recommend drink
        self.assertEqual(snack_2.drinks.get(pk=1), drink)  # snack 2 recommends drink
        self.assertEqual(snack_3.drinks.get(pk=1), drink)  # snack 3 recommends drink

    def test_create_two_drinks_that_share_recommended_snacks(self):
        """
        Test creating two Drinks that share a recommended snack. Drinks and snacks should recommend each other
        correctly.
        :return:
        """

        # Snacks that exist before creating drink
        snack_1 = Snack.objects.create(name='snack 1', ingredients='snack ingredient 1')
        snack_2 = Snack.objects.create(name='snack 2', ingredients='snack ingredient 2')
        snack_3 = Snack.objects.create(name='snack 3', ingredients='snack ingredient 3')

        response_1 = self.client.post(path=self.url, data={
            'name': 'drink 1',
            'ingredients': 'drink ingredient 1',
            'snacks': (1, 2)
        })
        response_2 = self.client.post(path=self.url, data={
            'name': 'drink 2',
            'ingredients': 'drink ingredient 2',
            'snacks': (2, 3)
        })

        # Redirect
        self.assertEqual(response_1.status_code, 302)
        self.assertEqual(response_2.status_code, 302)

        # drink 1 correctly recommends snacks
        drink_1 = Drink.objects.get(pk=1)
        drink_1_snacks = drink_1.snacks.all()
        self.assertEqual(drink_1_snacks.get(pk=1), snack_1)
        self.assertEqual(drink_1_snacks.get(pk=2), snack_2)
        self.assertRaises(Snack.DoesNotExist, drink_1_snacks.get, pk=3)

        # drink 2 correctly recommends snacks
        drink_2 = Drink.objects.get(pk=2)
        drink_2_snacks = drink_2.snacks.all()
        self.assertRaises(Snack.DoesNotExist, drink_2_snacks.get, pk=1)
        self.assertEqual(drink_2_snacks.get(pk=2), snack_2)
        self.assertEqual(drink_2_snacks.get(pk=3), snack_3)

        # snacks correctly recommend drinks
        snack_1_drinks = snack_1.drinks.all()
        self.assertEqual(snack_1_drinks.get(pk=1), drink_1)
        self.assertRaises(Drink.DoesNotExist, snack_1_drinks.get, pk=2)

        snack_2_drinks = snack_2.drinks.all()
        self.assertEqual(snack_2_drinks.get(pk=1), drink_1)
        self.assertEqual(snack_2_drinks.get(pk=2), drink_2)

        snack_3_drinks = snack_3.drinks.all()
        self.assertRaises(Drink.DoesNotExist, snack_3_drinks.get, pk=1)
        self.assertEqual(snack_3_drinks.get(pk=2), drink_2)


class DrinkUpdateViewTests(TestCase):
    """
    Test updating a Drink
    """

    def test_update_drink(self):
        # Snacks that exist before creating drink
        snack_1 = Snack.objects.create(name='snack 1', ingredients='snack ingredient 1')
        snack_2 = Snack.objects.create(name='snack 2', ingredients='snack ingredient 2')

        drink = Drink.objects.create(name='name before', ingredients='drink ingredient before')
        drink.snacks.add(snack_1)

        # Information before update is correct
        self.assertEqual(drink.name, 'name before')
        self.assertEqual(drink.ingredients, 'drink ingredient before')
        self.assertEqual(drink.snacks.get(pk=1), snack_1)
        self.assertRaises(Snack.DoesNotExist, drink.snacks.get, pk=2)

        # Update
        url = reverse('inventory_manager:drink_update', kwargs={'pk': drink.pk})
        response = self.client.post(path=url, data={
            'name': 'name after',
            'ingredients': 'drink ingredient after',
            'snacks': 2
        })

        updated_drink = Drink.objects.get(pk=drink.pk)

        self.assertEqual(response.status_code, 302)  # Redirect

        # Information after update is correct
        self.assertEqual(updated_drink.name, 'name after')
        self.assertEqual(updated_drink.ingredients, 'drink ingredient after')
        self.assertRaises(Snack.DoesNotExist, updated_drink.snacks.get, pk=1)
        self.assertEqual(updated_drink.snacks.get(pk=2), snack_2)


class DrinkDeleteView(TestCase):
    """
    Test deleting a Drink
    """

    def test_delete_drink(self):
        # Snacks that exist before creating drink
        snack = Snack.objects.create(name='snack 1', ingredients='snack ingredient 1')

        drink = Drink.objects.create(name='name', ingredients='ingredient')

        url = reverse('inventory_manager:drink_delete', kwargs={'pk': drink.pk})
        response = self.client.get(url)

        # Redirect
        self.assertEqual(response.status_code, 302)

        # drink does not exist after delete
        self.assertRaises(Drink.DoesNotExist, Drink.objects.get, pk=drink.pk)

        # snacks do not recommend deleted drink
        self.assertFalse(snack.drinks.all())

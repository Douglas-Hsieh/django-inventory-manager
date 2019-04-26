=====
Inventory Manager
=====

Inventory Manager is a simple Django app to manage an inventory of drink and snacks. Each snack/drink can have a set of recommended drinks/snacks.

Quick start
-----------

1. Add "inventory_manager" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'inventory_manager',
    ]

2. Include the inventory_manager URLconf in your project urls.py like this::

    path('inventory_manager/', include('inventory_manager.urls')),

3. Run `python manage.py migrate` to create the inventory_manager models.

4. Start development server and visit http://127.0.0.1:8000/inventory_manager/ to manage inventory.

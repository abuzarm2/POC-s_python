# Online Food Delivery and Zoom Car Rent Python POC

## Online Food Delivery

### Overview

This Python POC (Proof of Concept) demonstrates an Online Food Delivery system using Object-Oriented Programming (OOP) principles.

### Classes

#### `FoodDelivery`

- **Methods:**
  - `__init__(self)`: Constructor that displays available food items based on category.
  - `show_available_items(self, category)`: Displays available food items for a given category.
  - `show_price(self, category)`: Displays prices of available items for a given category.
  - `apply_discount(self, category, promo_code)`: Applies a 10 percent discount on each category based on the provided promo code.
  - `add_to_cart(self, category, item)`: Adds a given food item to the cart and displays a message.
  - `buy_now(self, item, price, amount_paid)`: Decides whether the user can buy the food based on the parameters and displays a success message on successful purchase.

#### Usage

```python
from food_delivery import FoodDelivery

fd = FoodDelivery()
print(fd.show_available_items("North Indian"))
print(fd.show_price("North Indian"))
print(fd.apply_discount("North Indian", "pythonlearner"))
print(fd.add_to_cart("North Indian", "Paneer Tikka"))
print(fd.cart)
print(fd.buy_now("Paneer Tikka", 10.0, 10.0))
```

## Zoom Car Rent

### Overview

This Python POC demonstrates a Zoom Car Rent system using Object-Oriented Programming (OOP) principles.

### Classes

#### `ZoomCarRent`

- **Methods:**
  - `__init__(self)`: Constructor that lists the numbers of cars available based on categories.
  - `display_available_cars(self, category)`: Displays available cars for a given category.
  - `display_car_price(self, category)`: Displays car prices based on the category.
  - `apply_seller_discount(self, category, promo_code)`: Applies a 10 percent discount based on the provided promo code.
  - `book_ride(self, category, car_name, hours)`: Books a ride, asks for price, car name, and hours to ride, and gives a successful booking message.
  - `handle_damage(self, damage_amount)`: Handles damage - user should pay the full amount for repairs.

#### Usage

```python
from zoom_car_rent import ZoomCarRent

zcr = ZoomCarRent()
print(zcr.display_available_cars("Micro"))
print(zcr.display_car_price("Micro"))
print(zcr.apply_seller_discount("Micro", "seller10"))
print(zcr.book_ride("Micro", "Alto", 3))
print(zcr.handle_damage(5000.0))
```

### Coding Conventions

1. All methods have exception handling.
2. Class names follow camel case, and method names are in snake case.
3. Code is written in VS Code.
4. Python files are organized as a package and can be imported in another folder.

Feel free to explore and test various orders and rides using the provided use cases.

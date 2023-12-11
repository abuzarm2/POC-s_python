class FoodDelivery:
    def __init__(self):
        self.food_items = {
            'North Indian': ['Paneer Tikka', 'Butter Chicken', 'Aloo Gobi', 'Dal Makhani', 'Chicken Biryani'],
            'South Indian': ['Dosa', 'Idli', 'Sambhar Vada', 'Chicken Chettinad', 'Hyderabadi Biryani'],
            'Italian': ['Margherita Pizza', 'Pasta Carbonara', 'Bruschetta', 'Lasagna', 'Tiramisu'],
            'Chinese': ['Spring Rolls', 'Sweet and Sour Chicken', 'Fried Rice', 'Manchurian', 'Dim Sum'],
            'Continental': ['Grilled Salmon', 'Chicken Caesar Salad', 'Beef Stroganoff', 'Vegetable Lasagna', 'Chocolate Fondue']
        }
        self.cart = {}

    def show_all_food_items(self):
        try:
            for category, food_items in self.food_items.items():
                print(f"{category} Food:")
                for items in food_items:
                    print(f"  - {items}")
                print()  # Empty line for better readability
        except Exception as e:
            raise e
        
    def show_available_items(self, category):
        try:
            return self.food_items[category]
        except KeyError:
            raise ValueError("Invalid food category")

    def show_price(self, category):
        try:
            items = self.show_available_items(category)
            prices = {item: 10.0 for item in items}  # Dummy prices for demonstration
            return prices
        except ValueError as e:
            raise e

    def apply_discount(self, category, promo_code):
        try:
            if promo_code == "pythonlearner":
                prices = self.show_price(category)
                discounted_prices = {item: price * 0.9 for item, price in prices.items()}
                return discounted_prices
            else:
                raise ValueError("Invalid promo code")
        except ValueError as e:
            raise e

    def add_to_cart(self, category, item):
        try:
            items = self.show_available_items(category)
            if item in items:
                self.cart[item] = 10.0  # Dummy price for demonstration
                return f"{item} added to the cart"
            else:
                raise ValueError("Invalid food item")
        except ValueError as e:
            raise e

    def buy_now(self, item, price, amount_paid):
        try:
            if amount_paid >= price:
                del self.cart[item]
                return "Order successfully purchased and will be delivered"
            else:
                return "Insufficient amount. Please pay the correct amount."
        except KeyError:
            raise ValueError("Item not found in the cart")



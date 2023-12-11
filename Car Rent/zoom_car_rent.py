class ZoomCarRent:
    def __init__(self):
        self.available_cars = {
            'Micro': ['Alto', 'Nano', 'Swift', 'WagonR', 'i10'],
            'Sedan': ['Honda City', 'Toyota Corolla', 'Hyundai Verna', 'Maruti Ciaz', 'Ford Aspire'],
            'SUV': ['Fortuner', 'Ford Endeavour', 'Mahindra XUV500', 'Tata Harrier', 'Jeep Compass'],
            'Luxury Car': ['Jaguar XF', 'Audi A8', 'Mercedes S-Class', 'BMW 7 Series', 'Lexus LS']
        }
    
    def display_all_available_cars(self):
        try:
            for category, cars in self.available_cars.items():
                print(f"{category} Cars:")
                for car in cars:
                    print(f"  - {car}")
                print()  # Empty line for better readability
        except Exception as e:
            raise e

    def display_available_cars(self, category):
        try:
            return self.available_cars[category]
        except KeyError:
            raise ValueError("Invalid car category")

    def display_car_price(self, category):
        try:
            cars = self.display_available_cars(category)
            prices = {car: 100.0 if category == 'Micro' else 150.0 if category == 'Sedan' else 200.0 if category == 'SUV' else 300.0 for car in cars}
            return prices
        except ValueError as e:
            raise e

    def apply_seller_discount(self, category, promo_code):
        try:
            if promo_code == "seller10":
                prices = self.display_car_price(category)
                discounted_prices = {car: price * 0.9 for car, price in prices.items()}
                return discounted_prices
            else:
                raise ValueError("Invalid promo code")
        except ValueError as e:
            raise e

    def book_ride(self, category, car_name, hours):
        try:
            prices = self.display_car_price(category)
            price_per_hour = prices[car_name]
            total_price = price_per_hour * hours
            return f"Booking successful! Your total amount is {total_price} INR."
        except ValueError as e:
            raise e

    def handle_damage(self, damage_amount):
        return f"Damage detected! Please pay {damage_amount} INR for repairs."

# Example usage:
# zcr = ZoomCarRent()
# print(zcr.display_available_cars("Micro"))
# print(zcr.display_car_price("Micro"))
# print(zcr.apply_seller_discount("Micro", "seller10"))
# print(zcr.book_ride("Micro", "Alto", 3))
# print(zcr.handle_damage(5000.0))

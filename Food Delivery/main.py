from food_delivery import FoodDelivery

def main():
    fd = FoodDelivery()

    try:
        print(fd.show_available_items("North Indian"))
        print(fd.show_price("North Indian"))
        print(fd.apply_discount("North Indian", "pythonlearner"))
        print(fd.add_to_cart("North Indian", "Paneer Tikka"))
        print(fd.cart)
        print(fd.buy_now("Paneer Tikka", 10.0, 10.0))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

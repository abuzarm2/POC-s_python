from zoom_car_rent import ZoomCarRent

def main():
    zcr = ZoomCarRent()

    try:
        zcr.display_all_available_cars()
        print(zcr.display_available_cars("Micro"))
        print(zcr.display_car_price("Micro"))
        print(zcr.apply_seller_discount("Micro", "seller10"))
        print(zcr.book_ride("Micro", "Alto", 3))
        print(zcr.handle_damage(5000.0))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

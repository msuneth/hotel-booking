import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.hotel_name = df.loc[df["id"] == hotel_id, "name"].squeeze()

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)
        print("hotel booked")

    def available(self):
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            print("hotel available")
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customers_name, hotel_object):
        self.customer_name = customers_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for booking
        name = {self.customer_name}
        hotel = {self.hotel.hotel_name}
        """
        return content


print(df)
hotel_Id = input("Enter hotel Id:")
hotel = Hotel(hotel_Id)

if hotel.available():
    hotel.book()
    customer_name = input("Enter customer name:")
    reservation = ReservationTicket(customer_name, hotel)
    print(reservation.generate())
else:
    print("Hotel is not available")

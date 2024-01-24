import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

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
    def __init__(self, name, hotel):
        pass

    def generate(self):
        pass


print(df)
hotel_Id = input("Enter hotel Id:")
hotel = Hotel(hotel_Id)

if hotel.available():
    hotel.book()
    name = input("Enter customer name:")
    reservation = ReservationTicket(name, hotel)
    print(reservation.generate())
else:
    print("Hotel is not available")

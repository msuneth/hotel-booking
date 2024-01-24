import pandas as pd

df = pd.read_csv("hotels.csv")


class Hotel:
    def __init__(self, id):
        pass

    def book(self):
        pass

    def available(self):
        return True


class ReservationTicket:
    def __init__(self, name, hotel):
        pass

    def generate(self):
        pass


print(df)
id = input("Enter hotel Id:")
hotel = Hotel(id)

if hotel.available():
    hotel.book()
    name = input("Enter customer name:")
    reservation = ReservationTicket(name, hotel)
    print(reservation.generate())
else:
    print("Hotel is not available")

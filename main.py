import pandas as pd

df = pd.read_csv("hotels.csv")


class Hotel:
    def __init__(self, id):
        self.id = id

    def book(self):
        pass

    def available(self):
        pass


class ReservationTicket:
    def __init__(self, username, hotel):
        self.username = username
        self.hotel = hotel

    def generate_ticket(self):
        content = f"{username}, your ticket for {hotel} has been generated successfully"
        return content


print(df)
username = input("Enter your name: ")
hotel_id_input = input("Enter hotel ID:")
hotel = Hotel(id)
reservation_ticket = ReservationTicket(username, hotel)
if hotel.available():
    hotel.book()
    print(reservation_ticket.generate_ticket())
else:
    print('Hotel is currently unavailable')

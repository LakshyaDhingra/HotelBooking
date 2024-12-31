import pandas as pd

# dtype=str gets all data as string type, even if others were of different types,
# specifications can be done
df = pd.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

    def book(self):
        """Books hotel by changing availability to NO"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        # Saves change to existing csv file
        df.to_csv("hotels.csv", index=False)
        # index=False so that python is not able to add another column to index

    def available(self):
        """Checks if hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True


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
hotel = Hotel(hotel_id_input)
reservation_ticket = ReservationTicket(username, hotel)
if hotel.available():
    hotel.book()
    print(reservation_ticket.generate_ticket())
else:
    print('Hotel is currently unavailable')

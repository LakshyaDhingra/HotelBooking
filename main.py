import pandas as pd

# dtype=str gets all data as string type, even if others were of different types,
# specifications can be done
df = pd.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

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
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object

    def generate_ticket(self):
        content = f"""
        Hi {self.customer_name}, your ticket for {self.hotel_object.name} has been generated successfully
        
        Here is your booking data:
        Customer Name: {self.customer_name}
        Hotel Name: {self.hotel_object.name}
        Hotel ID: {self.hotel_object.hotel_id}
        """
        return content




print(df)
username = input("Please, Enter your name : ")
hotel_id_input = input("Enter Hotel ID : ")
hotel = Hotel(hotel_id_input)
reservation_ticket = ReservationTicket(customer_name=username, hotel_object=hotel)
if hotel.available():
    hotel.book()
    print(reservation_ticket.generate_ticket())
else:
    print('Sorry, the Hotel is currently unavailable')

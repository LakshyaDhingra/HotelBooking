import pandas as pd
# abstract based class(abc) module
from abc import ABC, abstractmethod

df = pd.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    # Class variable, can be used by all instances
    watermark = "The Caped Crusader"

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        # Instance variable, can be used only by instances
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
    # Instance methods

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
    # Class method, @..... are decorators

    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

    # magic method used actually which is covered by ==
    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True


# cannot instantiate an abstract class
class Ticket(ABC):

    @abstractmethod
    def generate_ticket(self):
        pass
    # no implementation done in abstract methods


class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object

    # subclass of Ticket and implementation done below of abstract method
    def generate_ticket(self):
        content = f"""
        Hi {self.the_customer_name}, your ticket for {self.hotel_object.name} has been generated successfully
        
        Here is your booking data:
        Customer Name: {self.the_customer_name}
        Hotel Name: {self.hotel_object.name}
        Hotel ID: {self.hotel_object.hotel_id}
        """
        return content

    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    @staticmethod
    def convert(amount):
        return amount*10


class DigitalTicket(Ticket):
    def generate_ticket(self):
        return "Hi, here's your ticket"

    def download(self):
        pass


hotel1 = Hotel(hotel_id="134")
hotel2 = Hotel(hotel_id="188")
hotel3 = Hotel(hotel_id="655")

print(hotel3.available())

print(hotel1.watermark)
print(hotel2.watermark)

print(hotel1.name)
print(hotel2.name)

print(Hotel.watermark)

print(Hotel.get_hotel_count(data=df))

ticket = ReservationTicket(customer_name="john smith ", hotel_object=hotel1)
print(ticket.the_customer_name)

a = ReservationTicket.convert(10)
print(a)

print(ticket.generate_ticket())

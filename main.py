import pandas as pd

# dtype=str gets all data as string type, even if others were of different types,
# specifications can be done
df = pd.read_csv("hotels.csv", dtype={"id": str})
df2 = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df3 = pd.read_csv("card_security.csv", dtype=str)


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


class CreditCard:
    def __init__(self, card_no):
        self.card_no = card_no

    def validate(self, card_expiry, card_cvc, card_name):
        """Checks if card is valid"""
        card_data = {"number": self.card_no, "expiration": card_expiry,
                     "holder": card_name, "cvc": card_cvc}
        if card_data in df2:
            return True


class CardSecurity(CreditCard):
    def authenticate(self, pass_entered):
        auth_password = df3.loc[df3["number"] == self.card_no, "password"].squeeze()
        if auth_password == pass_entered:
            return True


class Spa(Hotel):
    def __init__(self, customer_name, hotel_name):
        self.customer_name = customer_name
        self.hotel_name = hotel_name

    def generate_spa_ticket(self):
        content2 = f"""
        Thank you for your SPA reservation!
        
        Here is your SPA booking data:
        Customer Name: {self.customer_name}
        Hotel Name: {self.hotel_name}
        """
        return content2


print(df)
username = input("Please, Enter your name : ")
hotel_id_input = input("Enter Hotel ID : ")
hotel = Hotel(hotel_id_input)
reservation_ticket = ReservationTicket(customer_name=username, hotel_object=hotel)
if hotel.available():
    print("Available to book!\n")
    print("Processing.......")
    auth_no = input("\nEnter your card number:- ")
    auth_pass = input("Enter your authentication password:- ")
    user_card = CardSecurity(card_no=auth_no)
    if user_card.validate(card_expiry="12/26", card_cvc="123", card_name="JOHN SMITH"):
        if user_card.authenticate(auth_pass):
            hotel.book()
            print(reservation_ticket.generate_ticket())
        else:
            print("Credit card authentication failed, Please try again!")
    else:
        print("There was a problem with the payment method, Please try again!")
else:
    print('Sorry, the Hotel is currently unavailable')

spa_package = Spa(username, hotel.name)
package = input("Do you want to book a spa package? ")
if package == "yes":
    print(spa_package.generate_spa_ticket())

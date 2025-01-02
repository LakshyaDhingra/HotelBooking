import pandas as pd
from fpdf import FPDF

df = pd.read_csv("articles.csv", dtype={"in stock": "int", "price": "float"})


class Appliance:
    def __init__(self, appliance_id):
        self.appliance_id = appliance_id
        self.name = df.loc[df["id"] == self.appliance_id, "name"].squeeze()
        self.price = df.loc[df["id"] == self.appliance_id, "price"].squeeze()

    def buy(self):
        """Subtracts item from stock when bought"""
        df.loc[df["id"] == self.appliance_id, "in stock"] -= 1
        df.to_csv("articles.csv", index=False)

    def check_stock(self):
        """Checks if hotel is available"""
        stock = df.loc[df["id"] == self.appliance_id, "in stock"].squeeze()
        if stock > 0:
            return True


class Receipt:
    def __init__(self, article):
        self.article = article

    def generate_receipt(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt No. {self.article.appliance_id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.article.name.title()}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.article.price}", ln=1)

        pdf.output("receipt.pdf")


print(df)
appliance_id_input = int(input("Enter Appliance ID : "))
appliance = Appliance(appliance_id_input)
receipt = Receipt(appliance)
if appliance.check_stock():
    appliance.buy()
    receipt.generate_receipt()
else:
    print('Sorry, the item is currently out of stock')


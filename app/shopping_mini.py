
from datetime import datetime
import os

#GOAL 1: simplify USD formatting
#GOAL 2: simplify receipt printing/ file writing
#GOAL 3: simplify tax rate

selected_products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
] # FYI: for the purposes of this exercise, you won't need to modify this list at all

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and displaying purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/datatypes
    Param: my_price (int or float) like 40000.444444
    example: to_usd(40000.444444)
    Return: $4,000.44
    """
    return f"${my_price:,.2f}"

checkout_at = datetime.now().strftime("%M/%d/%Y %I:%m %p")

now = datetime.now()

subtotal = sum([p["price"] for p in selected_products])

# PRINT RECEIPT

receipt = ""


receipt += "\n---------"
receipt += "\nCHECKOUT AT: " + str(now.strftime("%Y-%M-%d %H:%m:%S"))
receipt += "\n---------"

for p in selected_products:
    receipt += "\nSELECTED PRODUCT: " + p["name"] + "   " + to_usd(p["price"])

receipt += "\n---------"
receipt += f"\nSUBTOTAL: {to_usd(subtotal)}"
receipt += f"\nTAX: {to_usd(subtotal * 0.0875)}"
receipt += f"\nTOTAL: {to_usd((subtotal * 0.0875) + subtotal)}"
receipt += "\n---------"
receipt += "\nTHANK YOU! PLEASE COME AGAIN SOON!"
receipt += "\n---------"


print(receipt)

# WRITE RECEIPT TO FILE

file_name = os.path.join(os.path.dirname(__file__), "..", "receipts", f"{now.strftime('%Y-%M-%d-%H-%m-%S')}.txt")
with open(file_name, 'w') as f:
   f.write(receipt)

   
   
   
   ## f.write("------------------------------------------")
   ## for p in selected_products:
   ##     f.write("\nSELECTED PRODUCT: " + p["name"] + "   " + to_usd(p["price"]))
##
   ## f.write("---------")
   ## f.write(f"SUBTOTAL: {to_usd(subtotal)}")
   ## f.write(f"TAX: {to_usd(subtotal * 0.1)}")
   ## f.write(f"TOTAL: {to_usd((subtotal * 0.1) + subtotal)}")
   ## f.write("---------")
   ## f.write("THANK YOU! PLEASE COME AGAIN SOON!")
   ## f.write("---------")

# TODO: SEND RECEIPT VIA EMAIL

# todo: sned the reciept variable



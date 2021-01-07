Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> print("Hello world")
Hello world
>>> lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester
blend on wood. 32 inches high x 40
inches
wide x 30 inches deep. Red or
white.
"""

lovely_loveseat_price = 254.00

stylish_setee_description = """
Stylish Settee. Faux leather on birch.
29.50 inches high x 54.75 inches wide
x 28 inches deep. Black.
"""

stylish_setee_price = 180.50

luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36
inches all. Brown with crean shade.
"""
luxurious_lamp_price = 52.15

sales_tax = .088

customer_one_total = 0
customer_one_itemization = """
Lovely Loveseat
Luxurious Lamp
"""
customer_one_total += lovely_loveseat_price + stylish_setee_price
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

print("Customer One Items")
print(customer_one_itemization)
print("Customer One Total:" , customer_one_total)

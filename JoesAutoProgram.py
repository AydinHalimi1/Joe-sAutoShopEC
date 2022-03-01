import CarClass as c
import CustomerClass as cc
import ServiceQuoteClass as sq

BMW = c.Car("BMW","328i","2013")

print("1st Car Type:",BMW.get_make(),BMW.get_model(),BMW.get_year())

BMW.set_make("Lexus")

BMW.set_model("RX350")

BMW.set_year("2014")

print("2nd Car Type:", BMW.get_make(),BMW.get_model(),BMW.get_year())

Aydin = cc.Customer("Aydin","909 Baylor Ave","123-456-7890")

print("1st Customer Information:",Aydin.get_name(),Aydin.get_address(),Aydin.get_phone())

Aydin.set_name("Leyla")

Aydin.set_address("123 Baylor St")

Aydin.set_phone("281-123-4567")

print("2nd Customer Information:",Aydin.get_name(),Aydin.get_address(),Aydin.get_phone())

OilChange = sq.ServiceQuote(35,20)

print("1st Customer Price:",OilChange.get_labor_charges(),OilChange.get_parts_charges(),'$',format(OilChange.get_sales_tax(),',.2f'),'$',format(OilChange.get_total_charges(),',.2f'))

OilChange.set_parts_charges(45)

OilChange.set_labor_charges(30)

print("2nd Customer Price:",OilChange.get_labor_charges(),OilChange.get_parts_charges(),'$',format(OilChange.get_sales_tax(),',.2f'),'$',format(OilChange.get_total_charges(),',.2f'))
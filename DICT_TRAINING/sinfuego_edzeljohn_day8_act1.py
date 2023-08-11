class Cellphone:

    color = " "
    model = ""
    manufacturer = ""

phones = []
phone1 = Cellphone()
phone1.color = "Black"
phone1.model = "iPhone 12 Pro Max"
phone1.manufacturer = "Apple"
phones.append(phone1)

phone2 = Cellphone()
phone2.color = "White"
phone2.model = "iPhone 12 Pro Max"
phone2.manufacturer = "Apple"
phones.append(phone2)

phone3 = Cellphone()
phone3.color = "Blue"
phone3.model = "C35"
phone3.manufacturer = "Cherry Mobile"
phones.append(phone3)

phone4 = Cellphone()
phone4.color = "Black"
phone4.model = "Vega 5"
phone4.manufacturer = "Vivo"
phones.append(phone4)

phone5 = Cellphone()
phone5.color = "White"
phone5.model = "Galaxy S21 Ultra"
phone5.manufacturer = "Samsung"
phones.append(phone5)

for i in phones:
    print("\nColor:", i.color, "\nModel:", i.model, "\nManufacturer:",i.manufacturer)


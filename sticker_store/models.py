from datetime import datetime

class Order:
    def __init__(self, id, status, firstname, surname, email, phone, date, stickers, total_cost):
        self.id = id
        self.status = status
        self.firstname = firstname
        self.surname = surname
        self.email = email
        self.phone = phone
        self.date = date
        self.stickers = stickers
        self.total_cost = total_cost
    
    def get_sticker_details(self):
        return str(self)

    def __repr__(self):
        str = "id: {}, Status: {}, Firstname: {}, Surname: {}, Email: {}, Phone: {}, Date: {}, Tours: {}, Total Cost: {}\n" 
        str =str.format( self.id, self.status,self.firstname,self.surname, self.email, self.phone, self.date, self.stickers, self.total_cost)
        return str

class Artist:
    def __init__(self, id, name, description, image, email):
        self.id = id
        self.name = name
        self.description = description
        self.image = image
        self.email = email

    def get_stickers(self):
        return str(self)

    def __repr__(self):
        str = "Name: {}, Description: {}, Image: {}, Email: {}\n"
        str = str.format(self.name, self.description, self.image, self.email)
        return str

class Sticker:
    def __init__(self, id, name, description, image, price, artist, date):
        self.id = id
        self.name = name
        self.description = description
        self.image = image
        self.price = price
        self.artist = artist
        self.date = date
    
    def get_sticker_details(self):
        return str(self)

    def __repr__(self):
        str = "Id: {}, Name: {}, Description: {}, Image: {}, Price: {}, City: {}, Date: {}\n" 
        str =str.format( self.id, self.name,self.description,self.image, self.price, self.artist, self.date)
        return str
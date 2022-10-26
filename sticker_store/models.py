from . import db

class Artist(db.Model):
    __tablename__='artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60))
    email = db.Column(db.String(60), nullable=False)
    stickers = db.relationship('Sticker', backref='Artist', cascade="all, delete-orphan")

    def __repr__(self):
        str = "Id: {}, Name: {}, Description: {}, Image: {}, Email: {}\n"
        str =str.format( self.id, self.name,self.description,self.image,self.email)
        return str

orderdetails = db.Table('orderdetails',
    db.Column('order_id', db.Integer,db.ForeignKey('orders.id'), nullable=False),
    db.Column('sticker_id',db.Integer,db.ForeignKey('stickers.id'),nullable=False),
    db.PrimaryKeyConstraint('order_id', 'sticker_id') )

class Sticker(db.Model):
    __tablename__='stickers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False)
    price = db.Column(db.Float, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    #sizeWidth = db.Column(db.Float(),)
    #sizeLength = db.Column(db.Float(),)
    shiny = db.Column(db.Boolean)
    puffy = db.Column(db.Boolean)
    category = db.Column(db.String(64))
    alt = db.Column(db.String(64))

    def __repr__(self):
        str = "Id: {}, Name: {}, Description: {}, Image: {}, Price: {}, Artist: {}, Date: {}\n"
        str = str.format(self.id, self.name,self.description,self.image, self.price, self.artist_id, self.shiny, self.puffy)
        return str

class Order(db.Model):
    __tablename__='orders'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    firstname = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    totalcost = db.Column(db.Float)
    date = db.Column(db.DateTime)
    stickers = db.relationship("Sticker", secondary=orderdetails, backref="orders")

    def __repr__(self):
        str = "id: {}, Status: {}, Firstname: {}, Surname: {}, Email: {}, Phone: {}, Date: {}, Stickers: {}, Total Cost: {}\n"
        str =str.format( self.id, self.status,self.firstname,self.surname, self.email, self.phone, self.date, self.stickers, self.totalcost)
        return str
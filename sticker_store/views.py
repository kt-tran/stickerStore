from datetime import datetime
from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import Artist, Sticker, Order
from .forms import CheckoutForm
from . import db

bp = Blueprint('main', __name__)

#homepage
@bp.route('/')
def index():
    stickers = Sticker.query.filter(Sticker.id.between(0,3))
    print (stickers)
    return render_template('index.html', stickers = stickers)

#search
@bp.route('/sticker_search/')
def search():
    search = request.args.get('search')
    search_copy = search
    search = '%{}%'.format(search)
    stickers = Sticker.query.filter(Sticker.name.like(search)).all()
    return render_template('search.html', stickers = stickers, search_copy = search_copy)

#return all artists
@bp.route('/artists')
def artists():
    artists = Artist.query.order_by(Artist.name).all()
    return render_template('all_artists.html', artists = artists)

#see all of the stickers one artist has
@bp.route('/artists/<int:artistid>/')
def artiststickers(artistid):
    stickers = Sticker.query.filter(Sticker.artist_id == artistid)
    artists =  Artist.query.filter_by(id=artistid).first()
    return render_template('artists_stickers.html', stickers = stickers, artists = artists.name)

@bp.route('/sticker/Space_Cat/')
def sticker_listing():
    stickers = Sticker.query.filter(Sticker.name == "Sparkle Space Cat")
    return render_template('sticker_listing.html', stickers = stickers)

@bp.route('/all_stickers/')
def all_stickers():
    stickers = Sticker.query.all()
    return render_template('all_stickers.html', stickers = stickers)

@bp.route('/flowers/')
def flowers():
    stickers = Sticker.query.filter(Sticker.category == "Flower")
    return render_template('cat_flowers.html', stickers = stickers)

@bp.route('/animals/')
def animals():
    stickers = Sticker.query.filter(Sticker.category == "Animal")
    return render_template('cat_animals.html', stickers = stickers)

@bp.route('/food_drink/')
def food_drink():
    stickers = Sticker.query.filter(Sticker.category == "Food_Or_Drink")
    return render_template('cat_food_drink.html', stickers = stickers)


@bp.route('/contact/')
def contact():
    return render_template('contact.html')


@bp.route('/order', methods=['POST','GET'])
def order():
    sticker_id = request.values.get('sticker_id')

    # retrieve order if there is one
    if 'order_id'in session.keys():
        order = Order.query.get(session['order_id'])
        # order will be None if order_id stale
    else:
        # there is no order
        order = None

    # create new order if needed
    if order is None:
        order = Order(status = False, firstname='', surname='', email='', phone='', totalcost=0, date=datetime.now())
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            print('failed at creating a new order')
            order = None
    
    # calcultate totalprice
    totalprice = 0
    if order is not None:
        for sticker in order.stickers:
            totalprice = totalprice + sticker.price
    
    # are we adding an item?
    if sticker_id is not None and order is not None:
        sticker = Sticker.query.get(sticker_id)
        if sticker not in order.stickers:
            try:
                order.stickers.append(sticker)
                db.session.commit()
            except:
                return 'There was an issue adding the item to your basket'
            return redirect(url_for('main.order'))
        else:
            flash('item already in basket')
            return redirect(url_for('main.order'))
    
    return render_template('order.html', order = order, totalprice = totalprice)


# Delete specific basket items
@bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    id=request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        sticker_to_delete = Sticker.query.get(id)
        try:
            order.stickers.remove(sticker_to_delete)
            db.session.commit()
            return redirect(url_for('main.order'))
        except:
            return 'Problem deleting item from order'
    return redirect(url_for('main.order'))


# Scrap basket
@bp.route('/deleteorder')
def deleteorder():
    if 'order_id' in session:
        del session['order_id']
        flash('Your basket was emptied successfully.')
    return redirect(url_for('main.index'))


@bp.route('/checkout/', methods=['POST','GET'])
def checkout():
    form = CheckoutForm()
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])

        if form.validate_on_submit():
            order.status = True
            order.firstname = form.firstname.data
            order.surname = form.surname.data
            order.email = form.email.data
            order.phone = form.phone.data
            totalcost = 0
            for sticker in order.stickers:
                totalcost = totalcost + sticker.price
            order.totalcost = totalcost
            order.date = datetime.now()
            try:
                db.session.commit()
                del session['order_id']
                flash('Order completed. Thank you! The artists will be in touch soon.')
                return redirect(url_for('main.index'))
            except:
                return 'There was an issue completing your order :('
    return render_template('checkout.html', form = form)
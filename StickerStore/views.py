from flask import Blueprint, render_template, request, url_for

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/artists')
def artists():
    return render_template('all_artists.html')

@bp.route('/space_cat/')
def sticker_listing():
    return render_template('sticker_listing.html')

@bp.route('/flowers/')
def flowers():
    return render_template('cat_flowers.html')

@bp.route('/all_stickers/')
def all_stickers():
    return render_template('all_stickers.html')

@bp.route('/contact/')
def contact():
    return render_template('contact.html')


@bp.route('/checkout/', methods=['POST', 'GET'])
def checkout():

    # print form paramenters sent using GET
    print('Firstname: {}\nSurname: {}\nPhone: {}'
          .format(request.values.get('firstname'), request.values.get('surname'), request.values.get('phone')))

    return render_template('checkout.html')

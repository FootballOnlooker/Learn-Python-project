from flask import Blueprint, render_template


blueprint = Blueprint('main', __name__, url_prefix='/')

@blueprint.route('/index')
def index_page():
    text = {'text': 'Test'}
    items = [
        {
            'brand': {'text': 'Catalog'},
            'body': 'Wireless headphones'
        }
    ]
    return render_template('index.html', title='Home Page', items=items)

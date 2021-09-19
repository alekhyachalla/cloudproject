from flask import Blueprint, render_template, session
from models import db, Users

redirect = Blueprint('redirect', __name__, template_folder='../frontend')
@redirect.route('/redirect', methods=['GET'])
def show():
    return render_template('redirect.html')

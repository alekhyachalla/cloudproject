from flask import Blueprint, url_for, render_template, redirect, request, session
from flask_login import LoginManager
from werkzeug.security import generate_password_hash
import sys
from models import db, Users
import os 

register = Blueprint('register', __name__, template_folder='../frontend')
login_manager = LoginManager()
login_manager.init_app(register)

@register.route('/register', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        session['first_name'] = first_name
        session['last_name'] = last_name
        session['username'] = username 
        session['email'] = email
        file_store = request.files['file']
        try: 
            os.makedirs(os.path.join('/tmp/files/',username))
        except:
            pass
        if file_store:
            file_store.save(os.path.join('/tmp/files/',username)+'/'+file_store.filename)
        if username and email and password and confirm_password:
            if password == confirm_password:
                hashed_password = generate_password_hash(
                    password, method='sha256')
                try:
                    new_user = Users(
                        username=username,
                        email=email,
                        password=hashed_password,
                        first_name=first_name,
                        last_name=last_name
                    )

                    db.session.add(new_user)
                    db.session.commit()
                except:
                    return redirect(url_for('register.show') + '?error=user-or-email-exists')

                return redirect(url_for('redirect.show'))
        else:
            return redirect(url_for('register.show') + '?error=missing-fields')
    else:
        return render_template('register.html')

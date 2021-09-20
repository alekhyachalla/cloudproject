from flask import Blueprint, render_template
from flask_login import LoginManager, login_required, current_user
import os
from models import db, Users

home = Blueprint('home', __name__, template_folder='../frontend')
login_manager = LoginManager()
login_manager.init_app(home)
file_path='/tmp/files/'

@home.route('/download/')
def download_file():
    path=file_path+current_user.username+'/'+os.listdir(file_path+current_user.username)[0]
    return send_file(path, as_attachment=True)

@home.route('/home', methods=['GET'])
@login_required
def show():
    num_words = 0
    if len(os.listdir(file_path+current_user.username)) != 0:
        with open(file_path+current_user.username+'/'+os.listdir(file_path+current_user.username)[0], 'r') as f:
            for line in f:
                words = line.split()
                num_words += len(words)
    else: 
        num_words = "File not uploaded"
    return render_template('home.html', word_count=str(num_words))

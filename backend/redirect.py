from flask import Blueprint, render_template, session, send_file
from models import db, Users
import os
redirect = Blueprint('redirect', __name__, template_folder='../frontend')
file_path='/tmp/files/'

@redirect.route('/download/')
def download_file():
    path=file_path+session['username']+'/'+os.listdir(file_path+session['username'])[0]
    return send_file(path, as_attachment=True)

@redirect.route('/redirect', methods=['GET'])
def show():
    num_words = 0
    if len(os.listdir(file_path+session['username'])) != 0:
        with open(file_path+session['username']+'/'+os.listdir(file_path+session['username'])[0], 'r') as f:
            for line in f:
                words = line.split()
                num_words += len(words)
    else:
         num_words = "File not uploaded"
    return render_template('redirect.html', word_count=str(num_words))

import os
import sys
from funciones.clasificacion import clasificacion

from flask import Flask
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '../data/espectrogramas'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        print('ingresa')
        # check if the post request has the file part
        if 'file' not in request.files:
            print('hmmm')
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            print('?')
            flash('No selected file')
            return redirect(request.url)
        print(file)
        print(allowed_file(file.filename))
        if file and allowed_file(file.filename):
            print('ok...')
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            results = clasificacion(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print('sale')

        return render_template('main.html', result=results)

    return render_template('main.html')
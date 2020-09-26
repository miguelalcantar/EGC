import os
import sys
from funciones.clasificacion import clasificacion
import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
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

        if file and allowed_file(file.filename):
            print('ok...')
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'data'))

            results = clasificacion(os.path.join(app.config['UPLOAD_FOLDER'], 'data'))

        print('sale')

        return render_template('main.html', result=get_max(results), display=True)

    return render_template('main.html')

def get_max(values):
    max = values[0]
    j = 0
    for i in range(1, len(values)):
        if max < values[i]:
            max = values[i]
            j = i

    if j == 0:
        type = 'N'
    elif j == 1:
        type = "S"
    elif j == 2:
        type = "V"
    elif j == 3:
        type = "F"
    elif j == 4:
        type = "Q"

    return int(max * 100), type


@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    dataset = pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], 'data'))
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    axis.plot(dataset)
    return fig
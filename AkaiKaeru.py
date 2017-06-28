from flask import Flask
from flask import render_template , request, redirect, url_for, send_from_directory
from DataWrangling import wrangle

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")
import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'C:/Users/mayur/PycharmProjects/AkaiKaeru/uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['csv'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    #print(wrangle('C:/Users/mayur/Downloads/age_specific_fertility_rates.csv'))
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print(wrangle(os.path.join(app.config['UPLOAD_FOLDER'], filename)))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)




if __name__ == '__main__':
    app.run()

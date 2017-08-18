from flask import Flask
from flask import render_template , request, redirect, url_for, send_from_directory, jsonify
from DataWrangling import wrangle
import json
import pandas as pd

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")
import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = app.root_path+'/Data'
app.config['ALLOWED_EXTENSIONS'] = set(['csv'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    #print(wrangle('C:/Users/mayur/Downloads/age_specific_fertility_rates.csv'))
    return render_template('index.html')


@app.route('/upload', methods=['GET','POST'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        topFeatures, groupedFeatures = wrangle(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print(topFeatures)
        return jsonify(topFeatures=topFeatures, groupedFeatures=groupedFeatures)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


def parseCsv():
    l1 = set(open('C:/Users/mayur/PycharmProjects/AkaiKaeru/Data/Columns1.csv'))
    l2 = set(open('C:/Users/mayur/PycharmProjects/AkaiKaeru/Data/Columns2.csv'))
    open('C:/Users/mayur/PycharmProjects/AkaiKaeru/Data/Columns31.csv','w').writelines(l1 & l2)

def mergeCsv():
    df = pd.read_csv('C:/Users/mayur/PycharmProjects/AkaiKaeru/Data/BlankCount1.csv')
    df2 = pd.read_csv('C:/Users/mayur/PycharmProjects/AkaiKaeru/Data/Columns31.csv')
    df3 = pd.read_csv('C:/Users/mayur/PycharmProjects/AkaiKaeru/Data/BlankCount2.csv')
    s1 = pd.merge(df,df2,how='inner', on='Institution Name')
    s2 = pd.merge(df2,df3,how='inner', on='Institution Name')
    s1.to_csv('C:/Users/mayur/PycharmProjects/AkaiKaeru/Data/MergedBlankCount1.csv')
    s2.to_csv('C:/Users/mayur/PycharmProjects/AkaiKaeru/Data/MergedBlankCount2.csv')

if __name__ == '__main__':
    #parseCsv()
    #mergeCsv()
    app.run()

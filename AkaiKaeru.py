from flask import Flask
from flask import render_template , request, redirect, url_for, send_from_directory, jsonify
from DataWrangling import wrangle
import json
import pandas as pd
import numpy as np


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

@app.route('/attributes', methods=['GET','POST'])
def attributeSet():
    if request.method == "POST":
        attributes = request.data
        createCSV(attributes)
        #print(json.dumps(attributes))
        return "hi"


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

def readCSV():
    df1 = pd.read_csv(app.root_path+'/Data/College_Data_Oct_17.csv', encoding='iso-8859-1')
    df2 = pd.read_csv(app.root_path+'/Data/PayScale.csv', encoding='iso-8859-1')
    result = pd.merge(df1, df2, how='left', on=['Institution Name'])
    result.to_csv(app.root_path+'/Data/College_Data_Oct_17_Updated.csv')
    # df3 = pd.read_csv(app.root_path + '/Data/CD_Final1.csv')
    # df4 = pd.read_csv(app.root_path+'/Data/Need_Blind.csv')
    # result2 = pd.merge(df3, df4, how='left', on=['Institution Name'])
    # result2.to_csv(app.root_path + '/Data/CD_Final.csv')

def blankCount():
    #(128 Columns)
    df = pd.read_csv(app.root_path + '/Data/College_Data_Oct_20_1.csv', encoding='iso-8859-1')
    df["Blank_Count"] = df.isnull().sum(axis=1).tolist()
    df.to_csv(app.root_path + '/Data/College_Data_Oct_20_2.csv')
    print(df["Blank_Count"])

def SatAct():
    df = pd.read_csv(app.root_path + '/Data/College_Data_Oct_20.csv', encoding='iso-8859-1')
    # df['SAT Critical Reading 25th percentile score (ADM2015)'].fillna(0,inplace=True)
    # df['SAT Critical Reading 75th percentile score (ADM2015)'].fillna(0,inplace=True)
    # df['SAT Math 25th percentile score (ADM2015)'].fillna(0,inplace=True)
    # df['SAT Math 75th percentile score (ADM2015)'].fillna(0,inplace=True)
    # df['SAT Writing 25th percentile score (ADM2015)'].fillna(0,inplace=True)
    # df['SAT Writing 75th percentile score (ADM2015)'].fillna(0,inplace=True)
    # df['ACT Composite 25th percentile score (ADM2015)'].fillna(0,inplace=True)
    # df['ACT Composite 75th percentile score (ADM2015)'].fillna(0,inplace=True)
    # df['ACT Writing 25th percentile score (ADM2015)'].fillna(0,inplace=True)
    # df['ACT Writing 75th percentile score (ADM2015)'].fillna(0,inplace=True)
    # df['ACT English 25th percentile score (ADM2015)'].fillna(0,inplace=True)
    # df['ACT English 75th percentile score (ADM2015)'].fillna(0,inplace=True)
    # df['ACT Math 25th percentile score (ADM2015)'].fillna(0,inplace=True)
    # df['ACT Math 75th percentile score (ADM2015)'].fillna(0,inplace=True)
    #
    #
    #
    # df['SAT 25th percentile'] = df['SAT Critical Reading 25th percentile score (ADM2015)'] + df['SAT Math 25th percentile score (ADM2015)'] + df['SAT Writing 25th percentile score (ADM2015)']
    # df['SAT 75th percentile'] = df['SAT Critical Reading 75th percentile score (ADM2015)'] + df['SAT Math 75th percentile score (ADM2015)'] + df['SAT Writing 75th percentile score (ADM2015)']
    # df['ACT 25th percentile'] = df['ACT Composite 25th percentile score (ADM2015)'] + df['ACT Writing 25th percentile score (ADM2015)'] + df['ACT English 25th percentile score (ADM2015)']+ df['ACT Math 25th percentile score (ADM2015)']
    # df['ACT 75th percentile'] = df['ACT Composite 75th percentile score (ADM2015)'] + df['ACT Writing 75th percentile score (ADM2015)'] + df['ACT English 75th percentile score (ADM2015)']+ df['ACT Math 75th percentile score (ADM2015)']

    df['SAT 25th percentile'] = df['SAT 25th percentile'].replace(0, np.nan)
    df['SAT 75th percentile'] = df['SAT 75th percentile'].replace(0, np.nan)
    df['ACT 25th percentile'] = df['ACT 25th percentile'].replace(0, np.nan)
    df['ACT 75th percentile'] = df['ACT 75th percentile'].replace(0, np.nan)


    df.to_csv(app.root_path + '/Data/College_Data_Oct_20_1.csv')
    print('donbe')


def removeNumsFromInstitutionName():
    df = pd.read_csv(app.root_path + '/Data/Testing_opt100.csv')
    df['Institution Name'] = df['Institution Name'].str.replace('\d+', '')
    df.to_csv(app.root_path + '/Data/Testing_optional1.csv')

def mergeTestingOp():
    df1 = pd.read_csv(app.root_path + '/Data/CD_Final1.csv',encoding='iso-8859-1')
    df2 = pd.read_csv(app.root_path+'/Data/Testing_optional1.csv')
    result2 = pd.merge(df1, df2, how='left', on=['Institution Name'])
    result2.to_csv(app.root_path + '/Data/CD_Final2.csv')


def editUniversity():
    df = pd.read_csv(app.root_path + '/Data/ranking.csv', encoding='iso-8859-1')
    df = df.dropna()
    df.to_csv(app.root_path + '/Data/ranking1.csv')

def addRanking():
    df1 = pd.read_csv(app.root_path + '/Data/College_Data_Nov_2.csv', encoding='iso-8859-1')
    df2 = pd.read_csv(app.root_path + '/Data/ranking1.csv', encoding='iso-8859-1')
    result2 = pd.merge(df1, df2, how='left', on=['Institution Name'])
    result2.to_csv(app.root_path + '/Data/College_Data_Nov_4.csv')

def addLivability():
    df1 = pd.read_csv(app.root_path + '/Data/College_Data_Oct_20_700.csv', encoding='iso-8859-1')
    df2 = pd.read_csv(app.root_path + '/Data/Livability.csv', encoding='iso-8859-1')
    result2 = pd.merge(df1, df2, how='left', on=['City location of institution'])
    result2.to_csv(app.root_path + '/Data/College_Data_Nov_2.csv')

def getTop():
    df = pd.read_csv(app.root_path + '/Data/College_Data_Nov_4.csv', encoding='iso-8859-1')
    df_subset = df.head(700)
    df_subset.to_csv(app.root_path + '/Data/College_Data_Nov_15.csv')

def missingValues():
    df = pd.read_csv(app.root_path + '/Data/College_Data_Nov_15.csv', encoding='iso-8859-1')
    for column in df:
        count_nan = len(df[column]) - df[column].count()
        print(column + " : " + str(count_nan))

def filterDatasets():
    df = pd.read_csv(app.root_path + '/Data/College_Data_Nov_15.csv', encoding='iso-8859-1')
    for column in df:
        count_nan = len(df[column]) - df[column].count()
        print(column + " : " + str(count_nan))
        if count_nan > 100:
            print("yes!!")
            df = df.drop([column], axis=1)
    df.to_csv(app.root_path + '/Data/College_Data_Nov_22.csv', index=False)

def fillWithMean():
    df = pd.read_csv(app.root_path + '/Data/College_Data_Nov_22_1.csv', encoding='iso-8859-1')
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    for column in df:
        if df[column].dtype in numerics:
            df[column] = df[column].fillna(df[column].mean())
    df.to_csv(app.root_path + '/Data/College_Data_Nov_22_1.csv', index=False)

def dropRows():
    df = pd.read_csv(app.root_path + '/Data/File2.csv')
    df = df[df["Blank Count"] < 11]
    df.to_csv(app.root_path + '/Data/College_Data_Nov_22_2.csv', index=False)

def updateFile2():
    df1 = pd.read_csv(app.root_path + '/Data/College_Data_Nov_22_2.csv', encoding='iso-8859-1')
    df2 = pd.read_csv(app.root_path + '/Data/College_Data_Nov_22_1.csv', encoding='iso-8859-1')
    df = pd.merge(df1, df2, how='inner', on='Institution Name')
    df.to_csv(app.root_path + '/Data/College_Data_Nov_27_2_Updated.csv', index=False)

def createLivabilityFile():
    df = pd.read_csv(app.root_path + '/Data/College_Data_Nov_27_2_Updated1.csv', encoding='iso-8859-1')
    df = df[df["Blank Count"] < 10]
    df.to_csv(app.root_path + '/Data/College_Data_Livability.csv', index=False)

def createClassSizeFile():
    df = pd.read_csv(app.root_path + '/Data/College_Data_Nov_27_2_Updated.csv', encoding='iso-8859-1')
    df = df[df["Average Class Size"].notnull()]
    df.to_csv(app.root_path + '/Data/College_Data_ClassSize.csv', index=False)



def addIndices():
    df1 = pd.read_csv(app.root_path + '/Data/College_Data_ClassSize.csv', encoding='iso-8859-1')
    df2 = pd.read_csv(app.root_path + '/CSV/DivIndices.csv', encoding='iso-8859-1')
    result = pd.merge(df1, df2, how='left', on=['Institution Name'])
    result.to_csv(app.root_path + '/CSV/College_Data_ClassSize_Indices.csv')

def getColumnNames():
    df = pd.read_csv(app.root_path + '/Data/College_Data_Final_Div_InOutState.csv', encoding='iso-8859-1')
    print(df.columns)

def diversityIndexAdmissions():
    df = pd.read_csv(app.root_path + '/CSV/College_Data_Final_Dec6_1.csv', encoding='iso-8859-1')
    N = df['Admissions men (ADM2015)'] + df['Total men (EF2015  All students  Undergraduate total)']
    n1 = df['Admissions men (ADM2015)'] * (df['Admissions men (ADM2015)'] - 1)
    n2 = df['Admissions women (ADM2015)'] * (df['Admissions women (ADM2015)'] - 1)
    numer = n1 + n2
    den = N * (N - 1)
    df['AdmissionsDiversityIndex'] = 1- (numer/ den)
    print(df['AdmissionsDiversityIndex'])

    N = df['Applicants men (ADM2015)'] + df['Applicants women (ADM2015)']
    n1 = df['Applicants men (ADM2015)'] * (df['Applicants men (ADM2015)'] - 1)
    n2 = df['Applicants women (ADM2015)'] * (df['Applicants women (ADM2015)'] - 1)
    numer = n1 + n2
    den = N * (N - 1)
    df['ApplicantsDiversityIndex'] = 1 - (numer / den)
    print(df['ApplicantsDiversityIndex'])

    df.to_csv(app.root_path + '/Data/College_Data_Final_Dec6_2.csv', index=False)


def diversityIndexAge():
    df = pd.read_csv(app.root_path + '/Data/College_Data_Final.csv', encoding='iso-8859-1')
    N = df['Grand total (EF2015B  Undergraduate  Age under 25 total)'] + df['Grand total (EF2015B  Undergraduate  Age 25 and over total)']
    n1 = df['Grand total (EF2015B  Undergraduate  Age under 25 total)'] * (df['Grand total (EF2015B  Undergraduate  Age under 25 total)'] - 1)
    n2 = df['Grand total (EF2015B  Undergraduate  Age 25 and over total)'] * (df['Grand total (EF2015B  Undergraduate  Age 25 and over total)'] - 1)
    numer = n1 + n2
    den = N * (N - 1)
    df['AgeDiversityIndex'] = 1- (numer/ den)
    print(df['AgeDiversityIndex'])
    df.to_csv(app.root_path + '/Data/College_Data_Final_DivAge.csv', index=False)

def diversityIndexGender():
    df = pd.read_csv(app.root_path + '/Data/College_Data_Final_DivAge.csv', encoding='iso-8859-1')
    N = df['Total women (EF2015  All students  Undergraduate total)'] + df['Total men (EF2015  All students  Undergraduate total)']
    n1 = df['Total women (EF2015  All students  Undergraduate total)'] * (df['Total women (EF2015  All students  Undergraduate total)'] - 1)
    n2 = df['Total men (EF2015  All students  Undergraduate total)'] * (df['Total men (EF2015  All students  Undergraduate total)'] - 1)
    numer = n1 + n2
    den = N * (N - 1)
    df['GenderDiversityIndex'] = 1- (numer/ den)
    print(df['GenderDiversityIndex'])
    df.to_csv(app.root_path + '/Data/College_Data_Final_DivGender.csv', index=False)

def diversityIndexRace():
    df = pd.read_csv(app.root_path + '/Data/College_Data_Final_DivGender.csv', encoding='iso-8859-1')
    n1 = df['American Indian or Alaska Native total (EF2015A  All students total)'] * (df['American Indian or Alaska Native total (EF2015A  All students total)'] - 1)
    n2 = df['Asian total (EF2015A  All students total)'] * (df['Asian total (EF2015A  All students total)'] - 1)
    n3 = df['Black or African American total (EF2015A  All students total)'] * (df['Black or African American total (EF2015A  All students total)'] - 1)
    n4 = df['Hispanic total (EF2015A  All students total)'] * (df['Hispanic total (EF2015A  All students total)'] - 1)
    n5 = df['Native Hawaiian or Other Pacific Islander total (EF2015A  All students total)'] * (df['Native Hawaiian or Other Pacific Islander total (EF2015A  All students total)'] - 1)
    n6 = df['White total (EF2015A  All students total)'] * (df['White total (EF2015A  All students total)'] - 1)
    n7 = df['Race/ethnicity unknown total (EF2015A  All students total)'] * (df['Race/ethnicity unknown total (EF2015A  All students total)'] - 1)
    n8 = df['Nonresident alien total (EF2015A  All students total)'] * (df['Nonresident alien total (EF2015A  All students total)'] - 1)
    N = df['American Indian or Alaska Native total (EF2015A  All students total)'] + df['Asian total (EF2015A  All students total)'] + \
        df['Black or African American total (EF2015A  All students total)'] + df['Hispanic total (EF2015A  All students total)'] +  \
        df['Native Hawaiian or Other Pacific Islander total (EF2015A  All students total)'] + df['White total (EF2015A  All students total)'] + \
        df['Two or more races total (EF2015A  All students total)'] + df['Race/ethnicity unknown total (EF2015A  All students total)'] + \
        df['Nonresident alien total (EF2015A  All students total)']
    numer = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
    den = N * (N - 1)
    df['RaceDiversityIndex'] = 1 - (numer / den)
    print(df['RaceDiversityIndex'])
    df.to_csv(app.root_path + '/Data/College_Data_Final_DivRace.csv', index=False)

def IncomeDivIndex():
    df = pd.read_csv(app.root_path + '/Data/College_Data_Final_DivRace.csv', encoding='iso-8859-1')
    N = df['Early Career($)'] + df['Mid-Career($)']
    n1 = df['Early Career($)'] * (df['Early Career($)'] - 1)
    n2 = df['Mid-Career($)'] * (df['Mid-Career($)'] - 1)
    numer = n1 + n2
    den = N * (N - 1)
    df['IncomeDiversityIndex'] = 1 - (numer / den)
    print(df['IncomeDiversityIndex'])
    df.to_csv(app.root_path + '/Data/College_Data_Final_DivIncome.csv', index=False)

def MajorDivIndex():
    df = pd.read_csv(app.root_path + '/Data/College_Data_Final_DivIncome.csv', encoding='iso-8859-1')
    r1 = df["Grand total men (C2016_A  First major  Communication  Journalism  and Related Programs  Bachelor's degree)"] + df["Grand total women (C2016_A  First major  Communication  Journalism  and Related Programs  Bachelor's degree)"]
    r2 = df["Grand total men (C2016_A  First major  Computer and Information Sciences and Support Services  Bachelor's degree)"] + df["Grand total women (C2016_A  First major  Computer and Information Sciences and Support Services  Bachelor's degree)"]
    r3 = df["Grand total men (C2016_A  First major  Foreign Languages  Literatures  and Linguistics  Bachelor's degree)"] + df["Grand total women (C2016_A  First major  Foreign Languages  Literatures  and Linguistics  Bachelor's degree)"]
    r4 = df["Grand total men (C2016_A  First major  Biological and Biomedical Sciences  Bachelor's degree)"] + df["Grand total women (C2016_A  First major  Biological and Biomedical Sciences  Bachelor's degree)"]
    r5 = df["Grand total men (C2016_A  First major  Mathematics and Statistics  Bachelor's degree)"] + df["Grand total women (C2016_A  First major  Mathematics and Statistics  Bachelor's degree)"]
    r6 = df["Grand total men (C2016_A  First major  Physical Sciences  Bachelor's degree)"] + df["Grand total women (C2016_A  First major  Physical Sciences  Bachelor's degree)"]
    r7 = df["Grand total men (C2016_A  First major  Psychology  Bachelor's degree)"] + df["Grand total women (C2016_A  First major  Psychology  Bachelor's degree)"]
    r8 = df["Grand total men (C2016_A  First major  Social Sciences  Bachelor's degree)"] + df["Grand total women (C2016_A  First major  Social Sciences  Bachelor's degree)"]
    r9 = df["Grand total men (C2016_A  First major  Visual and Performing Arts  Bachelor's degree)"] + df["Grand total women (C2016_A  First major  Visual and Performing Arts  Bachelor's degree)"]
    r10 = df["Grand total men (C2016_A  First major  Health Professions and Related Programs  Bachelor's degree)"] + df["Grand total women (C2016_A  First major  Health Professions and Related Programs  Bachelor's degree)"]
    r11 = df["Grand total men (C2016_A  First major  Business  Management  Marketing  and Related Support Services  Bachelor's degree)"] + df["Grand total women (C2016_A  First major  Business  Management  Marketing  and Related Support Services  Bachelor's degree)"]
    r12 = df["Grand total men (C2016_A  First major  History  Bachelor's degree)"] + df["Grand total women (C2016_A  First major  History  Bachelor's degree)"]

    N = r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8 + r9 + r10 + r11 + r12
    n1 = r1 * (r1 - 1)
    n2 = r2 * (r2 - 1)
    n3 = r3 * (r3 - 1)
    n4 = r4 * (r4 - 1)
    n5 = r5 * (r5 - 1)
    n6 = r6 * (r6 - 1)
    n7 = r7 * (r7 - 1)
    n8 = r8 * (r8 - 1)
    n9 = r9 * (r9 - 1)
    n10 = r10 * (r10 - 1)
    n11 = r11 * (r11 - 1)
    n12 = r12 * (r12 - 1)
    numer = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10 + n11 + n12
    den = N * (N - 1)
    df['MajorDiversityIndex'] = 1 - (numer / den)
    print(df['MajorDiversityIndex'])
    df.to_csv(app.root_path + '/Data/College_Data_Final_DivMajor.csv', index=False)

def SATACTIndex():
    df = pd.read_csv(app.root_path + '/Data/College_Data_Final_DivMajor.csv', encoding='iso-8859-1')
    r1 = df["SAT 25th percentile"] + df["SAT 75th percentile"]
    r2 = df["ACT 25th percentile"] + df["ACT 75th percentile"]
    N = r1 + r2
    n1 = r1 * (r1 - 1)
    n2 = r2 * (r2 - 1)
    numer = n1 + n2
    den = N * (N - 1)
    df['SAT_ACT_DiversityIndex'] = 1 - (numer / den)
    print(df['SAT_ACT_DiversityIndex'])
    df.to_csv(app.root_path + '/Data/College_Data_Final_Div_SAT_ACT.csv', index=False)


def diversityIndexInstateOutstate():
    df = pd.read_csv(app.root_path + '/Data/College_Data_Final_Div_SAT_ACT.csv', encoding='iso-8859-1')
    N = df['Total price for in-state students living on campus 2016-17 (DRVIC2016)'] + df['Total price for out-of-state students living on campus 2016-16 (DRVIC2016)']
    n1 = df['Total price for in-state students living on campus 2016-17 (DRVIC2016)'] * (df['Total price for in-state students living on campus 2016-17 (DRVIC2016)'] - 1)
    n2 = df['Total price for out-of-state students living on campus 2016-16 (DRVIC2016)'] * (df['Total price for out-of-state students living on campus 2016-16 (DRVIC2016)'] - 1)
    numer = n1 + n2
    den = N * (N - 1)
    df['InstateOutstateDiversityIndex'] = 1- (numer/ den)
    print(df['InstateOutstateDiversityIndex'])
    df.to_csv(app.root_path + '/Data/College_Data_Final_Div_InOutState.csv', index=False)

def avgGraduation():
    df = pd.read_csv(app.root_path + '/Data/College_Data_Final_Div_InOutState.csv', encoding='iso-8859-1')
    n8 = df["8-year Graduation rate - bachelor's degree within 200% of normal time (GR200_15)"]
    n6 = df["6-year Graduation rate - bachelor's degree within 150% of normal time (GR200_15)"]
    n4 = df["4-year Graduation rate - bachelor's degree within 100% of normal time (GR200_15)"]

    df["Average Graduation rate - bachelor's degree within 200% of normal time (GR200_15)"] = n8 + n6 + n4
    df.to_csv(app.root_path + '/Data/College_Data_Final_Dec6_1.csv', index=False)

def createCSV(attributes):
    obj = json.loads(attributes.decode('utf-8'))

    womenFlag = False
    if obj['gender'] == 'Female':
        obj['sex'] = 'women'
        womenFlag = True
    else:
        obj['sex'] = 'men'

    selectedAttrs = []
    for key, value in obj.items():
        selectedAttrs.append(value.lower())
    df = pd.read_csv(app.root_path + '/CSV/College_Data_Final_Dec6_2.csv', encoding='iso-8859-1')
    columnsToAdd = []
    for column in df.columns:
        for attr in  selectedAttrs:
            if attr in column.lower() and 'index' not in column.lower():
                if not womenFlag:
                    if 'women' not in column.lower():
                        if "Bachelor's degree" in column and column not in columnsToAdd:
                            if  obj['major'] in column:
                                columnsToAdd.append(column)
                            elif obj['race'] in column:
                                columnsToAdd.append(column)
                        elif column not in columnsToAdd:
                            columnsToAdd.append(column)
                else:
                    if "Bachelor's degree" in column and column not in columnsToAdd:
                        if obj['major'] in column:
                            columnsToAdd.append(column)
                        elif obj['race'] in column:
                            columnsToAdd.append(column)
                    elif column not in columnsToAdd:
                        columnsToAdd.append(column)
    columnsToAdd.append('Institution Name')
    #print(columnsToAdd)
    new_df = df[columnsToAdd]
    print(new_df.columns)
    df1 = pd.read_csv(app.root_path + '/CSV/College_Data_Basic.csv', encoding='iso-8859-1')
    df2 = pd.read_csv(app.root_path + '/CSV/College_Data_Basic_Livability.csv', encoding='iso-8859-1')
    df3 = pd.read_csv(app.root_path + '/CSV/College_Data_Basic_ClassSize.csv', encoding='iso-8859-1')
    #print(df1.columns)
    result1 = pd.merge(df1, new_df, how='outer', on=['Institution Name'])
    result2 = pd.merge(df2, new_df, how='outer', on=['Institution Name'])
    result3 = pd.merge(df3, new_df, how='outer', on=['Institution Name'])
    result1.to_csv(app.root_path + '/Test/College_Data_Dec7_Selected1.csv',index=False)
    result2.to_csv(app.root_path + '/Test/College_Data_Dec7_Selected2.csv', index=False)
    result3.to_csv(app.root_path + '/Test/College_Data_Dec7_Selected3.csv', index=False)
    #print(new_df.columns)
    return

if __name__ == '__main__':
    #parseCsv()
    #mergeCsv()
    #readCSV()
    #removeNumsFromInstitutionName()
    #mergeTestingOp()
    #readCSV()
    #blankCount()
    #SatAct()
    #editUniversity()
    #addRanking()
    #addLivability()
    #addRanking()
    #calculateResult(0)
    #missingValues()
    #filterDatasets()
    #fillWithMean()
    #dropRows()
    #createClassSizeFile()
    #getColumnNames()
    #diversityIndexAge()
    #diversityIndexGender()
    #diversityIndexRace()
    #IncomeDivIndex()
    #MajorDivIndex()
    #SATACTIndex()
    #diversityIndexInstateOutstate()
    #avgGraduation()
    #addIndices()
    #diversityIndexAdmissions()
    #createCSV('hi')
    app.run()

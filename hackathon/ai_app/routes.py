from ai_app import app
from flask import Flask, request, render_template, Response, redirect, url_for
import json
from wtforms import StringField, Form, SubmitField
import pandas as pd
from ai_app.model import predict_gpa

df = pd.read_csv('results.csv')
courses = df["course"].unique().tolist()
profs = df["prof"].unique().tolist() # seems like there's a limit to length of list for autocomplete.
# profs = ["banana","apple"]



class SearchForm(Form):
    course = StringField('Course', id='course_autocomplete', 
                         render_kw={'class':'form-control', 
                                    'style':'margin-bottom: 8px;',
                                    'placeholder':'CHEM181'})
    prof = StringField('Professor', id='prof_autocomplete', 
                         render_kw={'class':'form-control', 
                                    'style':'margin-bottom: 8px;',
                                    'placeholder':'Lastname, Firstname'})
    completed_credits = StringField('Completed Credits', id='completed_credits', 
                                    render_kw={'class':'form-control', 
                                    'style':'margin-bottom: 8px;',
                                    'placeholder':'55'})
    gpa = StringField('GPA', id='gpa', 
                                    render_kw={'class':'form-control', 
                                    'style':'margin-bottom: 8px;',
                                    'placeholder':'4.0'})


@app.route('/_autocompletecourse', methods=['GET'])
def autocomplete_course():
    return Response(json.dumps(courses), mimetype='application/json')

@app.route('/_autocompleteprof', methods=['GET'])
def autocomplete_prof():
    return Response(json.dumps(profs), mimetype='application/json')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm(request.form)
    print(len(courses))
    if request.method == "POST":
        if request.form['submit_button'] == 'select':
            course = request.form["course"]
            prof = request.form["prof"]
            try:
                app.config['completed_credits'] = float(request.form["completed_credits"])
            except:
                app.config['completed_credits'] = 0

            try:
                app.config['gpa'] = float(request.form["gpa"])
            except:
                app.config['gpa'] = 0
            if course not in app.config["selections"] and course in courses: 
                app.config["selections"].append(course)
                app.config["profs"].append(prof)
            return render_template("index.html", form=form, 
                                   selections=app.config["selections"],
                                   profs=app.config["profs"])
        if request.form['submit_button'] == 'reset':
            app.config["selections"] = []
            app.config["profs"] = []
            app.config["completed_credits"] = 0
            app.config["gpa"] = 0
        if request.form['submit_button'] == 'calculate':
            predicted_gpa = predict_gpa(app.config['gpa'], 
                                        app.config['completed_credits'],
                                        app.config['selections'],
                                        app.config['profs'])
            predicted_gpa = round(predicted_gpa, 2)
            return render_template("index.html", form=form, selections=app.config["selections"], profs=app.config["profs"], predicted_gpa=predicted_gpa)
            # return redirect(url_for('results', predicted_gpa = predicted_gpa))
    return render_template("index.html", form=form)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/process', methods=['POST'])
def process():
    data = request.form.get('data')
    # process the data using Python code
    result = data.upper()
    return result

@app.route('/results/<predicted_gpa>')
def results(predicted_gpa):
    return render_template('results.html', gpa=predicted_gpa)
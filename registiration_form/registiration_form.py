
from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    session['email']= request.form['email']
    session['first_name']= request.form['first_name']
    session['last_name']= request.form['last_name']
    counter = 0
    if len(request.form['email'])<1:
        flash("An email must be provided!")
        counter +=1
    # if not EMAIL_REGEX.match(request.form['email']):
    #     flash("Invalid Email Address!")
    if len(request.form['first_name'])<1:
        flash("A first name must be provided!")
        counter +=1
    if len(request.form['last_name'])<1:
        flash("A last name must be provided!")
        counter +=1
    if len(request.form['password']) <8:
        flash("Password must contain at least 8 characters!")
        counter +=1
    if request.form['confirm_password'] != request.form['password']:
        flash("Password and password confirmation does not match")
        counter +=1
    if counter == 0:
        flash('Thanks!')

    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
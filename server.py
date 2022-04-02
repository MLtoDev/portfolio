from email import message
from flask import Flask, render_template, url_for, request, redirect
import csv 

app = Flask(__name__)

@app.route('/') #home 
def my_home():
    return render_template('./index.html') 

@app.route('/<string:page_name>')  
def html_page(page_name):
    return render_template(page_name) 

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n {email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',
         quotechar = '"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


#Creating a contact page for users to submit their details
#https://flask.palletsprojects.com/en/1.1.x/quickstart/#accessing-request-data

@app.route('/submit_form', methods=['POST', 'GET']) #POST = browser want us to save info ; GET = browser wants us to send information
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict() #add data to a dictionary
            write_to_csv(data)
            return redirect('/thankyou.html') # redirect to thankyou.html
        except:
            'did not save to database'
    else:
        'something went wrong. Try again'


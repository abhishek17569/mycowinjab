from flask import Flask, render_template, request, redirect, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from today_date import today_date
from datetime import datetime
import requests
import json
import logging
import sys


app = Flask(__name__, static_url_path="", static_folder="static")
#app._static_folder = "/flaskenv/static"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    age = db.Column(db.String(60), nullable=False)
    phone = db.Column(db.String(20),unique=True, nullable=False)
    email = db.Column(db.String(60),unique=True, nullable=False)
    district = db.Column(db.String(50), nullable=False)
    pincode = db.Column(db.String(10), nullable=False)
    avail = db.Column(db.Boolean, nullable=False)
    data = db.Column(db.String(50),nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.name}"

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    response = ''
    age_limit=0
    if request.method=='POST':
        name = request.form['name']
        age = request.form['age']
        phone = request.form['phone']
        email = request.form['email']
        district =request.form['district']
        pincode  =request.form['pincode']
        #todo = Todo(name=name, phone=phone,age = age, email=email,district= district,pincode=pincode,data="NA")
        
        ##########api request########
        #print(pincode)
        # print(type(pincode))
        params = (
            ('pincode', pincode),
            ('date', today_date()),
        )
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        }
        
        response = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin', headers=headers, params=params)
        print(response.text)
        response = response.text  # RESPONSE TEXT WITHOUT STATUS CODE
        dic = json.loads(response)
        vaccine = 0
        response = dic
        ##### scraping data from Api response ####
        centre = dic["centers"]
        # print(type(centre))
        for li in centre:
            # print(type(li))
            print("Centre Name:", li['name'], "\nCentre Address:", li['address'], li['block_name'], li['district_name'], li['pincode'],"\nFee Type:",li['fee_type']) #, li["'sessions'"][0]['date'], li["'sessions'"][0]['date'], li["'sessions'"][0]['available_capacity'], li["'sessions'"][0]['min_age_limit'])
            # print(li[""'sessions'""])
            print("Date        Availability    Minimum Age   Vaccine")
            for session in li["sessions"]:
                print(session['date'],"      ", session['available_capacity'],"        ", session['min_age_limit'],"            ", session['vaccine'])
                vaccine=vaccine+session['available_capacity']
                age_limit = session['min_age_limit']     
        #avail=bool(1)
        #print(age_limit)
        if(int(age) > age_limit & vaccine > 0 ):
            avail=bool(1)
        else:
            avail=bool(0)    

        todo = Todo(name=name, phone=phone,age = age, email=email,district= district,pincode=pincode,data="NA",avail= avail)
        if len(centre)==0:                    # check is response if empty/ no centre available
            response={"centers":-1}
        try:
            db.session.add(todo)
            db.session.commit()
        except:
            response= {"centers":-300}   
        
    # allTodo = Todo.query.all() 
    #return render_template('index1.html', allTodo=response) #for check
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.setLevel(logging.ERROR)
    return render_template('index2.html', allTodo=response) # response in json


@app.route('/show')
def products():
    allTodo = Todo.query.all()
    print(allTodo)
    return 'There is nothing to Show'


if __name__ == "__main__":
    app.run(debug=True, port=8000)
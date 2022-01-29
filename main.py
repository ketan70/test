from flask import Flask ,render_template ,request 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import csv

from platformdirs import user_cache_path

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bace.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True
db = SQLAlchemy(app)

## create databace
class basic(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), nullable=False)
    PNO= db.Column(db.Integer,nullable=False)
    FNO = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.sno} - {self.Name}"

class survey(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    SN = db.Column(db.String(80), nullable=False)
    SQ = db.Column(db.String(120), nullable=False)
    SA = db.Column(db.String(120), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.username

class survey_suggesion(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    SSN = db.Column(db.String(80), nullable=False)
    SA = db.Column(db.String(120), nullable=False)
    CA = db.Column(db.String(80), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.username


# create the object


# main code 

@app.route("/")
def hello():
    
    return render_template('front.html')

@app.route("/main",methods=['POST', 'GET'])
def hello_world():
    
    return render_template('main.html')

@app.route("/home", methods=['POST', 'GET'])
def login1():
    if request.method == 'POST':
        name = request.form.get("name")
        PNo = request.form.get("MNO")
        FNo = request.form.get("FNO")
        print(name)
        print(PNo)
        print(FNo)
        admin = basic(Name=name, PNO=PNo,FNO=FNo)
        db.session.add(admin)
        db.session.commit()


    import csv
    pathCSV = "s.csv"
    with open(pathCSV, newline='\n') as f:
        reader = csv.reader(f)
        dataAll = list(reader)[:]
        l=dataAll[0][1:] 
        l2=dataAll[1][1:]

    return render_template('home.html',l=l,l2=l2,)


@app.route("/form",methods=['POST', 'GET'])
def hello_world1():
    if request.method == 'POST':
        select = request.form.get("select")
        print(select)



    import csv
    pathCSV = select + ".csv"
    with open(pathCSV, newline='\n') as f:
        reader = csv.reader(f)
        dataAll = list(reader)[1:]
        l5=dataAll[:]

        print(l5)


    return render_template('form.html',l3=l5,name_survey=select,)


@app.route("/thanks",methods=['POST', 'GET'])
def thanks():
    if request.method == 'POST':
        chek = request.form.get("chek")
        if chek == "on":
            CA = "satisfied"
        else:
            CA = "Unsatisfied"
        select = request.form.get("select")
        sugession = request.form.get("sugession")
        admin = survey_suggesion(SA=sugession, CA=CA,SSN=select)
        db.session.add(admin)
        db.session.commit()

# get how many no of qustion 
    pathCSV = select +".csv"
    print(pathCSV)
    with open(pathCSV, newline='\n') as f:
        reader = csv.reader(f)
        dataAll = list(reader)[1:]
        l5=dataAll
        L = len(l5)
        print(L)

# tacking no of mcq input 
#
    a=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
    print(a)

#
    print("strat")

    i=0
    if request.method == 'POST':
        while (i<=L-1):
            A = request.form.get(a[i])
            select = request.form.get("select")
            QN = a[i]
            admin56 = survey(SN=select, SQ=QN,SA=A)
            db.session.add(admin56)
            db.session.commit()



            print(A)
            i=i+1




#
#
#
#




# total no of survey
    pathCS = "s.csv"
    with open(pathCS, newline='\n') as f:
        reader = csv.reader(f)
        dataAll = list(reader)[:]
        l=dataAll[0][1:]
        al=len(l)
    return render_template('thankyouforsurvey.html',CA=CA, AL=al)












@app.route("/About")
def About():
    
    return render_template('About.html')

@app.route("/contact")
def contact():
    
    return render_template('contact.html')


if __name__ == '__main__':
    app.run( port=8000, debug=True)

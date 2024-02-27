from flask import Flask , render_template,request

app=Flask(__name__)

#---------------------Db-----------------------

import sqlite3

connection=sqlite3.Connection("admin.db")

cursor = connection.cursor()

create_table_query = """CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,Username TEXT NOT NULL,Password TEXT NOT NULL,ConfirmPassword TEXT NOT NULL);
"""
cursor.execute(create_table_query)
connection.commit()
cursor.close()
connection.close()


@app.route('/')
def home():
    return render_template("index.html")  


@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        try:
            username = request.form["Username"]
            password = request.form["Password"]
            cpassword = request.form['ConfirmPassword']
            sqlconnection=sqlite3=sqlite3.connect(admin.db)
            cur=sqlconnection.cursor()
            cur.execute("INSERT INTO users (Username, Password, ConfirmPassword) VALUES (?, ?, ?)")
            sqlconnection.commit()
            flash("record added successfully","success")
        except:
            flash("Error in Insert operation","danger")
        finally:
            return redirect('/login')
            sqlconnection.close()        
                    
        return render_template("signup.html")


@app.route('/login')
def login():
    return render_template("login.html")       

      
@app.route('/AesculusHippocastanum.html')
def AesculusHippocastanum():
    return render_template("AesculusHippocastanum.html")
@app.route('/BetalLeafPlant.html')
def BetalLeafPlant():
    return render_template("BetalLeafPlant.html")
     
@app.route('/Eveningprimroseoil.html')
def Eveningprimroseoil():
    return render_template("Eveningprimroseoil.html")
@app.route('/gingko.html')
def gingko():
    return render_template("gingko.html")
@app.route('/Gulvelplant.html')
def Gulvelplant():
    return render_template("Gulvelplant.html")
@app.route('/keezhanelli.html')
def keezhanelli():
    return render_template("keezhanelli.html")
@app.route('/holymangrove.html')
def holymangrove():
    return render_template("holymangrove.html")    
@app.route('/MultivitaminPlant.html')
def MultivitaminPlant():
    return render_template("MultivitaminPlant.html")
@app.route('/RutaGraveolens.html')
def RutaGraveolens():
    return render_template("RutaGraveolens.html")
   
@app.route('/Sambucus.html')
def Sambucus():
    return render_template("Sambucus.html")
@app.route('/Terminalia.html')
def Terminalia():
    return render_template("Terminalia.html")
@app.route('/Rose.html')
def Rose():
    return render_template("Rose.html")
@app.route('/Marigold.html')
def Marigold():
    return render_template("Marigold.html")
@app.route('/Lavanda.html')
def Lavanda():
    return render_template("Lavanda.html")
@app.route('/Jasmine.html')
def Jasmine():
    return render_template("Jasmine.html")
@app.route('/Hibiscus.html')
def Hibiscus():
    return render_template("Hibiscus.html")
@app.route('/herbalplants.html')
def herbalplants():
    return render_template("herbalplants.html")            
@app.route('/flowers.html')
def flowers():
    return render_template("flowers.html")
@app.route('/Echinacea.html')
def Echinacea():
    return render_template("Echinacea.html")
@app.route('/contact.html')
def contact():
    return render_template("contact.html")
@app.route('/checkout.html')
def checkout():
    return render_template("checkout.html")
@app.route('/chamomile.html')
def chamomile():
    return render_template("chamomile.html")
@app.route('/Calendula.html')
def Calendula():
    return render_template("Calendula.html")                                
if __name__=="__main__":
    app.run(debug=True)                                     

from flask import Flask , render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")        
@app.route('/AesculusHippocastanum.html')
def AesculusHippocastanum():
    return render_template("AesculusHippocastanum.html")
@app.route('/BetalLeafPlant.html')
def BetalLeafPlant():
    return render_template("BetalLeafPlant.html")
@app.route('/login.html')
def login():
    return render_template("login.html")        
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
@app.route('/signup.html')
def signup():
    return render_template("signup.html")        
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

import pickle
from flask import Flask, render_template,request as req

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route("/",methods=["GET"])
def some():
    return render_template("home.html")

@app.route("/",methods=["POST"])
def hello():
    ram = float(req.form['ram'])
    hdd = float(req.form['hdd'])
    ssd = float(req.form['ssd'])
    flash = float(req.form['flash'])
    hybrid = float(req.form['hybrid'])
    predict = model.predict([[ram,hdd,ssd,flash,hybrid]])

    predict = round(predict[0],2)
    return render_template("home.html",price=predict,ram=ram,hdd=hdd,ssd=ssd,flash=flash,hybrid=hybrid)
    

if __name__ == "__main__":
    app.run(host='0.0.0.0')

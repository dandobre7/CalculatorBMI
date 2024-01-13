from doctest import debug
from flask import Flask, render_template, request 

app=Flask(__name__)


def calcul_bmi(greutate, inaltime):
    bmi=greutate*10000/(inaltime * inaltime)
    return round(bmi,2)

def interpretare_bmi(bmi):
    if bmi<18.5:
        return "Subponderal"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Supraponderal"
    elif 30 <= bmi < 34.9:
        return "Obezitate clasa I"
    elif 35 <= bmi < 39.9:
        return "Obezitate clasa II"
    else:
        return "Obezitate clasa III"

def sfaturi_bmi(bmi):
    if bmi < 18.5:
        return " Consultă un nutriționist pentru a elabora un plan alimentar sănătos, încearcă să mănânci alimente bogate in proteine și grăsimi sănătoase, dar nu în ultimul rând încearcă să faci mai multe exerciții fizice pentru a-ți crește masa musculară."
    elif 18.5 <= bmi < 24.9:
        return "Continuă să menții un stil de viață sănătos cu o dietă echilibrată și exerciții fizice regulate."
    elif 25 <= bmi < 29.9:
        return " Incearcă să faci cât mai multe exerciții fizice și să reduci alimentele bogate in calorii."
    else:
        return "Indicele BMI este foarte ridicat, consultă un nutriționist pentru a elabora un plan alimentar sănătos, încearcă să reduci alimentele bogate in calorii și începe un program regulat de exerciții fizice."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rezultat', methods=['POST'])
def rezultat():
    inaltime=float(request.form['inaltime'])
    greutate=float(request.form['greutate'])
    bmi=calcul_bmi(greutate, inaltime)
    interpretare=interpretare_bmi(bmi)
    sfaturi=sfaturi_bmi(bmi)
    return render_template('rezultat.html',bmi=bmi,interpretare=interpretare,sfaturi=sfaturi)

if __name__=='__main__':
    app.run(debug=True)
    


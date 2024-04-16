from flask import Flask, render_template, request, session
import sqlite3 as lite

app = Flask(__name__)
app.secret_key = 'your_secret_key'

type_voiture = ["CLF", "CLO", "CCF", "CCO"]

@app.route('/')
def index():
    return render_template('Code.html')

@app.route('/Code', methods=['POST'])
def Code():
    return render_template('Code.html')

@app.route('/CLF', methods=['POST'])
def CLF():
    # Code pour gérer la sélection de CLF
    global a
    a = type_voiture[0]
    print(a)
    return render_template('CLF.html')

@app.route('/CLO', methods=['POST'])
def CLO():
    # Code pour gérer la sélection de CLO
    global a
    a = type_voiture[1]
    print(a)
    return render_template('CLO.html')

@app.route('/CCO', methods=['POST'])
def CCO():
    # Code pour gérer la sélection de CCO
    global a
    a = type_voiture[2]
    print(a)
    return render_template('CCO.html')
@app.route('/CCF', methods=['POST'])
def CCF():
    # Code pour gérer la sélection de CCF
    global a
    a = type_voiture[3]
    print(a)
    return render_template('CCF.html')

@app.route('/Agigreen', methods=['POST'])
def Agigreen():
    # Code pour gérer la sélection de Agigreen
    return render_template('Agigreen.html')
@app.route('/Agilog', methods=['POST'])
def Agilog():
    # Code pour gérer la sélection de Agilog
    return render_template('Agilog.html')

@app.route('/Commande', methods=['POST'])
def Commande():
    type_voiture = session.get('type_voiture')
    con = lite.connect('projet_test.db')
    pieces = con.execute('SELECT code_voiture FROM voiture_dans_commande').fetchall()
    con.close()
    print(a)
    # Code pour gérer la sélection de Agilog
    return render_template('Commande.html')

if __name__ == '__main__':
    app.run(debug=True, port=5678)
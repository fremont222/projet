from flask import Flask, render_template, request, session
import sqlite3 as lite

app = Flask(__name__)
app.secret_key = 'your_secret_key'

type_voiture = ["CLF", "CLO", "CCO","CCF"]
type_option =["An","CA","AA"]

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

@app.route('/Agilean', methods=['POST'])
def Agilean():
    # Code pour gérer la sélection de Agigreen
    return render_template('Agilean.html')
@app.route('/Agilog', methods=['POST'])
def Agilog():
    # Code pour gérer la sélection de Agilog
    return render_template('Agilog.html')


def str_list_to_bool_list(str_list):
    mapping = {"An": 0, "CA": 1, "AA": 2}
    bool_list = [False] * len(mapping)
    for str_value in str_list:
        if str_value in mapping:
            index = mapping[str_value]
            bool_list[index] = True
    return bool_list

@app.route('/Commande', methods=['POST'])
def Commande():
    """
    type_voiture = session.get('type_voiture')
    con = lite.connect('projet_test.db')
    pieces = con.execute('SELECT code_voiture FROM voiture_dans_commande').fetchall()
    con.close()
    """
    print(a)
    if request.method == 'POST':
        option= request.form.getlist('option')
    print(option)
    L_bool=str_list_to_bool_list(option)
    print(L_bool)
    return render_template('Commande.html', a=a, option=option)

if __name__ == '__main__':
    app.run(debug=True, port=5678)
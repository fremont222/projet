from flask import Flask, url_for, request, render_template, session
import sqlite3 as lite

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET'])
def index():
    return render_template('page0.html')

@app.route('/Agilean', methods=['GET','POST'])
def Agilean():
    if request.method == 'POST':
        voiture_selectionnee = None  # Réinitialise la variable à chaque fois
        for piece in pieces:
            voiture_id = f"voiture_id_{piece[0]}"
            if request.form.get(voiture_id):
                voiture_selectionnee = request.form.get(voiture_id)
                break  # Sortir de la boucle une fois qu'une voiture est sélectionnée
        if voiture_selectionnee:
            session['voiture_selectionnee'] = voiture_selectionnee
            print("Voiture sélectionnée dans la console :", session['voiture_selectionnee'])
            return render_template('Agilean_options.html', voiture_selectionnee=voiture_selectionnee)
        else:
            return "Veuillez sélectionner une voiture."
    else:
        con = lite.connect(r'C:\Users\agath\Desktop\2A\Maths info\Base de donnée- DBBrowser\projet_test.db')
        pieces = con.execute('SELECT code_voiture FROM voiture_dans_commande').fetchall()
        con.close()
        print(pieces)
        return render_template('Agilean.html', pieces=pieces)

@app.route('/Agilean_options', methods=['POST'])
def Agilean_options():
    options_selectionnees = request.form.getlist('option')
    voiture_selectionnee = session.get('voiture_selectionnee')
    if options_selectionnees :
        print("Options sélectionnées dans la console :", options_selectionnees)
        return f"Options sélectionnées : {', '.join(options_selectionnees)}, Voiture sélectionnée : {voiture_selectionnee}"
    else:
        return "Veuillez sélectionner au moins une option"

@app.route('/Agilog', methods=['GET','POST'])
def Agilog():
    return render_template('Agilog.html')

@app.route('/Agipart', methods=['GET','POST'])
def Agipart():
    return render_template('Agipart.html')

if __name__ == '__main__':
    app.run(debug=True, port=5678)
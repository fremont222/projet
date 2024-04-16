from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Exemple de données pour les voitures
pieces = [("V1",), ("V2",), ("V3",)]

@app.route('/', methods=['GET'])
def index():
    return render_template('Agilean2.html', pieces=pieces)

@app.route('/Agilean', methods=['POST'])
def Agilean():
    voiture_selectionnee = request.form.get('voiture')
    if voiture_selectionnee:
        session['voiture_selectionnee'] = voiture_selectionnee
        return render_template('Agilean_option2.html', voiture_selectionnee=voiture_selectionnee)
    else:
        return "Veuillez sélectionner une voiture."

@app.route('/Agilean_options', methods=['POST'])
def Agilean_options():
    options_selectionnees = request.form.getlist('option')
    voiture_selectionnee = session.get('voiture_selectionnee')
    if options_selectionnees:
        return f"Options sélectionnées : {', '.join(options_selectionnees)}, Voiture sélectionnée : {voiture_selectionnee}"
    else:
        return "Veuillez sélectionner au moins une option"

if __name__ == '__main__':
    app.run(debug=True, port=5678)

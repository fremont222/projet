from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('Code.html')

@app.route('/Code', methods=['POST'])
def Code():
    return render_template('Code.html')

@app.route('/CLF', methods=['POST'])
def CLF():
    # Code pour gérer la sélection de CLF
    return render_template('CLF.html')

@app.route('/CLO', methods=['POST'])
def CLO():
    # Code pour gérer la sélection de CLO
    return render_template('CLO.html')
@app.route('/CCO', methods=['POST'])
def CCO():
    # Code pour gérer la sélection de CCO
    return render_template('CCO.html')
@app.route('/CCF', methods=['POST'])
def CCF():
    # Code pour gérer la sélection de CCF
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
    # Code pour gérer la sélection de Agilog
    return render_template('Commande.html')

if __name__ == '__main__':
    app.run(debug=True, port=5678)
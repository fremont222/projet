from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Fonction pour se connecter à la base de données
def connect_db():
    return sqlite3.connect(r'Z:\Mes Documents\GitHub\projet\pythonProject\notre-projet\projet_test.db')

# Route pour afficher la page d'achat
@app.route('/achat')
def afficher_page_achat():
    # Code pour récupérer les données nécessaires à afficher sur la page (par exemple, la liste des pièces disponibles)
    db = connect_db()
    # Exemple de requête pour récupérer les pièces disponibles
    pieces = db.execute('SELECT code_piece,quantite FROM pieces_dans_commande WHERE id_commande=?', (2,)).fetchall()
    db.close()
    print(pieces)
    return render_template('achat.html', pieces=pieces)

# Route pour traiter l'achat
@app.route('/traiter_achat', methods=['POST'])
def traiter_achat():
    # Récupérer les données soumises par le formulaire d'achat
    piece_id = request.form['piece_id']
    quantite = request.form['quantite']

    # Soustraire la quantité de pièces de la base de données
    db = connect_db()
    # Exemple de requête pour soustraire la quantité de pièces
    db.execute('SELECT code_piece,quantite FROM pieces_dans_commande WHERE id_commande=?', (2))
    db.commit()
    db.close()

    # Rediriger l'utilisateur vers une page de confirmation ou de succès
    return 'Achat traité avec succès'

if __name__ == '__main__':
    app.run(debug=True, port=5678)

connect_db()

afficher_page_achat()


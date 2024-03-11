from flask import Flask, url_for, request, render_template, redirect
import sqlite3 as lite

# ------------------
# application Flask
# ------------------

app = Flask(__name__)


# ---------------------------------------
# les différentes pages (fonctions VUES)
# ---------------------------------------

# une page index avec des liens vers les différentes pages d'exemple d'utilisation de Flask
@app.route('/')
def index():
	contenu = ""
	contenu += "<a href='/afficher_personnes'>Afficher les personnes</a><br/>"
	contenu += "<a href='/ajouter_personne'>Ajouter une personne</a><br/><br/>"

	return contenu;


@app.route('/afficher_personnes', methods=['GET','POST'])
def afficher_personnes():
	if request.method == 'POST':
		recherche= request.form.get('recherche', '')
		con = lite.connect('exemples.db')
		con.row_factory = lite.Row
		cur = con.cursor()
		if recherche:
			# Requête SQL pour rechercher une personne en fonction de son ID
			cur.execute(
				"SELECT id, nom, prenom, role FROM personnes WHERE id=? OR nom LIKE ? OR prenom LIKE ? ",
				(recherche, '%' + recherche + '%', '%' + recherche + '%'))
		else:
			# Si aucun ID de recherche n'est spécifié, afficher toutes les personnes
			cur.execute("SELECT id, nom, prenom, role FROM personnes")
		lignes = cur.fetchall()
		con.close()
		return render_template('affichage_personnes.html', personnes=lignes, recherche=recherche)
	else:
		# Si la méthode HTTP est GET, afficher toutes les personnes
		con = lite.connect('exemples.db')
		con.row_factory = lite.Row
		cur = con.cursor()
		cur.execute("SELECT id, nom, prenom, role FROM personnes")
		lignes = cur.fetchall()
		con.close()
		return render_template('affichage_personnes.html', personnes=lignes, recherche='')

@app.route('/ajouter_personne', methods=['GET', 'POST'])
def ajouter_personne():
	if not request.method == 'POST':
		return render_template('formulaire_personne.html', msg="", nom="", prenom="", role=0)
	else:
		nom = request.form.get('nom', '')
		prenom = request.form.get('prenom', '')
		role = request.form.get('role', 0, type=int)

		if (nom != "" and prenom != "" and role > 0 and role < 4):
			con = lite.connect('exemples.db')
			con.row_factory = lite.Row
			cur = con.cursor()
			cur.execute("INSERT INTO personnes('nom', 'prenom', 'role') VALUES (?,?,?)", (nom, prenom, role))
			conn.commit()
			conn.close()
			return redirect(url_for('afficher_personnes'))
		else:
			return render_template('formulaire_personne.html', msg="Mauvaise saisie !", nom="", prenom="", role=0)


# ---------------------------------------
# pour lancer le serveur web local Flask
# ---------------------------------------

if __name__ == '__main__':
	app.run(debug=True, port=5678)
import sqlite3

from flask import g

from flask import Flask

# g est une variable de contexte, pour stocker des données pendant un contexte d'application
DATABASE = 'Z:\Mes Documents\GitHub\projet\pythonProject\notre-projet\projet_test.db'


def create_app():
    app = Flask(__name__)

    with app.app_context():
        init_db()

    return app

def get_db():
    db = getattr(g, '_database', None)
    if db is None: # la base de données n'est pas encore mémorisée dans le contexte
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db
# Pour s'assurer que la connexion à la base est bien fermée
# à la fermeture du contexte (fin de la session)
#@app.teardown_appcontext


def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()



def read_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv
def write_db(query, args=()):
    db = get_db()
    cur = db.execute(query, args) 
    db.commit()
    cur.close()

#Pour lire base de données : read_db("SELECT * FROM users WHERE email=?", (email,), one = True)
#Pour écrire dans base de données : write_db("INSERT INTO users VALUES (?,?,?)", (nom, email, hmdp))

create_app()

get_db()

read_db("SELECT code_piece,quantite FROM pieces_dans_commande WHERE id_commande=?;", (2,), one = True)




close_connection(exception)
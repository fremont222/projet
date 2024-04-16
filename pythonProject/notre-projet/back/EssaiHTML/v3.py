from flask import Flask, url_for, request, render_template, session
import sqlite3 as lite

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET'])
def index():
    return render_template('Code.html')


if __name__ == '__main__':
    app.run(debug=True, port=5678)
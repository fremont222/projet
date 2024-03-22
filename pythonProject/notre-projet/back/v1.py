from flask import Flask, url_for, request, render_template, redirect
app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
	return render_template('page0.html');
@app.route('/Agilean', methods=['GET','POST'])
def Agilean():
	return render_template('Agilean.html');
@app.route('/Agilog', methods=['GET','POST'])
def Agilog():
	return render_template('Agilog.html');
@app.route('/Agipart', methods=['GET','POST'])
def Agipart():
	return render_template('Agipart.html');

if __name__ == '__main__':
	app.run(debug=True, port=5678)

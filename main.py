from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

db = SQLAlchemy(app)

class User(db.Model):
	user_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique= True, nullable=False)
	user_email = db.Column(db.String(100), unique= True, nullable=False)
	password = db.Column(db.String(100), nullable=False)

	def __repr__(self):
		return f"User({self.user_id}, {self.username}, {self.user_email}, {self.password})"

class Provision(db.Model):
	prov_id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, nullable=False)
	value = db.Column(db.Integer, nullable=False)
	client_name = db.Column(db.String(20))

	def __repr__(self):
		return f"Provision({self.prov_id}, {self.user_id}, {self.value}, {self.client_name})"


@app.route("/")
@app.route("/dashboard")
def dashboard():
	return render_template("dashboard.html")

@app.route("/login")
def login():
	return render_template("login.html")

if __name__ == "__main__":   
    app.run(debug=True)

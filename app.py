from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:master#123@localhost/form'
db = SQLAlchemy(app)

class FormData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    fullname = db.Column(db.String(120), nullable=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=["POST"])
def submit_form():
    email = request.form.get('email')
    username = request.form.get('username')
    fullname = request.form.get('fullname')

    new_data = FormData(email=email, username=username, fullname=fullname)

    db.session.add(new_data)
    db.session.commit()

    return "Form submitted successfully"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

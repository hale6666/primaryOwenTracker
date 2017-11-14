from flask import Flask, render_template
from datetime import datetime
import csh_ldap
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
"""TODO: you need to get the submission page working fully, pushing things to the put request, and then build the database. 
after that you need to get ldap working, and have the submission page be a dropdown menu with all CSHers with a search """


app = Flask(__name__)
db = SQLAlchemy(app)


class Owen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)
    owen = db.Column(db.String(50))
    victory = db.Column(db.String(2000))

@app.route("/")
def main():
   return render_template('index.html')

@app.route("/submission")
def submission():
   return render_template('submission.html')

@app.route("/add_owen", methods = ['PUT'])
def add_owen():
   data = json.loads(request.data.decode('utf-8'))
   if data['owen'] and data['victory']:
      owen_data = data['owen']
      victory_data = data['victory']
      new_owen = Owen(time=datetime.now(), owen=owen_data, victory=victory_data  )

      


if __name__ == "__main__":
    app.run()

application = app

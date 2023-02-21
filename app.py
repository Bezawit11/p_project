from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

class Product(db.Model):
  name = db.Column(db.String(30), nullable=False, unique=True, primary_key=True)
  price = db.Column(db.Integer(), nullable=False)

  def __init__(self, name, price):
    self.name = name
    self.price = price


with app.app_context():
    db.create_all()

@app.route("/")
def hello():
  product = Product.query.all()
  return render_template('home.html', product=product)
  

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

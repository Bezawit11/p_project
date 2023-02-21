from flask import Flask, render_template

app = Flask(__name__)

JOBS =[{
  'id': 1,
  'question': 'Who made is c?'
},
      {
        'id': 2,
        'question': 'Who made python?'
      }]
@app.route("/")
def hello():
  return render_template('home.html', jobs=JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

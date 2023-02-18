from flask import Flask, render_template

app = Flask(__name__)

JOBS =[{
  'id': 1,
  'type': 'C'
},
      {
        'id': 2,
        'type': 'Python'
      }]
@app.route("/")
def hello():
  return render_template('home.html', jobs=JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
  return render_template('index.html')

@app.route("/about")
def about():
  return "<p>This is not not the about page.</p>"

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)


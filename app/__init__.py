from flask import Flask 
from flask import render_template
from random import randint 
from flask import redirect
from flask import request

# Create the app 
app = Flask(__name__)


# home page - loading a static page
@app.get("/")
def home():
  return render_template('pages/home.jinja')
# about page - loading a static page
@app.get("/about/")
def about():
  return render_template('pages/about.jinja')
# random number page - passing a value into the template
@app.get("/random/")
def random():
 randNum = (randint(1,100000))
 return render_template('pages/random.jinja', number=randNum)
# Number page - Getting a value from the route and passing it into template
@app.get("/number/<int:num>")
def analyseNumber(num):
  print(f"You entered:{num}")
  return render_template("pages/number.jinja", number=num)
# Form page - static page with a form
@app.get("/form/")
def form():
  return render_template('pages/form.jinja')

# handle data posted from form
app.post("/processForm")
def processForm():
  print(f"form data: ${request.form}")
  return render_template(
    "pages/formData.jinja",
    name=request.form["name"],
    age=request.form["age"]
  )
# error handler - Handle any missing pages
@app.errorhandler(404)
def notFound(e):
  return render_template("pages/404.jinja")


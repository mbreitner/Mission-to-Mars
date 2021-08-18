### Begin Process of Creating a Flask App

#import dependencies
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

# set up flask
app = Flask(__name__)

# tell python how to connect to mongo using PyMongo
#use flask_pymongo to set up a mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
#app.config["MONGO_URI"] tells python that our app will connect to mongo using a URI (uniform resource identifier similiar to a URL)
# everything after the = is the URI we are using to connect to mongo
mongo = PyMongo(app)

# define the route for the html page (module 10.5.1)
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

# define the scraping route
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return redirect('/', code=302)

#tell flask to run
if __name__ == "__main__":
    app.run()

#Dependencies and Setup
from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import scrape_mars

#use flask_pymongo to set up mongo connection
app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

#mainpage
@app.route("/")
def homepage():
    mars = mongo.db.mars.find_one()

    return render_template("index.html", mars = mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_all()
    mars.update({}, mars_data, upsert = True)

    return redirect("/", code = 302)

if __name__ == "__main__":
    app.run(debug = True)
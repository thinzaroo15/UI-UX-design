
from flask import Flask , render_template, request, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/unitozawgyi")
def unitozawgyi():
    return render_template("unitozawgyi.html")

@app.route("/zawgyitouni")
def zawgyitouni():
    return render_template("zawgyitouni.html")

@app.route("/wintouni")
def wintouni():
    return render_template("wintouni.html")

@app.route("/unitowin")
def unitowin():
    return render_template("unitowin.html")

@app.route("/wintozawgyi")
def wintozawgyi():
    return render_template("wintozawgyi.html")
	
@app.route("/zawgyitowin")
def zawgyitowin():
    return render_template("zawgyitowin.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/howitwork")
def howitwork():
    return render_template("howitwork.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/question")
def question():
    return render_template("question.html")

@app.route("/about1")
def about1():
    return render_template("about1.html")

@app.route("/howitwork1")
def howitwork1():
    return render_template("howitwork1.html")

@app.route("/resources1")
def resources1():
    return render_template("resources1.html")

@app.route("/contact1")
def contact1():
    return render_template("contact1.html")

@app.route("/question1")
def question1():
    return render_template("question1.html")

if __name__ == "__main__":
    app.run(debug=True)


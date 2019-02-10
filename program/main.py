from flask import Flask, render_template
app = Flask("book_api")


@app.route("/", methods=['GET'])
@app.route("/api/", methods=['GET'])
@app.route("/home/", methods=['GET'])
def home():
    return render_template("home_template.html")

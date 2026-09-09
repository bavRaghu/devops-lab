from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def registration_form():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register_student():
    name = request.form["name"].strip()
    year = request.form["year"].strip()
    return render_template("success.html", name=name, year=year)


if __name__ == "__main__":
    app.run(debug=True)

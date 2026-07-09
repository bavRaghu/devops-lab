from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("registration.html")

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    year = request.form['year']
    return render_template("success.html", n=name, y=year)

if __name__ == "__main__":
    app.run(debug=False)
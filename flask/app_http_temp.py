from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("home_http.html")

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        return render_template("form_http.html", name=name, age=age)
    return render_template("form_http.html", name=None, age=None)  # fixed "age" here

@app.route("/about", methods=["GET"])
def about():
    return "<h1>About Page</h1><p>This is a simple About page.</p>"

if __name__ == "__main__":
    app.run(debug=True)

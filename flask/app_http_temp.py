from flask import Flask,render_template,request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("home_http.html")


@app.route("/form", methods=["GET","POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        return render_template("form_http.html", name=name)
    return render_template("form_http.html", name=None) 


if __name__ == "__main__":
    app.run(debug=True)  
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        return f"Hello , {username}. Your passwrod is {password}"
    return render_template("login.html")


#Code without templates:
# @app.route("/search")
# def search():
#     name = request.args.get("name")   # from URL query parameter
#     return f"You searched for: {name}"

# @app.route("/login", methods=["POST"])
# def login():
#     username = request.form.get("username")  # from form
#     password = request.form.get("password")
#     return f"Username: {username}, Password: {password}"

# @app.route("/json", methods=["POST"])
# def json_data():
#     data = request.get_json()   # from JSON body
#     return {"you_sent": data}


if __name__ == "__main__":
    app.run(debug=True)
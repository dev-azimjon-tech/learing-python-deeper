from flask import Flask, request, render_template

app = Flask(__name__)

# Task 1:
# @app.route("/info", methods=["GET","POST"])
# def city_country():
#     if request.method == "POST":
#         country = request.form.get("country")
#         city = request.form.get("city")
#         return f"You live in : {country}, and in city: {city}"
#     return render_template("index.html")

# @app.route("/city_search", methods=["GET","POST"])
# def city_search():
#     if request.method == "GET":
#         city_name = request.args.get("city-name")
#         return f"You searched for: {city_name}"



if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)


# Task 1:
# Hello World App
# Create a simple Flask app that displays "Hello, World!" at the home page (/ route).
# Add another route, e.g., /about, that returns a short bio.
# @app.route('/')
# def hello():
#     return "<p>Hello World!</p>"

# @app.route('/about')
# def about():
#     return "<h1>About Page</h1>"

# Task 2:
# Dynamic URL
# Create a route /greet/<name> that displays "Hello, <name>!" dynamically based on the URL.

# @app.route('/greet/<name>')
# def greet(name):
#     return f"<h1>Hello {name}!</h1>"

# if __name__ == "__main__":
#     app.run(debug=True)

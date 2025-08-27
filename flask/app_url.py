#URL Building
from flask import Flask, url_for

app = Flask(__name__)

# @app.route('/')
# def index():
#     return "Home Page"

# @app.route('/user/<username>')
# def profile(username):
#     return f"Profile of {username}"

# @app.route('/links')
# def link():
#     home_url = url_for('index')
#     profile_url = url_for('profile', username="Azimjon")
#     return f"Home: {home_url}, Profile: {profile_url}"


# Tasks:
# Task 1:
# @app.route('/')
# def home():
#     return "Welocome to Home Page"

# @app.route('/links')
# def links():
#     home_url = url_for('home')
#     return home_url

# Task 2:
# @app.route('/user/<username>')
# def profile(username):
#     return f"Hello {username}"

# @app.route('/links')
# def links():
#     profile_url = url_for('profile', username="Pavel")
#     return profile_url

# Task 3:
@app.route('/post/<int:post_id>')
def post(post_id):
    return f"Post {post_id}"

@app.route('/links')
def links():
    post_urls = url_for('post', post_id=5)
    return f"Link for {post_urls}  `google.com`"


if __name__ == "__main__":
    app.run(debug=True)
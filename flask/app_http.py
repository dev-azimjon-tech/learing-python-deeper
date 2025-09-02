from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=["GET"])
def home():
    return "Welcome! Use /form to send data"


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        return f"Hello {name}! You used POST"
    return '''''
        <form method="POST">
            <input type="text" name="name" placeholder="Enter your name">
            <input type="submit">
        </form>
    '''


if __name__ == "__main__":
    app.run(debug=True)
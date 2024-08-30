import random
from flask import Flask, render_template, request

# Config

app = Flask(__name__)
app.secret_key = "234hj32v4k32b4jb32lj4b32lj4"
app.config["WTF_CSRF_ENABLED"] = False  # Disable CSRF protection

# Define the custom random function
def random_id(length: int =8):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(length))

# Add the custom function to the Jinja2 environment
app.jinja_env.globals['random_id'] = random_id
# Routing


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
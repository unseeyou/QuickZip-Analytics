from constants import app

from flask import (
    render_template,
    request,
    redirect,
)

@app.route("/")
def index():
    return "under construction"


if __name__ == "__main__":
    app.run(debug=True, host="localhost")

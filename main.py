from constants import app



@app.route("/")
def index():
    return "under construction"


if __name__ == "__main__":
    app.run(debug=True, host="localhost")

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/femboy")
def hello_femboy():
    return render_template("Femboy.html")

@app.route("/Therian_Photos")
def hello_therian_photos():
    return render_template("Therian_Photos.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True) 
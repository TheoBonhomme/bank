from flask import Flask, render_template

app = Flask(__name__)

@app.route("/bonjour")

def bonjour():
	data = "robert"
	return render_template("bonjour.html", data = data)

app.run(port = 12345, debug = True)
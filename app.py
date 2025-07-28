from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/management")
def management():
	return render_template("management.html")

@app.route("/courses")
def courses():
	return render_template("courses.html")

@app.route("/contact")
def contact():
	return render_template("contact.html")

if __name__ == '__main__':
	app.run(debug=True)

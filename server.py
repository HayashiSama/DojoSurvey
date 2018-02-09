from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key = '0118999881999119725'


# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")


@app.route('/results', methods=['POST'])
def ninjas():
	name = request.form['name']
	location = request.form['location']
	language = request.form['language']
	comments=request.form['comments']
	email=request.form['email']
	if(len(name)==0):
		flash("Name cannot be empty!")
		return redirect('/')
	if(len(email) < 1):
		flash("Email cannot be empty!")
		return redirect('/')
	elif not EMAIL_REGEX.match(email):
		flash("Invalid Email Address!")	
		return redirect('/')
	if(len(comments)>140):
		flash("Comments must be under 140 chars")	
		return redirect('/')
	if(len(comments)<1):
		flash("Comments cannot be blank")	
		return redirect('/')
	
  	return render_template("results.html", name=name, location=location, language=language, comments=comments)

@app.route('/color', methods=['POST'])
def colorify():
	red=int(request.form['red'])
	green=int(request.form['green'])
	blue=int(request.form['blue'])
	if(red >= 0 and red <= 255 and green >= 0 and green <= 255 and blue >= 0 and blue <= 255):
		print "Color in bounds"
		return render_template("index.html", red=red, green=green, blue=blue)
	else:
		return render_template("index.html", error=True)

app.run(debug=True) # run our server
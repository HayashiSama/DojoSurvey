from flask import Flask, render_template, request, redirect
app = Flask(__name__)
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
	print name
	print location
	print language

	
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
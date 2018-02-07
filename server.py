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



app.run(debug=True) # run our server
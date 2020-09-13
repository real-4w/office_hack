#https://developer.here.com/blog/here-map-with-python-flask
#now i need to master Jinja to umpdate the template file before it gets rendered.
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def map_func():
	return render_template('map.html', lat = -36.8484769, long = 174.7652662)
if __name__ == '__main__':
    app.run(debug = True)    
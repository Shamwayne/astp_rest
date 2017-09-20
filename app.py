from flask import *
from restapi import *


app = Flask(__name__)

@app.route("/")
def hello():
	return "<h1> API functions are on the <code>/api/</code> route </h1>"


if __name__ == '__main__':
	app.run(debug=True)

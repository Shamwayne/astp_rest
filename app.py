from flask import *
import restapi


app = Flask(__name__)

restapi.add_api_endpoints(app)


@app.route("/")
def hello():
	return "<h1> API functions are on the <code>/api/</code> route </h1>"



if __name__ == '__main__':
	app.run(debug=True)

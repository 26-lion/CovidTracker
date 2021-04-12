from flask import Flask,render_template,request
import requests 
import json
app = Flask(__name__)


def statistics(state):
	confirm = state["confirm"]
	cured = state["cured"]
	death = state["death"]
	total = state["total"]
	return confirm,cured,death,total




@app.route("/", methods=["GET","POST"])

def index():
	if request.method=="POST":
		url = "https://covid-19-india2.p.rapidapi.com/details.php"

		headers = {
		'x-rapidapi-key': "5bf8a327c3msh7bd827f26a073e0p1cb7c8jsncfad9a99c69f",
		'x-rapidapi-host': "covid-19-india2.p.rapidapi.com"
		}

		response = requests.request("GET", url, headers=headers)

		data = json.loads(response.content)
		state = request.form["country"]
		confirm,cured,death,total = statistics(data[state])

		return render_template("index.html", data=data[state], file="corona.jpg",confirm=confirm, cured=cured, death=death, total=total, statement="Covid Report of "+state+" is as follows")
	else:
		data=""
		return render_template("index.html", data=data, file="corona.jpg", confirm="", cured="", death="", total="", statement="Please Select a State/Union Territory")

if __name__ == "__main__" :
	app.run(debug=True)


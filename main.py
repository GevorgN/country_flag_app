from flask import Flask
from flask import request
from flask import render_template
import requests


app = Flask(__name__)
app.config["DEBUG"] = False


@app.route("/", methods=['POST', 'GET'])
def home_view():
    if request.method == 'POST':
        country = request.form['country']
        try:
            url_for_request = f'https://restcountries.eu/rest/v2/name/{country}'
            response = requests.get(url_for_request)
            data = response.json()[0]
            url = data.get('flag')
        except:
            return render_template('error.html', name=country)
        return render_template('flag.html', url=url)
    return render_template('home.html')

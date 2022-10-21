from flask import Flask, render_template
import requests
import json
import os
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def get_meal_rec():

   response = requests.get('http://' + str(os.environ.get("API_HOST")) + ':' + str(os.environ.get("API_PORT")) + "/" + str(os.environ.get("API_ENDPOINT")))
   response = response.content
   response = json.loads(response)
   meal = response['Meal']
   price = response['Price']
   
   return render_template('yummy.html', meal = meal, price = price)


app.run(debug=True, host='0.0.0.0', port=os.environ.get('CONSUMER_PORT'))
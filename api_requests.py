import requests
import json

"""
	Jsonify get request
"""

response = requests.get("https://api.trumail.io/v2/lookups/json?email=mannnonegra@gmail.com"
print(json.loads(response.text))
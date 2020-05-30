import requests
import json
import tqdm

"""
	Pass emails here
	emails : []
"""

results = []
for email in tqdm(emails):
    if email is not None:
        response = requests.get("https://api.trumail.io/v2/lookups/json?email="+str(email))
        try:
            results.append({"valide_format" :json.loads(response.text)["validFormat"],
                            "deliverable" : json.loads(response.text)["deliverable"]})
        except:
            results.append({"valide_format":False, "deliverable":False})
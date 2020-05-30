import requests
import json
import tqdm


"""
	email : str
	returns : {	'address': 'my_email@gmail.com',
 			   	'username': 'my_email',
 			   	'domain': 'gmail.com',
 				'md5Hash': '19b021ad275fae318696ab8027aec424',
 				'suggestion': '',
 				'validFormat': True,
 				'deliverable': False,
 				'fullInbox': False,
 				'hostExists': True,
 				'catchAll': False,
 				'gravatar': False,
 				'role': False,
 				'disposable': False,
 				'free': True}
"""

def check_email(email):
	response = requests.get("https://api.trumail.io/v2/lookups/json?email="+str(email))
	return json.loads(response.text)
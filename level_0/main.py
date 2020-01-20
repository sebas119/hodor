import requests

payload = {'id': 1182, 'holdthedoor': 'Submit'}
url = "http://158.69.76.135/level0.php"

for i in range(0, 1024):
    r = requests.post(url, allow_redirects=False, data=payload)
    print("sending post request no. {}".format(i))

########################################################################################
# mfit api implementation
import requests

# url = "http://portal.mfit.co.in/rest/file/scrape?apiKey=API_KEY"
# url = "http://portal.mfit.co.in/rest/file/scrape?apiKey=537c9f95-d279-468c-aa78-6edbffab7bc8"

payload = {'password': '12345678'}
files = [
  ('file', open('/var/www/html/temp/test.pdf','rb'))
]
headers= {}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))

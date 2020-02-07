import requests

url = "https://mail.ukr.net/widget?lang=uk"

response = requests.request("GET", url)
print(response.status_code)


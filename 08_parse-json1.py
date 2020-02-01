
import urllib.parse
import requests
# cambiar la key customer del profe por la mia

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Quito, Cotocollao"
dest = "Quito, Ofelia"
key = "MBGX4ICpnM56NpGtpOCkHOLzyFVww9UM"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data)

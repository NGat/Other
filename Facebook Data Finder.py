import requests
def facebook():
  access = "" #         <<<< Insert access token here
  URL = raw_input("Facebook username>>>")
  data = requests.get("https://graph.facebook.com/" + URL+"?access_token="+access).json()
  for x in data:
      print x + ":" , data[x]
while True:
  facebook()


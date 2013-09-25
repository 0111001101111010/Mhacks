#using utf-8
from twilio.rest import TwilioRestClient
import urllib2
import urlparse
import requests
import pprint
from flask import Flask
#app = Flask(__name__)

#@app.route("/")
#def hello():
#   	return "Hello World!"

account = "AC25ca07e6de65c06312ef13d3a9e78c28"
token = "d3b770a8afddf0c57a6a64e43a8e8da6"
client = TwilioRestClient(account, token)

#twillio  +17573374787
#mynumber +13473993732

req = requests.get(url = 'http://lit-inlet-3610.herokuapp.com/api/routes/active/')
#print req
req = req.json()

#print req

time = requests.get(url = 'http://lit-inlet-3610.herokuapp.com/api/stops/near/36.866978/-76.307433/')

time = time.json()

#print time

#while req 
#for route in req:
 	#print route["route_long_name"]
#i = iter(req)
#print i.next()
#print i.next()
#print  req[len(item)].long_route_names
#print req
#print req[0].long_route_names

message = client.messages.create(to="+13473993732", from_="+17573374787",
                                 body="The requested bus has departed, if you require another reply MORE ")

#if __name__ == "__main__":
 #   app.run()

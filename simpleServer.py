#!/usr/bin/python3

import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import urllib
import json
import configparser

from maradek.maradek import *

config = configparser.ConfigParser()
config.read('simpleServer.properties')
hostName = "localhost"
hostPort = int(config['BASIC']['PORT'])

class MyServer(BaseHTTPRequestHandler):

	#	GET is for clients geting the predi
	def do_GET(self):
		self.send_response(200)
		self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))

	#	POST is for submitting data.
	def do_POST(self):
           
           
           

           if self.path == "/maradek":
             #send response status code
             self.send_response(200)
             

             length = int(self.headers['Content-Length'])
             post_data = self.rfile.read(length).decode('utf-8')
             de_data=json.loads(post_data)
             solution=assign_holidays(de_data)
                  
             #send header
             self.send_header('Content-type','application/json')
             self.end_headers()
             
             #send response
             resp=json.dumps(solution)
             self.wfile.write(resp.encode("utf-8"))

           else:
              self.send_response(400)
           


myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
	myServer.serve_forever()
except KeyboardInterrupt:
	pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))

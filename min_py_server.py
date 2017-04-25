#!/usr/bin/env python

# Inspired by https://gist.github.com/jtangelder/e445e9a7f5e31c220be6
# Python3 http.server for Single Page Application

import http.server
import socketserver
import re
from pathlib import Path
PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		request_file_path = Path(self.path.strip("/"))

		if not request_file_path.is_file():
			self.path = 'edit.html'
		
		return http.server.SimpleHTTPRequestHandler.do_GET(self)

try :
	HOST = ('', PORT)
	httpd = socketserver.TCPServer(HOST, Handler)
	httpd.serve_forever()
except KeyboardInterrupt:
	httpd.server_close()


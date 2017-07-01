#!/usr/bin/env python
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import socket

class PostClient(BaseHTTPRequestHandler):

    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

    def do_POST(self):
        def do_GET(self):
            # Send response status code
            self.send_response(200)

            # Send headers
            self.send_header('Content-type', 'text/html')
            self.end_headers()
        print()
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        ConvertJson(self.data_string)



def run():
    ipAdress = socket.gethostbyname(socket.gethostname())
    if ipAdress == "127.0.1.1":
        ipAdress = socket.getfqdn()

    print("Starting Fronius Listener with IP: {0}".format(ipAdress))
    server_address = (ipAdress, 40)
    httpd = HTTPServer(server_address, PostClient)
    httpd.serve_forever()

def ConvertJson(text):
    data = json.loads(text)
    print("Timestamp: {0}".format(data["Head"]["Timestamp"]))
    print("Current Production: {0}{1}".format(data["Body"]["PAC"]["Values"]["1"],data["Body"]["PAC"]["Unit"]))
    print("Today's Yeild: {0}{1}".format(data["Body"]["DAY_ENERGY"]["Values"]["1"],data["Body"]["DAY_ENERGY"]["Unit"]))


run()
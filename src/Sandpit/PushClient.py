#!/usr/bin/env python
from bs4 import BeautifulSoup
from http.server import BaseHTTPRequestHandler, HTTPServer


# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    # GET
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
        print("POST Packet Recieved")
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        soup = BeautifulSoup(self.data_string, "lxml")
        print(soup.prettify())


def run():
    print('starting server...')

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('10.1.1.15', 40)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()


run()
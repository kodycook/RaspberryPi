#!/usr/bin/env python
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import socket



# HTTPRequestHandler class
class PostClient(BaseHTTPRequestHandler):

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
        print()
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        ConvertJson(self.data_string)
        #soup = BeautifulSoup(self.data_string, "lxml") # Maybe these two lines aren't necessary



def run():
    print('Starting Fronius Listener')


    # Test
    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    # server_address = ('10.1.1.15', 40)
    # httpd = HTTPServer(server_address, PostClient)
    # httpd.serve_forever()

    server = socket.socket()
    server.bind(('10.1.1.15', 40))
    server.listen(4)
    client_socket, client_address = server.accept()
    print(client_address, "has connected")
    while 1 == 1:
        recieved_data = client_socket.recv(1024)
        ConvertJson(recieved_data)

def ConvertJson(text):
    print(text)

    # data = json.loads(text)
    # print("Timestamp: {0}".format(data["Head"]["Timestamp"]))
    # print("Current Production: {0}{1}".format(data["Body"]["PAC"]["Values"]["1"],data["Body"]["PAC"]["Unit"]))
    # print("Today's Yeild: {0}{1}".format(data["Body"]["DAY_ENERGY"]["Values"]["1"],data["Body"]["DAY_ENERGY"]["Unit"]))
    #print(data[""])
    #print(data[""])



    #print(type(obj))
    #print(obj.tostring())


run()